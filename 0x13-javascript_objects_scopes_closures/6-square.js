#!/usr/bin/node
const Quare = require('./5-square');
class Square extends Quare {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }

    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
