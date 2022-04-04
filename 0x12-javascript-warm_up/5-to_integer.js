#!/usr/bin/node

const numArg = Number(process.argv[2]);
if (isNaN(numArg)) {
	console.log('Not a number');
} else {
	console.log('My number: ' + Math.trunc(numArg));
}
