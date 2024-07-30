#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  let count = 0;
  const movies = JSON.parse(body).results;
  for (const movie in movies) {
    const characters = movies[movie].characters;
    for (const character in characters) {
      if (characters[character].includes('18')) {
        count++;
      }
    }
  }
  console.log(count);
});
