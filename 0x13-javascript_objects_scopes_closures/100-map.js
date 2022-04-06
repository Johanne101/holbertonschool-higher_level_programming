#!/usr/bin/node
// Function imports & computes a new array
const array1 = require('./100-data').list;
// pass a function to map
const map1 = array1.map((x, idx) => x * idx);

console.log(array1);
console.log(map1);
