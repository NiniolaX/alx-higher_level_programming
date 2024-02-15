#!/usr/bin/node
// Script searches the second largest integer in the list of arguments

// Write function that returns the second largest number in an array of numbers
function secondBiggest (arrayOfNumbers) {
  let num;
  let max = Number.MIN_VALUE;
  let max2;
  for (num of arrayOfNumbers) {
    if (num > max) {
      max2 = max;
      max = num;
    } else if (num > max2 && num !== max) {
      max2 = num;
    }
  }
  if (max2 === Number.MIN_VALUE) {
    return (0);
  } else {
    return (max2);
  }
}

// Find the second largest number in argument list
const args = process.argv.slice(2);
const numbers = args.map(Number); // Convert values in args to integers

if (args.length === 0) {
  console.log(0);
} else {
  console.log(secondBiggest(numbers));
}
