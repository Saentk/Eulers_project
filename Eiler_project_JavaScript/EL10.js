
function isPrime(num){
	let sqr_num = Math.ceil(num ** (1/2))

	for (let di = 2; di <= sqr_num; di++){
		if (num % di == 0) { return false } 
	} return true
}

let sum = 2
for (let num = 3; num < 2e6; num += 2) {
	if (isPrime(num)) { 
		sum += num
	}
}

console.log(sum)


