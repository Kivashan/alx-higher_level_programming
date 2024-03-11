#!/usr/bin/node

const argv = process.argv;
let num;

if (!argv[2] || isNaN(Number(argv[2]))) {
  num = 1;
} else {
  num = Number(argv[2]);
}

function factorial (a) {
  if (a === 1 || a === 0) {
    return 1;
  }

  return a * factorial(a - 1);
}

console.log(factorial(num));
