#!/usr/bin/node
const value = process.argv[2];
if (isNaN(value)) {
  console.log(1);
} else {
  fac(parseInt(value));
}

function fac (n) {
  let factorial = 1;
  for (let i = 2; i <= n; i++) {
    factorial *= i;
  }
  console.log(factorial);
}
