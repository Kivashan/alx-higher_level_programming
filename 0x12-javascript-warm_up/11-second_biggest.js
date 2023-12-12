#!/usr/bin/node

const args = process.argv;

let secondLargestNum;
let largestNum;
const arraySize = args.length;

if (arraySize < 4) {
  console.log(0);
} else {
  largestNum = args[2];

  for (let x = 3; x < arraySize; x++) {
    if (args[x] > largestNum) {
      secondLargestNum = largestNum;
      largestNum = args[x];
    } else if (!secondLargestNum || args[x] > secondLargestNum) {
      if (args[x] < largestNum) {
        secondLargestNum = args[x];
      }
    }
  }
  if (!secondLargestNum) {
    secondLargestNum = 0;
  }
  console.log(secondLargestNum);
}
