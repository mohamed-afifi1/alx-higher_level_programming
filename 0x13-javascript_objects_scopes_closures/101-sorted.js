#!/usr/bin/node

const dic = require('./101-data.js').dict;
const data = {};
for (const key in dic) {
  data[dic[key]] = [];
}

for (const key in dic) {
  data[dic[key]].push(key);
}
console.log(data);
