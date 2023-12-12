#!/usr/bin/node

const args = process.argv;

const str = 'My number: ';
const notNum = 'Not a number';

if (!args[2]) {
  console.log(notNum);
} else if (isNaN(args[2])) {
  console.log(notNum);
} else {
  const num = parseInt(args[2]);
  console.log(str + num);
}
