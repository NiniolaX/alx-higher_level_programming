#!/usr/bin/node
// Script prints 3 lines of text using an array of strings and a loop

// Put lines of text in an array
const array = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
let str;
// Print array using a loop
for (str of array) {
  console.log(str);
}
