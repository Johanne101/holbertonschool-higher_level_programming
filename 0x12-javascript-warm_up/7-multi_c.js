#!/usr/bin/node


let x = parseInt(process.argv[2]);

if (isNaN(x)) {
	console.log('Missing number of occurrences');
} else {
	for (; x > 0; x--) {
		console.log('C is fun');
	}
}
