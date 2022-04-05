#!/usr/bin/node

/*
 * Script prints 1st arg passed:
 * If no args print: “No argument”
 * Otherwise, return: Argument value
 */
if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
