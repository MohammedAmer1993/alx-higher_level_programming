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
      block = block + 'x';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(block);
    }
  }

  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}
module.exports = Rectangle;
