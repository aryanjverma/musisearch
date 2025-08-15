const fruits = [
    {
        name: "Apple",
        color: "Red",
        weight: 150
    },
    {
        name: "Banana",
        color: "Yellow",
        weight: 120
    },
    {
        name: "Cherry",
        color: "Red",
        weight: 10
    }
];
console.log(fruits);
const maxFruitWeight = fruits.reduce((max, fruit) => {
    return Math.max(max, fruit.weight);
}, 0);
console.log(`Max fruit weight: ${maxFruitWeight}`);