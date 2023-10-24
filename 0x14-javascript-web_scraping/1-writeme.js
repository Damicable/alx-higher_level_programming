#!/usr/bin/node
const fs = require('fs');
fs.writeFile(process.argv[2], proces.arg[3], error => {
  if (error) console.log(error);
});
