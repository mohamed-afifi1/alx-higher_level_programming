#!/user/bin/node
const arr = require('./100-data.js').list;
console.log(arr);
for (let i = 0; i < arr.length; i++) {
  arr[i] = arr[i] * i;
}
console.log(arr);
