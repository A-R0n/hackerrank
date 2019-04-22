
// Given a list of integers, count and output the number of
// times each value appears as a list of space-separated integers.
function countingSort(arr) {
    var sorter = [];
    for (let i = 0; i < 100; i++){
        sorter[i] = 0;
    }
    for (let j = 0; j < arr.length; j++) {
        sorter[arr[j]] += 1;
    }
    return sorter;
}
//  Returns an array of integers where each value is the number of
//  occurrences of the element's index value in the original array.