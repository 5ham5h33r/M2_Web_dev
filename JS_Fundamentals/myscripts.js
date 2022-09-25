let x = 5;
let y = 6;
document.getElementById("x").innerHTML = x
document.getElementById("y").innerHTML = y

var numOne = 12, numTwo = 13, sum;
function add(numOne, numTwo) {
    sum = numOne + numTwo;
    document.getElementById("ans").innerHTML = sum;
}
add(numOne, numTwo);

let sum2 = (a, b) => a + b;
document.getElementById("ans2").innerHTML = sum2(numOne, numTwo)

// Compares two variables
if (numOne < numTwo) {
    document.getElementById("if1").innerHTML = "NumOne is less than numTwo";
}

if (numOne > numTwo) {
    document.getElementById("if_else").innerHTML = "False";
}
else {
    document.getElementById("if_else").innerHTML = "As numOne is not greater than numTwo, we move onto the else statement";
}

let text = "";

// Example of for loop, where counter is initialized and the condition along with the increment/decrement is specified at start of the loop
for (i = 0; i < 5; i++) {
    text += "The number is " + i + "<br>";
}

document.getElementById("for").innerHTML = text;

let text2 = "";
i = 5;
// Example of while loop, where condition is checked at the start of the loop
while (i > 0) {
    text2 += "The number is " + i + "<br>";
    i--;
}
document.getElementById("while").innerHTML = text2;

text3 = ""
// Example of do_while where loop is ran at least once after which the condition is checked.
do {
    text3 += "The number is " + i + "<br>";
    i++;
}
while (i < 10);

document.getElementById("do_while").innerHTML = text3;
