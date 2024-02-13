#!/usr/bin/node
let x = process.argv[2];
let y = process.argv[3];
let tmp = 0;

if (x === undefined || y === undefined) {
  console.log('NaN');
} else {
  if (x < y) {
    tmp = x;
    x = y;
    y = tmp;
  }
  let i = 0;
  while (process.argv[i + 4]) {
    if (x < process.argv[i + 4]) {
      x = process.argv[i + 4];
    } else if (y < process.argv[i + 4]) {
      y = process.argv[i + 4];
    }
    i++;
  }
  console.log(y);
}
