#!/usr/bin/node
exports.converter = function (base) {
  return function (num) {
    if (num < base) {
      return num.toString();
    }
    return (num / base).converter(base) + (num % base).toString();
  }
}
