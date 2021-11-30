function is_polindrome(num){
	let str = '' + num;
	let reverse_str = str.split("").reverse().join("");
	if (str == reverse_str) return true
	else return false
}

let max = 0
for (let i = 999; i > 101; i--) {
	for (let j = 999; j > 101; j--) {
		let result = i * j
		if ((is_polindrome(result)) && (max < result)) {
			max = result
		}
	}
}

console.log(max)
