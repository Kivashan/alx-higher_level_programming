#!/usr/bin/node

const args = process.argv;

// addition function
function add (a, b) {
  const result = a + b;
  return result;
}

// validity check before calling function and displaying result
if (!args[2] || !args[3]) {
  console.log('NaN');
} else if (isNaN(args[2]) || isNaN(args[3])) {
  console.log('NaN');
} else {
  const num1 = parseInt(args[2]);
  const num2 = parseInt(args[3]);
  console.log(add(num1, num2));
}
