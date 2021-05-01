function pizzaOven(crustType, sauceType, cheeses, toppings) {
    var pizza = {};
    arr = [s1, s2, s3, s4]
    pizza.crustType = crustType;
    pizza.sauceType = sauceType;
    pizza.cheeses = cheeses;
    pizza.toppings = toppings;
    return pizza;
}
    
var s1 = pizzaOven("deep dish", "traditional", ["mozzarella"], ["pepperoni", "sausage"]);
var s2 = pizzaOven("hand tossed", "marinara", ["mozzarella", "feta"], ["mushrooms", "olives", "onions"]);
var s3 = pizzaOven(["half hand tosses, half thin crust"], "traditional", ["mozzarella"], ["pepperoni", "olives"]);
var s4 = pizzaOven("hand tossed", "traditional", ["mozzarella"], ["pineapple", "olives"]);
var randompizza = Math.floor(Math.random() * 4);
arr = [s1, s2, s3, s4] // There must be an easier way than this. Maybe not....... Probably.....
console.log(arr[randompizza])