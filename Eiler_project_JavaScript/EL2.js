'use strict';

let fibonacciList = [0, 1]
function fibonacciNumbers(num){
while (true){
    let new_number = fibonacciList.slice(-1)[0] + fibonacciList.slice(-2)[0]
    if (new_number >= num) { break }
    fibonacciList.push(new_number)
    }
}

fibonacciNumbers(4000000)

let sum = 0
for (let x of fibonacciList){ 
    if (x % 2 == 0) {
        sum += x
    }
}
console.log(sum)

