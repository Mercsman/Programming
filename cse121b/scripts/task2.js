/* Lesson 2 */

/* VARIABLES */

// Step 1: declare and instantiate a variable to hold your name
const NAME = 'Seth Bowles';

// Step 2: place the value of the name variable into the HTML file (hint: document.querySelector())
document.querySelector('#name').textContent = NAME;

// Step 3: declare and instantiate a variable to hold the current year
const YEAR = '2022';

// Step 4: place the value of the current year variable into the HTML file
document.querySelector('#year').textContent = YEAR;

// Step 5: declare and instantiate a variable to hold the name of your picture
const IMG = 'images/mywifeandI.png';

// Step 6: copy your image into the "images" folder
document.querySelector('img').src = IMG;
// Step 7: place the value of the picture variable into the HTML file (hint: document.querySelector().setAttribute())




/* ARRAYS */

// Step 1: declare and instantiate an array variable to hold your favorite foods
let FOODS = ['steak', ' lomo saltado', ' chicken alfredo', ' cafe rio']

// Step 2: place the values of the favorite foods variable into the HTML file
document.querySelector('#food').textContent = FOODS;

// Step 3: declare and instantiate a variable to hold another favorite food
const BONUS = 'pizza'

// Step 4: add the variable holding another favorite food to the favorite food array
FOODS.push(BONUS)

// Step 5: repeat Step 2

document.querySelector('#food').textContent = FOODS;
// Step 6: remove the first element in the favorite foods array
FOODS.shift()

// Step 7: repeat Step 2
document.querySelector('#food').textContent = FOODS;

// Step 8: remove the last element in the favorite foods array
FOODS.pop()

// Step 7: repeat Step 2
document.querySelector('#food').textContent = FOODS;


