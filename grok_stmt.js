// @flow
import pathlib from './pathlib';
import pdf from 'pdf-parse';

async function main(argv, { stdout, readFile, resolve, fsp }) {
    const cwd = pathlib.fsReadAccess('.', { readFile, resolve });
    let hdDone = false;
    for (const stmt of argv.slice(2)) {
        console.warn(stmt);

        const rd = cwd.joinPath(stmt);
        const raw = await rd.readBytes();
        console.warn('raw bytes: ', raw.length);

        // https://www.npmjs.com/package/parse-pdf
        // based on https://mozilla.github.io/pdf.js/getting_started/
        const data = await pdf(raw);

        // console.warn('// PDF text', data.text);
        const info = portfolioSummary(data.text);
        console.warn(info);
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

        const fh = await fsp.open(rd.name());
        const [_, t] = info.period;
        await setDate(fh, rd, t);
    }
}


function asQIF(info) {
    const typeA = 'Oth A';
    const dt = info.period[1];
    const qn = Math.floor(dt.getMonth() / 3) + 1;

    const money = f => Math.round(f * 100) / 100;
    const parseAmt = txt => money(parseFloat(txt.replace(/[$, ]/g, '')));
    const asset = 'Fixed:Retirement:IRA Daniel';
    const [mp, svc, ira] = ['OB:Market Performance', 'OB:Services',
                            'Fixed:Retirement:IRA Daniel'];
    const splitCats = [null, null, mp, mp, mp, svc, mp, null];
    const splits = info.detail.map(
        ([memo, q1, ytd], ix) =>
            ({ memo, amt: parseAmt(q1), cat: splitCats[ix]}));
    console.warn(splits);
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
        `D${dt.getMonth() + 1}/${dt.getDate()}/${dt.getFullYear()}`,
        'Cc',
    ];
    const body = splitLines.reduce((acc, more) => [...acc, ...more], main);
    return {
        header,
        body: [...body, '^'],
    };
}


async function setDate(fh, rd, t) {
    console.warn(`fh = open(${rd.name()})`);
    console.warn(`await fh.utimes(${t}, ${t})`);
    const name = `summit${t.toISOString().slice(0, 7)}-dwc.pdf`;
    console.warn(`fsp.rename(${rd.name()}, ${rd.joinPath(name).name()})`);
}


function portfolioSummary(text) {
    let state = null;
    let rows = [];
    let row = [];
    let out = {};
    for (const line of text.split('\n')) {
        // console.warn(line);
        if (line.startsWith('REPORTING PERIOD:')) {
            state = 'reporting';
        } else if (state === 'reporting') {
            const parts = line.match(
                    /([^ ]+) through ([^ ]+)/);
            out = { 'REPORTING PERIOD': parts.slice(1, 3), ...out };
            state = null;
        }

        if (state === null && line.trim() === 'PORTFOLIO CHANGES') {
            state = 'head1';
        } else if (line.trim() === 'Since Inception') {
            out = {detail: rows, ...out};
            break;
        } else if (state === 'head1') {
            row.push(line.trim());
            state = 'head23';
        } else if (state === 'head23') {
            const slash = row[0].indexOf('/');
            row.push(line.slice(0, slash));
            row.push(line.trim().slice(slash));
            rows.push(row);
            row = [];
            state = 'body';
        } else if (state === 'body') {
            // console.warn('line:', line);
            const parts = line.trim().match(
                    /([^\-0-9,$]+)([\- 0-9,$]+\.[0-9]{2})(.*)/);
            rows.push(parts.slice(1, 4));
        }
    }

    out = { period: out['REPORTING PERIOD'].map(from_yymmdd), ...out };

    return out;
}


function from_yymmdd(txt) {
    // console.warn(txt);
    const [mm, dd, yy] = txt.split('/').map(dd => parseInt(dd, 10));
    const yr = (yy < 50 ? 2000 : 1900) + yy;
    return new Date(yr, mm - 1, dd);
}


/* global require, process, module */
if (require.main === module) {
    main(process.argv, {
        stdout: process.stdout,
        readFile: require('fs').readFile,
        fsp: require('fs').promises,
        resolve: require('path').resolve,
    })
        .then(_ => null)
        .catch((oops) => { console.error(oops); });
}
