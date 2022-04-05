#!/usr/bin/node
/*
 * Script prints a square
 */

const nSize = parseInt(process.argv[2]);
const sqr = 'X';
if (isNaN(nSize)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < nSize; i++) {
    console.log(sqr.repeat(nSize));
  }
}
