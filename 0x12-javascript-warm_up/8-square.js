#!/usr/bin/node

const argv = process.argv;

if (!argv[2] || isNaN(Number(argv[2]))) {
  console.log('Missing size');
} else {
  const size = Math.floor(Number(argv[2]));
  for (let i = 0; i < size; i++) {
    let str = '';
    for (let j = 0; j < size; j++) {
      str += 'X';
    }
    console.log(str);
  }
}
