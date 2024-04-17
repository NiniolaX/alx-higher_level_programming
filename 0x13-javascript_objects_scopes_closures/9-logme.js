#!/usr/bin/node
// Prints the number of arguments already printed and new argument value
let printCount = 0;
exports.logMe = function (item) {
  console.log(printCount + ': ' + item);
  printCount++;
};
