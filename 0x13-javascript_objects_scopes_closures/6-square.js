#!/usr/bin/node
module.exports = class Square extends require('./5-square.js') {
  constructor (sideLength) {
    super(sideLength, sideLength);
  }

  charPrint (c) {
    for (let i = 0; i < this.width; i++) {
      console.log(c.repeat(this.width));
    }
  }
};
