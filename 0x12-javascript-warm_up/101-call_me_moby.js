#!/usr/bin/node
/*
 * function executes x times a function
 */

exports.callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
