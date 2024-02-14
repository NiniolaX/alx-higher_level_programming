#!/usr/bin/node
// Script prints 'C is fun' x times, where x is the first argument of the script

// Extract number of times text should be printed from argument list
const args = process.argv.slice(2);
const x = parseInt(args[0]);
let i;
/* If first argument can't be converted to an integer, print error message
 * else, print text x times
 */
if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
