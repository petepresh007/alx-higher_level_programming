#!/usr/bin/node
const userId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${userId}`;
const request = require('request');
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  console.log(data.title);
});
