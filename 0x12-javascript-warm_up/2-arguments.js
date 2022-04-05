#!/usr/bin/node

/*
 * Script returns process.argv msg:
 * If no args: “No argument”
 * Else If only 1 arg: “Argument found”
 * Otherwise: “Arguments found”
 */
if (process.argv.length === 3) {
  console.log('Argument found');
} else if (process.argv.length < 3) {
  console.log('No argument');
} else console.log('Arguments found');
