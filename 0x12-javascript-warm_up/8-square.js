#!/usr/bin/node
const n = parseInt(process.argv[2]);
const sqr = 'X';
if (isNaN(n)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < n; i++) {
    console.log(sqr.repeat(n));
  }
}
