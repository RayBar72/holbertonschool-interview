#!/usr/bin/node
/* Script that prints all character of Starwars movie
*/
const request = require('request');
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}/`;
request(url, async function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const characters = JSON.parse(body).characters;
    for (const c in characters) {
      const res = await new Promise((resolve, reject) => {
        request(characters[c], (error, res, html) => {
          if (error) {
            reject(error);
          } else {
            resolve(JSON.parse(html).name);
          }
        });
      });
      console.log(res);
    }
  }
});
