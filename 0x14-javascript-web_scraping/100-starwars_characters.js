#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  for (const i of data.characters) {
    request(i, function (error, response, body) {
      if (error) {
        console.log(error);
      }
      const bod = JSON.parse(body);
      console.log(bod.name);
    });
  }
});
