// Calculate the percentage of elements
// that are positive, negative, and zero.
function plusMinus(arr) {
    var pos = 0;
    var neg = 0;
    var zero = 0;
    for (let i = 0; i < arr.length; i++){
        if (arr[i] < 0) {
            neg++;
        }
        else if (arr[i] === 0) {
            zero++;
        }
        else {
            pos++;
        }
    }
    var posNum = pos / arr.length;
    var negNum = neg / arr.length;
    var zeroNum = zero / arr.length;
    console.log(posNum.toFixed(6));
    console.log(negNum.toFixed(6));
    console.log(zeroNum.toFixed(6));
}