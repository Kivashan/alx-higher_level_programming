#!/usr/bin/node

// Rectangle class update
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      return this;
    }
  }

  // method that prints the rectangle using x as a representation of 1 unit
  print () {
    for (let i = 0; i < this.height; i++) {
      let arr = '';
      for (let j = 0; j < this.width; j++) {
        arr = arr + 'X';
      }
      console.log(arr);
    }
  }

  // method that swaps the width value with the height value and vice versa
  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  // method that doubles the width and height value
  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
