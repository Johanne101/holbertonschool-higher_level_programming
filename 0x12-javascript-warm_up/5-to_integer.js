#!/usr/bin/node
/*
 * Script prints a msg:
 * If arg can be converted,
 * else if can't e converted;
 * "Not a number" msg will print.
 */

const arg = Number(process.argv[2]);
if (isNaN(arg)) {
	console.log('Not a number');
} else {
	console.log('My number: ' + Math.trunc(arg));
}
