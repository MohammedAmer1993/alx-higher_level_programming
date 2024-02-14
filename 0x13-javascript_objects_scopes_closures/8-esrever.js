#!/usr/bin/node

exports.esrever = function (list) {
  let j = list.length - 1;
  let i = 0;
  let tmp;
  while (i < j) {
    tmp = list[i];
    list[i] = list[j];
    list[j] = tmp;
    i++;
    j--;
  }
  return list;
};
