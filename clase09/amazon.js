const isPrime = product => product.type === "prime";
const isNotPrime = product => product.type !== "prime";
const primeItems = cart => cart.filter(isPrime);
const notPrimeItems = cart => cart.filter(isNotPrime);

const TECH_DISCOUNT = 0.8;
const isTech = product => product.category === "tech";
const getPrice = product => product.price * (isTech(product) ? TECH_DISCOUNT : 1);
const getPrices = cart => cart.map(getPrice);
const getTotal = cart => getPrices(cart).reduce((total, price) => total + price, 0);


const cart = [
    {"name":"Biscuits", "type":"regular", "category":"food", "price": 2.0},
    {"name":"Monitor", "type":"prime", "category":"tech", "price": 119.99},
    {"name":"Mouse", "type":"prime", "category":"tech", "price": 25.50},
    {"name":"dress", "type":"regular", "category":"clothes", "price": 49.90},
  ];
// console.log(primeItems(cart));
// console.log(notPrimeItems(cart));
console.log(getTotal(cart));







// const TECH_DISCOUNT = 0.8;
// const isTech = product => product.category === "tech";
// const getPrice = product => product.price * (isTech(product) ? TECH_DISCOUNT : 1);
// const getPrices = cart => cart.map(getPrice);
