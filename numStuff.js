/*
Input:
'1-10', '1,3,4-6' , '1,2'

Output:
'1, 2, 3, 4, 5, 6, 7, 8, 9, 10', '1, 3, 4, 5, 6', '1, 2'
*/
console.log();

str = '1,3,4-6';
strArr = str.split(',');
console.log("string array after splitting:", strArr); // → [ '1', '3', '4-6' ]

output = []
strArr.forEach(numStr => {
    if (numStr.includes("-")) {
        numRange = numStr.split("-")
        console.log("string array after splitting hyphen:", numRange) // → [ '4', '6' ]
        for (let i = Number(numRange[0]); i < Number(numRange[1])+1; i++) {
            output.push(i)
        }
        console.log("current output after hypen loop:", output)
    } else {
        output.push(Number(numStr))
        console.log("current output after normal number", output)
    }
})
console.log("final output:", output) // → [ 1, 3, 4, 5, 6 ]

console.log();
