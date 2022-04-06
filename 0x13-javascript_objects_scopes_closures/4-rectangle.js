#!/usr/bin/node
// Rectangle class defines a rectangle
// Instance methods;
// `print`, `rotate`, & `double`
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let sqr = '';
      for (let j = 0; j < this.width; j++) {
        sqr += 'X';
      }
      console.log(sqr);
    }
  }

  rotate () {
    const tmp = this.height;
    this.height = this.width;
    this.width = tmp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
