#!/usr/bin/node
function helpRequest (arr, i) {
    if (i === arr.length) {
      return;
    }
    request(arr[i], function (error, response, body) {
      if (error) {
        console.error(error);
      }
      console.log(JSON.parse(body).name);
      helpRequest(arr, i + 1);
    });
  }
  
  request('https://swapi-api.hbtn.io/api/films' + process.argv[2], function (error, response, body) {
    if (error) {
      console.error(error);
    }
    const charac = JSON.parse(body).characters;
    helpRequest(charac, 0);
  });
/*
const request = require('request');
const film = process.argv[2];
let url = 'https://swapi-api.hbtn.io/api/films';
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
      console.log('An error occured. Status code: ' + response.statusCode);
    }
  });
}
moviecharacters(film, url);
*/