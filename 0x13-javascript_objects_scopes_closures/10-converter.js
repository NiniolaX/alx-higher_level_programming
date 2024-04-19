#!/usr/bin/node
// Converts a number in base 10 to another base passed as an argument
exports.converter = function (base) {
  /* Converts a base 10 number to a number in a given base
  * Return: A function that converts a number passed as argument to 'base'
  */
  return function baseConverter (number) {
    return number.toString(base);
  };
};
