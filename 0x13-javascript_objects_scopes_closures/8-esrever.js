#!/usr/bin/node
// Contains a function which reverses an array
exports.esrever = function (list) {
  const tempArray = list.slice();

  for (let i = 0; i < list.length; i++) {
    list[i] = tempArray[tempArray.length - 1 - i];
  }

  return (list);
};
