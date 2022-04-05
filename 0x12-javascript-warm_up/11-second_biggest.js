#!/usr/bin/node
/*
 * script searches second biggest int
 * in list of args;
 * If no arg "0"
 * If 1 arg "0"
 * Else < 2 "output"
 */

const data = process.argv.slice(2).map(Number);
const result = data.sort((a, b) => b - a);
if (process.argv.length < 4) {
  console.log('0');
} else {
  console.log(result[1]);
}
