#!/usr/bin/node
/*
 * Function increments & calls function
 */

exports.addMeMaybe = function (number, theFunction) {
  theFunction(number + 1);
};
