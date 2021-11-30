'use strict';

function smallestFactor(arg) {
	let num = arg
	while (true) {
		for (let i = arg; i > 0; i--){
			if (num % i != 0) break 
			else if (i == 1) return num
		}
		num += arg
	}
}

console.log(smallestFactor(20))
