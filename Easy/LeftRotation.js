// Perform d rotations on array a:
function rotLeft(a, d) {
    var end = a.splice(d, a.length);
    var beginning = a.slice(0, d);
    var flipped = end.concat(beginning);
    return flipped;
}
// Change the original array by splicing it at d
// Then concatenate the beginning of what is sliced
// on the end.
