#!/usr/bin/node
// Script computes and prints a factorial.

// Extract number whose factorial is to be computed from script arguments
const args = process.argv.slice(2);
const num = parseInt(args[0]);

// Write function that computes the factorial of a number
function factorial (n) {
  if (isNaN(n)) {
    return (0);
  } else if (n === 0) {
    return (1);
  } else {
    return (n * factorial(n - 1));
  }
}

// Print factorial
console.log(factorial(num));
