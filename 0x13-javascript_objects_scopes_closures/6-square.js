#!/usr/bin/node
const OldSquare = require('./5-square');

class Square extends OldSquare {
  charPrint (c) {
    if (c === undefined) { this.print(); } else {
     for (let k = 0; k < this.height; k++) {
      console.log(c.repeat(this.width)):
     }
    }
  }
}

module.exports = Square;
