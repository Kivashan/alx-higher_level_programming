#!/usr/bin/node

const argv = process.argv;

function add (a, b) {
  return (Number(a) + Number(b));
}

console.log(add(argv[2], argv[3]));
