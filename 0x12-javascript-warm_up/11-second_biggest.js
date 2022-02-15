#!/usr/bin/node
const data = process.argv.slice(2).map(Number);
const result = data.sort((a, b) => b - a);
if (process.argv.length < 4) {
  console.log('0');
} else {
  console.log(result[1]);
}
