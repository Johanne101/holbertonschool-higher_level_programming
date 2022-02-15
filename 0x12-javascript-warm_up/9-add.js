#!/usr/bin/node
add(process.argv[2], process.argv[3]);
function add (a, b) {
  console.log(parseInt(a) + parseInt(b));
}
