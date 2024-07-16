#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}

const r1 = new Rectangle(-5, 4);
console.log(r1.height);
console.log(r1.width);
