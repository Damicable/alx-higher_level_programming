#!/usr/bin/node
const OldSquare = require('./5-square');
module.exports = class Square extends OldSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    const strCmp = c ?? 'X';
    let strPrt = '';
    for (let k = 0; k < this.width; k++) {
      strPrt += strCmp;
    }
    for (let l = 0; l < this.height; l++) {
      console.log(strPrt);
    }
  }
};
