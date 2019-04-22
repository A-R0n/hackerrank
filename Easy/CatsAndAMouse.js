// Two cats and a mouse are at various positions on a line.
// You will be given their starting positions. 
// Your task is to determine which cat will reach the mouse first,
// assuming the mouse doesn't move and the cats travel at equal speed. 
// If the cats arrive at the same time,
// the mouse will be allowed to move and it will escape while they fight.
function catAndMouse(cat1, cat2, mouse) {
    if (Math.abs(mouse-cat1) == Math.abs(mouse-cat2)) {
        return 'Mouse';
    }
    else if (Math.abs(cat2 - mouse) > Math.abs(cat1 - mouse)) {
        return 'Cat 1';
    }
    else {
        return 'Cat 2';
    }
}