#!/usr/bin/node
// Script prints the addition of two integers

// Extract operands from script argument
const args = process.argv.slice(2);

// Parse arguments to integer
const num1 = parseInt(args[0]);
const num2 = parseInt(args[1]);

// Write addition function
function add (a, b) {
  return (a + b);
}

// Print result of addition
console.log(add(num1, num2));
