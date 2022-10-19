#!/usr/bin/node

const request = require('request');
const film = process.argv[2];
let url = 'https://swapi-api.hbtn.io/api/people';
function moviecharacters (film, url) {
  request(url, function (err, response, body) {
    if (err) {
      console.log(err);
    } else if (response.statusCode === 200) {
      let jsonobj = JSON.parse(body);
      let characters = jsonobj.results;
      for (let i in characters) {
        for (let j in characters[i].films) {
          if (characters[i].films[j].includes(film)) {
            console.log(characters[i].name);
          }
        }
      }
      if (jsonobj.next !== null) {
        moviecharacters(film, jsonobj.next);
      }
    } else {
      console.log('Error. Status code: ' + response.statusCode);
    }
  });
}
moviecharacters(film, url);
