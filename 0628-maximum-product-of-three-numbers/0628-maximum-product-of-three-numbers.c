int maximumProduct(int* nums, int numsSize) {
    int max1 = -1001, max2 = -1001, max3 = -1001;
    int min1 = 1001, min2 = 1001;

    for (int i = 0; i < numsSize; i++) {
        int x = nums[i];

        // Track the three largest numbers
        if (x > max1) {
            max3 = max2;
            max2 = max1;
            max1 = x;
        } else if (x > max2) {
            max3 = max2;
            max2 = x;
        } else if (x > max3) {
            max3 = x;
        }

        // Track the two smallest numbers
        if (x < min1) {
            min2 = min1;
            min1 = x;
        } else if (x < min2) {
            min2 = x;
        }
    }

    int product1 = max1 * max2 * max3;
    int product2 = min1 * min2 * max1;

    return product1 > product2 ? product1 : product2;
}