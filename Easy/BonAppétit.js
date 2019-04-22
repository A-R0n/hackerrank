// Two people are splitting a bill but one person, Anna, won't
// pay for anything she is allergic to if the other person
// orders it. 'k' represents the index of the item in 'bill'
// that Anna is allergic to, and 'b' represents how much she paid.

function bonAppetit(bill, k, b) {
    const reducer = (a, c) => a + c;
    const annasBill = bill.filter((elem, index) => index != k).reduce(reducer)/2;
    if (b == annasBill) {
        console.log('Bon Appetit');
    }
    else {
        console.log(b - annasBill);
    }
}