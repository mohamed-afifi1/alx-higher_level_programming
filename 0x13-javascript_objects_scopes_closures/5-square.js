#!/usr/bin/node
module.exports = class Square extends require('./4-rectangle.js') {
  constructor (sideLength) {
    super(sideLength, sideLength);
  }
};
