
const maxSubArray = (arr) => {

let maxSum = -1234567890, temp = 0;
for(let i = 0; i < arr.length - 1; i++) {
  temp = arr[i];
  for(let j = i + 1; j < arr.length; j++) {
    temp += arr[j];
    maxSum = (temp > maxSum) ? temp : maxSum;
    console.log(`Array form ${i}...${j}, temp: ${temp}, maxSum: ${maxSum}`);
  }
}
console.log(`Maximum sum: ${maxSum}`);
};

const generateArray = (arr) => {
let changeArr = [];
changeArr.push(0);
for(let i = 1; i < arr.length; i++) {
  changeArr.push(arr[i] - arr[i - 1]);
}

return changeArr;
};

const arr = generateArray([100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]);

maxSubArray(arr);