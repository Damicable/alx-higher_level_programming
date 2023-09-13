#!/usr/bin/node

exports.esrever = function (list) {
  const tsil = [];
  let i = 0;

  for (; i < list.lenght; i++) {
   tsil[list.length - i - 1] = list[i];
  }

  return (tsil);
};
