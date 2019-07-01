// @flow
import pathlib from './pathlib';
import pdf from 'pdf-parse';

async function main(argv, { readFile, join }) {
    // console.log('argv:', argv);
    const stmt = argv[2];
    const rd = pathlib.fsReadAccess(stmt, readFile, join);

    const raw = await rd.readBytes();
    console.log('raw bytes: ', raw.length);
    // https://www.npmjs.com/package/parse-pdf
    // based on https://mozilla.github.io/pdf.js/getting_started/
    const data = await pdf(raw);

    // console.log('// PDF text', data.text);
    const rows = portfolioChanges(data.text);
    console.log(rows);
}


function portfolioChanges(text) {
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
            out = {'REPORTING PERIOD': parts.slice(1, 3), ...out};
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
    return out;
}


/* global require, process, module */
if (require.main === module) {
    main(process.argv, {
        readFile: require('fs').readFile,
        join: require('path').join,
    })
        .then(_ => null)
        .catch((oops) => { console.error(oops); });
}
