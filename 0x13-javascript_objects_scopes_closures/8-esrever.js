#!/usr/bin/node
// Function Reverses a list
exports.esrever = function (list) {
  const rvlst = [];
  for (let i = list.length - 1; i >= 0; i--) {
    rvlst.push(list[i]);
  }
  return rvlst;
};
