'use strict';

function sumOfSquares(array){
    let sum = 0
    for (let number of array){
        sum += number ** 2
    }
    return sum
}

function squareOfSum(array){
    let sum = 0
    for (let number of array){
        sum += number
    }
    return (sum ** 2)
}

function range(size, startAt = 0) {
    return [...Array(size).keys()].map(i => i + startAt);
}

let ls = range(101)

let result = squareOfSum(ls) - sumOfSquares(ls)
console.log(result)

