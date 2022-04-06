#!/usr/bin/node
// Script imports a dict of ocurrences by,
// user ID, & computes a
// dictionary of user IDs by occurrences

const dict1 = require('./101-data.js').dict;
const dict2 = {};

for (const keyID in dict1) {
  if (dict2[dict1[keyID]] === undefined) {
    dict2[dict1[keyID]] = [];
  }
  dict2[dict1[keyID]].push(keyID);
}

console.log(dict2);
