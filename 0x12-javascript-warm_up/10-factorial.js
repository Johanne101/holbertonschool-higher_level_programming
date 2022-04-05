#!/usr/bin/node
/*
 * Script computes & prints a factorial
 */

const n = parseInt(process.argv[2]);
function factorial (n) {
  if (n <= 1) {
    return (1);
  }
  return factorial(n - 1) * n;
}
if (isNaN(n)) {
  console.log(1);
} else {
  console.log(factorial(n));
}
