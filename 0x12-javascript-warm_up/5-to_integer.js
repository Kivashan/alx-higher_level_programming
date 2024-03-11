#!/usr/bin/node

const argv = process.argv;
let num = 0;

if (!argv[2]) {
  console.log('Not a number');
} else {
  num = Number(argv[2]);
  if (isNaN(num)) {
    console.log('Not a number');
  } else {
    console.log(Math.floor(num));
  }
}
