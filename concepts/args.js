function args(array) {
  for (let value of array) {
    console.log(value);
  }
}

args([]);

function sum(array) {
  let ans = 0;
  for (let value of array) {
    ans = ans + value;
  }

  console.log(ans);
  return ans;
}

sum([10, 20, 30]);