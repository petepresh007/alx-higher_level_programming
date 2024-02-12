#!/usr/bin/node
const argument = process.argv[2];
if (!argument || isNaN(argument)) {
  console.log('Not a number');
} else {
  console.log(parseInt(argument));
}
