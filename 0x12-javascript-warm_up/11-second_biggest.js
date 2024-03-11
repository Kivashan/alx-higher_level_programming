#!/usr/bin/node

const argv = process.argv;

let largest;
let secondLargest;
let index = 3;

if (!argv[2] || !argv[3]) {
  console.log(0);
} else {
  largest = parseInt(argv[2]);
  secondLargest = parseInt(argv[3]);

  while (argv[index]) {
    if (parseInt(argv[index]) > largest) {
      const temp = largest;
      largest = parseInt(argv[index]);
      secondLargest = temp;
    } else if (parseInt(argv[index]) > secondLargest) {
      secondLargest = argv[index];
    }
    index++;
  }
  console.log(secondLargest);
}
