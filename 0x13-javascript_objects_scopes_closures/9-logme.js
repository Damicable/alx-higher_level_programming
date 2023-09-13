#!/usr/bin/node

let ArgPrinted = 0;

exports.logMe = function count (item) {
  console.log(Argprinted + ': ' + item);
  ArgPrinted++;
};
