#!/usr/bin/node
const arr = require('./100-data.js').list;
console.log(arr);
const map = arr.map((x, i) => x * i);
console.log(map);
