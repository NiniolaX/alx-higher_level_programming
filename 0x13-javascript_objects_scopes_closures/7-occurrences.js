#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  // Returns the number of occurences of an element in a list
  let nb = 0;

  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      nb++;
    }
  }

  return (nb);
};
