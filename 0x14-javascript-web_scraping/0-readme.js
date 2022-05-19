#!/usr/bin/node
// Script that reads and prints the content of a file
// // Include fs module
const fs = require('fs');

// Use fs.readFile() method to read the file
fs.readFile(process.argv[2], 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  // Display the file content
  console.log(data);
});
