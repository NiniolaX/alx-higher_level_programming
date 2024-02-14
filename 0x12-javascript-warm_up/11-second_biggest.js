#!/usr/bin/node
// Script searches the second biggest integer in the list of arguments

// Extract arguments
const args = process.argv.slice(2);
let max = Number.MIN_VALUE;
let max2 = Number.MIN_VALUE;
let num;

// Write function that returns the second biggest number in a list
/*
 * Find the biggest element
 * Find the next biggest element
 * To find the biggest element
 * 1. Initialize a variable max to Number.MIN_VALUE
 * 2. Compare each element in array to max, if an element is greater than max, reassign it to max and continue search.
 * 3. Repeat process 1-2 to find second biggest number
 */
function secondBig (args) {
  // Obtain maximum number
  for (num of args) {
    if (parseInt(num) > max) {
      max = parseInt(num);
    }
  }
  // Obtain second maximum number
  for (num of args) {
    if (parseInt(num) > max2 && parseInt(num) < max) {
      max2 = parseInt(num);
    }
  }
  // Return second maximum number
  if (max2 === Number.MIN_VALUE) {
    return (0);
  } else {
    return (max2);
  }
}

// Print second biggest number
console.log(secondBig(args));
