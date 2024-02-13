#!/usr/bin/node

if (process.argv[2] === undefined || process.argv[3] === undefined) {
  console.log('NaN');
} else {
  console.log(process.argv[3]);
}
