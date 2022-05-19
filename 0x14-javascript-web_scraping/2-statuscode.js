#!/usr/bin/node
/* Display status code of a GET request */
const request = require('request');
const url = process.argv[2];
request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    console.log('code:' + res.statusCode);
  }
});
