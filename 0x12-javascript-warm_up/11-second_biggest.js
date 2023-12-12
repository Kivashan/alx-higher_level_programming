#!/usr/bin/node

const args = process.argv;

let secondLargestNum;
let largestNum;
const arraySize = args.length;

if (arraySize === 2 || arraySize === 3) {
  console.log(0);
} else {
  largestNum = args[2];

  for (let x = 3; x < arraySize; x++) {
    if (args[x] >= largestNum) {
      secondLargestNum = largestNum;
      largestNum = args[x];
    } else if (args[x] > secondLargestNum) {
      secondLargestNum = args[x];
    }
  }
  console.log(secondLargestNum);
}
