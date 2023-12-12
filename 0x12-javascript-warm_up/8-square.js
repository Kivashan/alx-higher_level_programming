#!/usr/bin/node

const args = process.argv;
let size;

if (!args[2] || isNaN(args[2])) {
  console.log('Missing size');
} else if (parseInt(args[2]) > 0) {
  size = parseInt(args[2]);

  for (let x = 0; x < size; x++) {
    let str = '';
    for (let y = 0; y < size; y++) {
      str += 'X';
    }
    console.log(str);
  }
}
