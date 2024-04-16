#!/usr/bin/node

// Import Square class
const ImportedSquare = require('./5-square');

class Square extends ImportedSquare {
  charPrint (c) {
    // Prints the rectangle using the character c
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.width; i++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}

module.exports = Square;
