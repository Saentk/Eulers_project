'use strict';


function PythagoreanTriplet(a, b, c){
	if (a ** 2 + b ** 2 == c ** 2) { return true }
	return false
}

let number = 1000
for (let a = 1; a < number; a++){
	for (let b = a; b < (number / 2); b++){
		for (let c = b; c < (number / 2); c++){
			if ((PythagoreanTriplet(a, b, c)) && (a + b + c == 1000)){
				console.log((a * b *c), [a, b, c])
			}
		}
	}
}

