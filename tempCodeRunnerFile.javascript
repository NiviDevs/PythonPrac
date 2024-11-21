const readline = require("readline")
const rl = readline.createInterface({
    input : process.stdin,
    output : process.stdout
})
let inp = rl.question("Enter number")
let n = parseInt(inp);


for (let index = 1; index <= n; index+=2) {
    console.log(" ".repeat((n - index) / 2) + "*".repeat(index) + " ".repeat((n - index) / 2));
    
}
