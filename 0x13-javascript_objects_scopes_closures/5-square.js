#!/usr/bin/node
// Defined Square class
// Inherits from 4-rectangle.js
const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
