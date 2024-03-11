#!/usr/bin/node

const argv = process.argv;
const str = 'C is fun';

if (!argv[2] || isNaN(Number(argv[2]))) {
  console.log('Missing number of occurrences');
} else {
  const occurences = Math.floor(Number(argv[2]));
  for (let i = 0; i < occurences; i++) {
    console.log(str);
  }
}
