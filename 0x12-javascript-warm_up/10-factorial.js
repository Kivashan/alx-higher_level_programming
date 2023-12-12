#!/usr/bin/node

const args = process.argv;

// function to calculate the factorial of a given number
function factorial (num) {
  let result = 1;
  if (num > 1) {
    result = factorial(num - 1);
  }
  result = result * num;

  return result;
}

// check for user input before passing data to function
if (!args[2] || isNaN(args[2])) {
  console.log(1);
} else {
  console.log(factorial(parseInt(args[2])));
}
