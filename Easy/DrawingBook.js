// What is the minimum number, n, of pages to flip in a book to
// page, p, if page 1 is always on the right side and you can
// only start at the beginning or end of the book?
function pageCount(n, p) {
    const pageTurnsFront = Math.floor(p / 2);
    const totalTurns = Math.floor(n / 2);
    return Math.min(pageTurnsFront, totalTurns - pageTurnsFront);
}