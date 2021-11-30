'use strict';


let listOfMultiples = []
function multiples_of_3_or_5(num){
    for (let i = 3; i < num; i++){
        if ((i % 3 == 0) || (i % 5 == 0)){
            listOfMultiples.push(i)
        }
    }
}

multiples_of_3_or_5(1000)

console.log(
  listOfMultiples.reduce((a, b) => a + b, 0)
)