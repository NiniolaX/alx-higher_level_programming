#!/usr/bin/node
const args = process.argv.slice(2); // Since first two arguments are 'node' and file path
if (!args[0]) {
  console.log('No argument');
} else {
  console.log(args[0]);
}
