#!/usr/bin/node

exports.esrever = function (list) {
  const RevList = [];
  let i = 0;

  for (; i < list.lenght; i++) {
   RevList[list.length - i - 1) = list[i];
  }

  return (RevList);
};
