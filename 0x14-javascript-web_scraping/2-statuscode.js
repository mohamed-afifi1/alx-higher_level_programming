#!/usr/bin/node

const req = require('request');
const url = process.argv[2];

req.get(url, function (err, res) {
  if (err) {
    console.error(err);
    return;
  }
  console.log('code:', res.statusCode);
});
