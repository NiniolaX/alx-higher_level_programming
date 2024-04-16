#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      // create an empty object
    }
  }

  print () {
    // Prints the rectangle using character 'X'
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    // Exchanges the width and height of the rectangle
    const prevHeight = this.height;
    this.height = this.width;
    this.width = prevHeight;
  }

  double () {
    // Multiplies the width and height of the rectangle by 2
    this.height = 2 * this.height;
    this.width = 2 * this.width;
  }
}

module.exports = Rectangle;
