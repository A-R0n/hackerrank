// Determine the minimum number of elements in an array to delete
// so that all remaining elements are equal.
function equalizeArray(arr) {
    return arr.length - Math.max(...Object.values(arr.reduce((key, val) => {
        key[val] = key[val] ? ++key[val] : 1;
        return key;
    }, {})));
}
// Each element in the array represents a key.
// If that key already exists in subsequent iterations,
// it is incremented by 1.