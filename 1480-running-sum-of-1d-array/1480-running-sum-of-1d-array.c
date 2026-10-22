/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* runningSum(int* nums, int numsSize, int* returnSize) {
    int* result = malloc(numsSize * sizeof(int));

    if (result == NULL) {
        *returnSize = 0;
        return NULL;
    }

    int sum = 0;

    for (int i =0; i < numsSize; i++){
        sum += nums[i];
        result[i] = sum;
    }
    
    *returnSize = numsSize;
    return result;
}