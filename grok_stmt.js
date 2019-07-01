// @flow
import pathlib from './pathlib';
import pdf from 'pdf-parse';

async function main(argv, { readFile, join }) {
    console.log('argv:', argv);
    const stmt = argv[2];
    const rd = pathlib.fsReadAccess(stmt, readFile, join);

    const raw = await rd.readBytes();
    console.log('raw bytes: ', raw.length);
    const data = await pdf(raw);
    console.log('// number of pages', data.numpages);
    console.log('// number of rendered pages', data.numrender);
    
    console.log('// PDF info', data.info);
    console.log('// PDF metadata', data.metadata); 
    // check https://mozilla.github.io/pdf.js/getting_started/
    console.log('// PDF.js version', data.version);
    console.log('// PDF text', data.text);
}


/* global require, process, module */
if (require.main === module) {
    main(process.argv, {
        readFile: require('fs').readFile,
        join: require('path').join,
    })
        .then((it) => { console.log(it); })
        .catch((oops) => { console.error(oops); });
}
