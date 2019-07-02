// @flow
import pathlib from './pathlib';
import pdf from 'pdf-parse';

const trace = console.warn;


async function main(argv, { stdout, readFile, writeFile, resolve, fsp }) {
    const cwd = pathlib.fsAdminAccess('.', {
        readFile, resolve, writeFile,
        open: fsp.open, rename: fsp.rename, utimes: fsp.utimes,
    });
    let hdDone = false;
    for (const stmt of argv.slice(2)) {
        trace(stmt);

        const path = cwd.joinPath(stmt);
        const raw = await path.readOnly().readBytes();
        trace('raw bytes: ', raw.length);

        // https://www.npmjs.com/package/parse-pdf
        // based on https://mozilla.github.io/pdf.js/getting_started/
        const data = await pdf(raw);

        // trace('// PDF text', data.text);
        const info = portfolioSummary(data.text);
        trace(info);
        const { header, body } = asQIF(info);
        if (!hdDone) {
            for (const line of header) {
                stdout.write(line + '\n');
            }
            hdDone = true;
        }
        for (const line of body) {
            stdout.write(line + '\n');
        }

        const [_, t] = info.period;
        await setDate(path, t);
    }
}


function asQIF(info,
               typeA = 'Oth A',
               asset = 'Fixed:Retirement:IRA Daniel',
               mp = 'OB:Market Performance',
               svc = 'OB:Services',
               ira = 'Fixed:Retirement:IRA Daniel') {
    const [_, dt] = info.period;
    const qn = Math.floor(dt.getMonth() / 3) + 1;

    const money = f => Math.round(f * 100) / 100;
    const parseAmt = txt => money(parseFloat(txt.replace(/[$, ]/g, '')));
    const splitCats = [null, null, mp, mp, mp, svc, mp, null];
    const splits = info.detail.map(
        ([memo, q1, ytd], ix) =>
            ({ memo, raw: q1, amt: parseAmt(q1), cat: splitCats[ix]}));
    trace(splits);
    const splitLines = splits.filter(
        s => s.cat !== null && s.amt !== null && s.amt !== 0)
          .map(s => [`S${s.cat || ''}`, `E${s.memo}`, `$${s.amt}`]);

    const amount = money(splits[7].amt - splits[1].amt);
    const header = [
        '!Account',
        `N${asset}`,
        `T${typeA}`,
        '^',
        `!Type:${typeA}`,
    ];
    const main = [
        `PQ${qn} Portfolio Summary`,
        `T${amount}`,
        `Mbegin: ${splits[1].raw} end: ${splits[7].raw}`,
        `D${dt.getMonth() + 1}/${dt.getDate()}/${dt.getFullYear()}`,
        'Cc',
    ];
    const body = splitLines.reduce((acc, more) => [...acc, ...more], main);
    return {
        header,
        body: [...body, '^'],
    };
}


async function setDate(stmt, t) {
    trace(`fh = open(${stmt.name()})`);
    trace(`await fh.utimes(${t}, ${t})`);
    const fh = await stmt.open();
    await fh.utimes(t, t);
    const name = `summit${t.toISOString().slice(0, 7)}-dwc.pdf`;
    trace(`fsp.rename(${stmt.name()}, ${stmt.joinPath(name).name()})`);
    stmt.rename(stmt.joinPath(name).name());
}


function portfolioSummary(text) {
    const mustMatch = (target, text) => {
        const parts = text.match(target);
        if (parts === null) { throw new Error(target); }
        return parts;
    };

    const reportingPeriod = (
        mustMatch(/^REPORTING PERIOD:\n([^ ]+) through ([^ ]+)/m, text)
            .slice(1, 3)
    );

    const mustFind = (target, text) => {
        const ix = text.indexOf(target);
        if (ix < 0) { throw new Error(target); }
        return ix;
    };

    const section = (start, end) => {
        const lo = mustFind(start, text);
        const rest = text.slice(lo);
        const hi = mustFind(end, rest);
        return rest.slice(start.length, hi).trim().split('\n');
    };

    return {
        detail: changeDetail(section('PORTFOLIO CHANGES', 'Since Inception')),
        'REPORTING PERIOD': reportingPeriod,
        period: reportingPeriod.map(from_mmddyy),
    };
}


/**
 * Between **PORTFOLIO CHANGES** and **Since Inception** headings,
 * we expect to find:
 *
 *  1. colhd2/colhd3
 *  2. colhd2colhd3
 *  3. rowhd999.99999.99
 *  4. rowhd999.99999.99
 *  5. ...
 *
 * We use the / to split colhd2 from colhd3 on line 2, and we know
 * amounts have exactly 2 digits after the decimal.
 */
function changeDetail(changes) {
    trace(changes);
    const rowHdAmt1Amt2 = /([^\-0-9,$]+)([\- 0-9,$]+\.[0-9]{2})(.*)/;
    const detail = changes.reduce(
        (d, line) => (
            d.state === 'head1' ? {
                state: 'head23',
                th: line, slash: line.indexOf('/'),
            } :
            d.state === 'head23' ? {
                state: 'body',
                rows: [[
                    d.th,
                    line.slice(0, d.slash),
                    line.trim().slice(d.slash),
                ]],
            } :
            // d.state must be 'body'
            {
                state: 'body',
                rows: [...d.rows,
                       line.trim().match(rowHdAmt1Amt2).slice(1, 4)]
            }),
        { state: 'head1' });

    return detail.rows;
}


function from_mmddyy(txt) {
    // trace(txt);
    const [mm, dd, yy] = txt.split('/').map(dd => parseInt(dd, 10));
    const yr = (yy < 50 ? 2000 : 1900) + yy;
    return new Date(yr, mm - 1, dd);
}


/* global require, process, module */
if (require.main === module) {
    main(process.argv, {
        stdout: process.stdout,
        // TODO: don't import fs so many times; just use .promises
        readFile: require('fs').readFile,
        writeFile: require('fs').writeFile,
        fsp: require('fs').promises,
        resolve: require('path').resolve,
    })
        .then(_ => null)
        .catch((oops) => { console.error(oops); });
}
