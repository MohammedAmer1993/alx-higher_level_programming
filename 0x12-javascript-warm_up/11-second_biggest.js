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
  while (process.argv[i + 3]) {
    if (x < process.argv[i + 3]) {
      x = process.argv[i + 3];
    } else if (y < process.argv[i + 3]) {
      y = process.argv[i + 3];
    }
    i++;
  }
  console.log(y);
}
