#!/usr/bin/node
// Function prints;
// Arguments and value
let iValue = 0;

exports.logMe = function (item) {
  console.log(iValue + ': ' + item);
  iValue++;
};
