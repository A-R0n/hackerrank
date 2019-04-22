// s represents a list with characters 'U' and 'D'
// that represent 1 unit of movement, up or down 
// and always right. Calculate the amount of vallies
// in the list. (A valley is negative y between two x's)
function countingValleys(n, s) {
    var vallies = 0;
    var level = 0;
    var splitted = s.split('');
    for (let i = 0; i < n; i++){
        if (splitted[i] === 'U') {
            level++;
            if (level === 0) {
                vallies++;
            }
        }
        else {
            level--;
        }
    }
    return vallies;
}