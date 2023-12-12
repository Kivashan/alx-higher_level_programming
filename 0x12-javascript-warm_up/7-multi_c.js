#!/usr/bin/node

const args = process.argv;

let noOfOccurrence;

if (!args[2] || isNaN(args[2])) {
  console.log('Missing number of occurrences');
} else if (parseInt(args[2]) > 0) {
  noOfOccurrence = parseInt(args[2]);

  for (let x = 0; x < noOfOccurrence; x++) {
    console.log('C is fun');
  }
}
