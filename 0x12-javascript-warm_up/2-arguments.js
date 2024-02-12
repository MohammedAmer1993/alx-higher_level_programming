#!/usr/bin/node

const { argv } = require('node:process');

if (argv[2] !== undefined && argv[3] !== undefined) {
  console.log('Arguments found');
} else if (argv[2] !== undefined) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
