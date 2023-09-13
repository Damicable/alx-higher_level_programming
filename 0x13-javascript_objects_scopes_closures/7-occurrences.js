#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let TimesOccure = 0;
  let i = 0;

  for (; i < list.length; i++) {
   if (list[i] === searchElement) { TimesOccure++; }
  }

  return TimesOcccure;
};
