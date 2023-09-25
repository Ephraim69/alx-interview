#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;

request(url, async (err, res, _body) => {
  if (err) {
    console.log(err);
    return;
  }

  const charactersArray = JSON.parse(res.body).characters;
  for (const character of charactersArray) {
    await new Promise((resolve, reject) => {
      request(character, (err, _res, body) => {
        if (err) {
          console.log(err);
          reject();
        }

        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
