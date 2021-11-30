'use strict';


let number = 600851475143,
	i = 2

while (i * i < number){
	while (number % i == 0){
		number /= i} 
	i++}

console.log(number)
