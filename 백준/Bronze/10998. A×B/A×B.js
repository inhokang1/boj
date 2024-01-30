const fs = require('fs');
const inputData = fs.readFileSync('/dev/stdin').toString().split(' ');

const A = inputData[0];
const B = inputData[1];
// Number(inputData[i]);
// 이런 식으로 타입을 string에서 number로 변환 후 계산해도 됨.

console.log(A*B);