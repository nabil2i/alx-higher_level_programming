#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    let completed_dict = {};
    let tasks = JSON.parse(body);
    for (let i in tasks) {
      let task = tasks[i];
      if (task.completed === true) {
        if (completed_dict[task.userId] === undefined) {
          completed_dict[task.userId] = 1;
        } else {
          completed_dict[task.userId]++;
        }
      }
    }
    console.log(completed_dict);
  } else {
    console.log('Error. Status code: ' + response.statusCode);
  }
});
