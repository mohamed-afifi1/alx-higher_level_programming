#!/usr/bin/node
exports.esrever = function (list) {
  let result = [];
  for (let i = 0; i < list.length; i++) {
    result[i] = list[list.length - 1 - i];
  }
  return result;
};
