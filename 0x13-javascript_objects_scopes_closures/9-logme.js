#!/usr/bin/node

let argPrinted = 0;

exports.logMe = function count (item) {
  console.log(argprinted + ': ' + item);
  argPrinted++;
};
