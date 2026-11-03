int minMoves(int* nums, int numsSize) {
    int max = nums[0];
    int moves = 0;

    // Find the maximum element
    for (int i = 1; i < numsSize; i++) {
        if (nums[i] > max) {
            max = nums[i];
        }
    }

    // Calculate moves needed to make every element equal to max
    for (int i = 0; i < numsSize; i++) {
        moves += max - nums[i];
    }

    return moves;
}