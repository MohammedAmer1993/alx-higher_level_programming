#!/usr/bin/node
const myList = require('./100-data.js').list;
const newList = myList.map((num, ind) => num * ind);
console.log(myList);
console.log(newList);
