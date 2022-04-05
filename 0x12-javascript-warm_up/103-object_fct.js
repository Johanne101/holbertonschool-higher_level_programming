#!/usr/bin/node
/*
 * Script Update;
 * adds new function `incr`
 * which incriments an int `value`
 * var not allowed
 */

const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
myObject.incr = function () {
  myObject.value += 1;
};
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
