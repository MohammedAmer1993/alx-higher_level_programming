#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w !== undefined && w > 0 && h !== undefined && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let block = '';
    for (let i = 0; i < this.width; i++) {
      block = block + 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(block);
    }
  }
}
module.exports = Rectangle;
