#!/usr/bin/node
// Writes a string to a file
const fs = require('fs');
// The first argument is the file path
const filepath = process.argv[2];
// The second argument is the string to write
const data = process.argv[3];
// Use fs.writeFile() method to write the file
fs.writeFile(filepath, data, 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  }
});
