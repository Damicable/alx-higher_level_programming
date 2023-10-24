#!/usr/bin/node
const fs = require('fs');
fs.readFile(process.arg[2], 'utf8', function (error, content) {
  console.log(error || content);
});
