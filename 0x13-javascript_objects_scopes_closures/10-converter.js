#!/usr/bin/node
// Function converts number to base 10
exports.converter = function (base) {
  function bConvert (n) {
    return n.toString(base);
  }
  return bConvert;
};
