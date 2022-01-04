#!/usr/bin/node
/*
 * Script returns value msg of 1st arg:
 * If no args print: “No argument”
 * Otherwise, return: Argument value
 */
if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
