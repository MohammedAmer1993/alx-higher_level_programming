#!/usr/bin/node

const Sq = require('./5-square');

class Square extends Sq {
  charPrint (c) {
    let block = '';
    if (c !== undefined) {
      for (let i = 0; i < this.width; i++) {
        block = block + c;
      }
      for (let i = 0; i < this.height; i++) {
        console.log(block);
      }
    } else {
      for (let i = 0; i < this.width; i++) {
        block = block + 'X';
      }
      for (let i = 0; i < this.height; i++) {
        console.log(block);
      }
    }
  }
}
module.exports = Square;
