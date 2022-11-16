#!/usr/bin/node
// Read file

const fs = require('fs');

fs.readFile(process.argv[2], 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
    return;
  }

  console.log(data);
});
