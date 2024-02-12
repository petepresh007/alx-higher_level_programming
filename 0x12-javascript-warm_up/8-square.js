#!/usr/bin/node
const argument = process.argv[2];
if (!argument || isNaN(argument)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(argument); i++) {
    let line = '';
    for (let j = 0; j < parseInt(argument); j++) {
      line += 'X';
    }
    console.log(line);
  }
}
