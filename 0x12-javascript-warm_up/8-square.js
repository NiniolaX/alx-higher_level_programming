#!/usr/bin/node
// Script prints a square

// Extract square size from script arguments
const args = process.argv.slice(2);
const size = parseInt(args[0]);
let i;

// Check if valid square size was passed
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
// Print square
