// @flow
import pathlib from './pathlib';
import pdf from 'pdf-parse';

async function main(argv, { readFile, resolve, fsp }) {
    const cwd = pathlib.fsReadAccess('.', { readFile, resolve });
    for (const stmt of argv.slice(2)) {
        console.log(stmt);
        const rd = cwd.joinPath(stmt);

        const raw = await rd.readBytes();
        console.log('raw bytes: ', raw.length);
        // https://www.npmjs.com/package/parse-pdf
        // based on https://mozilla.github.io/pdf.js/getting_started/
        const data = await pdf(raw);

        // console.log('// PDF text', data.text);
        const info = portfolioSummary(data.text);
        console.log(info);

        const fh = await fsp.open(rd.name());
        const [_, t] = info.period;
        await setDate(fh, rd, t);
    }
}


async function setDate(fh, rd, t) {
    console.log(`fh = open(${rd.name()})`);
    console.log(`await fh.utimes(${t}, ${t})`);
    const name = `summit${t.toISOString().slice(0, 7)}-dwc.pdf`;
    console.log(`fsp.rename(${rd.name()}, ${rd.joinPath(name).name()})`);
}


function portfolioSummary(text) {
    let state = null;
    let rows = [];
    let row = [];
    let out = {};
    for (const line of text.split('\n')) {
        // console.log(line);
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
            // console.log('line:', line);
            const parts = line.trim().match(
                    /([^\-0-9,$]+)([\- 0-9,$]+\.[0-9]{2})(.*)/);
            rows.push(parts.slice(1, 4));
        }
    }

    out = { period: out['REPORTING PERIOD'].map(from_yymmdd), ...out };

    return out;
}


function from_yymmdd(txt) {
    // console.log(txt);
    const [mm, dd, yy] = txt.split('/').map(dd => parseInt(dd, 10));
    const yr = (yy < 50 ? 2000 : 1900) + yy;
    return new Date(yr, mm - 1, dd);
}


/* global require, process, module */
if (require.main === module) {
    main(process.argv, {
        readFile: require('fs').readFile,
        fsp: require('fs').promises,
        resolve: require('path').resolve,
    })
        .then(_ => null)
        .catch((oops) => { console.error(oops); });
}
