#!/usr/bin/node

const req = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
const episode = process.argv[2];
req.get(url + episode, function (err, res, body) {
  if (err) {
    console.error(err);
    return;
  }
  console.log(JSON.parse(body).title);
});
