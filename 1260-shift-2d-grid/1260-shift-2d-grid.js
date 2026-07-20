/**
 * @param {number[][]} grid
 * @param {number} k
 * @return {number[][]}
 */
var shiftGrid = function(grid, k) {
    const m = grid.length;
    const n = grid[0].length;
    const total = m * n;

    let arr = [];
    for (let row of grid) {
        arr.push(...row);
    }

    k %= total;
    arr = arr.slice(total - k).concat(arr.slice(0, total - k));

    let ans = [];
    for (let i = 0; i < total; i += n) {
        ans.push(arr.slice(i, i + n));
    }

    return ans;
    
};