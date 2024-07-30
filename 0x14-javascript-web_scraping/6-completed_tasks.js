#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  const completed = {};
  const tasks = JSON.parse(body);
  for (const task in tasks) {
    if (tasks[task].completed === true) {
      if (completed[tasks[task].userId] === undefined) {
        completed[tasks[task].userId] = 1;
      } else {
        completed[tasks[task].userId]++;
      }
    }
  }
  console.log(completed);
});
