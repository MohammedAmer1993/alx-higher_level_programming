#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let i = 0;
  let counter = 0;
  while (list[i] !== undefined) {
    if (searchElement === list[i]) {
      counter++;
    }
    i++;
  }
  return counter;
};
