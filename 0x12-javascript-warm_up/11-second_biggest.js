#!/usr/bin/node
let x = process.argv[2];
let y = process.argv[3];
let tmp = 0;

if (x === undefined || y === undefined) {
  console.log('NaN');
} else {
  let i = 0;
  while (process.argv[i + 3]) {
    if (x < process.argv[i + 3]) {
      tmp = x;
      x = process.argv[i + 3];
      if (tmp > y) {
        y = tmp;
      }
    }
    i++;
  }
  console.log(y);
}
