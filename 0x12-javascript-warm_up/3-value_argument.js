#!/usr/bin/node

const argv = process.argv;
let i = 0;
let len = 0;

while (argv[i]) {
  len++;
  i++;
}

if (len === 2) {
  console.log('No argument');
} else {
  console.log(argv[2]);
}
