#!/usr/bin/node
const fs = require('fs');
const path = process.argv[2];
const write = process.argv[3];
fs.writeFileSync(path, write);
