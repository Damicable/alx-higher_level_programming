#!/usr/bin/node
const swap = (list, one, two) => {
  const tmp = list[one];
  list[one] = list[two];
  list[two] = tmp;
};
exports.esrever = function (list) {
  let firstIdx = 0;
  let lastIdx = list.length - 1;
  const halfWay = Math.floor(list.length / 2);
  while (firstIdx < halfWay) {
    swap(list, firstIdx, lastIdx);
    firstIdx++;
    lastIdx--;
  }
  return list;
};
