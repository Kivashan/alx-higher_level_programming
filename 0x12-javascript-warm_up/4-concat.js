#!/usr/bin/node

const { argv } = require('process');

let a;
let b;

if (!argv[2]) {
  a = b = 'undefined';
} else if (!argv[3]) {
  a = argv[2];
  b = 'undefined';
} else {
  a = argv[2];
  b = argv[3];
}

console.log(`${a} is ${b}`);
