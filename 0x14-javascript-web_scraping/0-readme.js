#!/usr/bin/node
const fs = require('fs');
const path = process.argv[2];
const read = fs.readFileSync(path, 'utf8');
console.log(read);
