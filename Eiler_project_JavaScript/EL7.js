function isSimple(num){
	let sqr_num = Math.round(num ** (1/2))
	for (let div = 2; div <= sqr_num; div++){
		if (num % div == 0) return false
	}
	return true
}

let arrayOfSimple = []

let i = 1
while (arrayOfSimple.length <= 10001){
	if (isSimple(i)) { arrayOfSimple.push(i) }
	i++
}

console.log(arrayOfSimple[10001])