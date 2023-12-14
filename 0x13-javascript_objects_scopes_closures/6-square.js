#!/usr/bin/node

// Square class that inherits from rectangle class

module.exports = class Square extends require('./5-square') {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        let arr = '';
        for (let j = 0; j < this.width; j++) {
          arr = `${arr}${c}`;
        }
        console.log(arr);
      }
    }
  }
};
