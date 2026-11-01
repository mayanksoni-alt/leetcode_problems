int minMoves(int* nums, int numsSize) {
    int min = nums[0];
    int moves = 0;

    for (int i = 1; i < numsSize; i++) {
        if (nums[i] < min) {
            moves += (min - nums[i]) * i;
            min = nums[i];
        } else {
            moves += nums[i] - min;
        }
    }

    return moves;
}