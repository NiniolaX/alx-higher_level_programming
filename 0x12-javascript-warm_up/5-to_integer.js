#!/usr/bin/node
// Extract arguments passed to script
const args = process.argv.slice(2);

// Convert first agrument to integer
const firstArg = parseInt(args[0]);

// Print result of conversion
if (isNaN(firstArg)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${firstArg}`);
}
