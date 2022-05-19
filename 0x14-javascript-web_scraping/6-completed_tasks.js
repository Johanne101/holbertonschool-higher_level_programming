#!/usr/bin/node
// Script that computes the number of tasks completed by user id
const request = require('request');
const urlReq = process.argv[2];
let taskdata = '';
const completedTask = {};

request(urlReq, function (error, stat, data) {
  if (error) {
    console.log(error);
  } else {
    taskdata = JSON.parse(data);
    for (let i = 0; i < taskdata.length; i++) {
      if (taskdata[i].completed === true) {
        if (isNaN(completedTask[taskdata[i].userID])) {
          completedTask[taskdata[i].userID] = 0;
        }
        completedTask[taskdata[i].userID] += 1;
      }
    }
  }
  console.log(completedTask);
});
