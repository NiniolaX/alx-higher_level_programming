#!/usr/bin/node
exports.nbOccurrences = function (list, searchElement) {
  // Returns the number of occurences of an element in a list
  let nb = 0;
  for (i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      nb++;
    }
  }
  return (nb);
}
