#!/usr/bin/node
// Converts a number in base 10 to another base passed as an argument
exports.converter = function (base) {
  /* Converts a base 10 number to a number in a given base
   * Return: A function that converts a number passed as argument to 'base'
   */
  function baseConverter (number) {
    // Converts a number (n) to base 'base'
    const result = [];
    // Return number if base equals 10
    if (base === 10) {
      return number.toString();
    }
    // Use successive division to convert bases less than or greater than 10
    while (number > 0) {
      result.push(Math.floor(number % base));
      number = Math.floor(number / base);
    }
    // Replace digits greater than 10 with corresponding letter
    const letters = 'abcdefghijklmnopqrstuvwxyz';
    return result.reverse().map(d => d >= 10 ? letters[d - 10] : d).join('');
  }
  return baseConverter;
};
