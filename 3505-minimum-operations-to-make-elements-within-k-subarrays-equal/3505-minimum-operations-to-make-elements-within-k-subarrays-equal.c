#include <stdlib.h>
#include <limits.h>

#define INF (LLONG_MAX / 4)

int cmp(const void *a, const void *b) {
    return (*(int *)a > *(int *)b) - (*(int *)a < *(int *)b);
}

void update(long long *bit, int n, int idx, long long val) {
    while (idx <= n) {
        bit[idx] += val;
        idx += idx & -idx;
    }
}

long long query(long long *bit, int idx) {
    long long sum = 0;
    while (idx > 0) {
        sum += bit[idx];
        idx -= idx & -idx;
    }
    return sum;
}

int kth(long long *bit, int n, int k) {
    int idx = 0;

    for (int step = 1 << 17; step > 0; step >>= 1) {
        int next = idx + step;
        if (next <= n && bit[next] < k) {
            idx = next;
            k -= bit[next];
        }
    }
    return idx + 1;
}

long long minOperations(int* nums, int numsSize, int x, int k) {
    int n = numsSize;

    int *sorted = malloc(n * sizeof(int));
    int *rank = malloc(n * sizeof(int));

    for (int i = 0; i < n; i++)
        sorted[i] = nums[i];

    qsort(sorted, n, sizeof(int), cmp);

    int m = 0;
    for (int i = 0; i < n; i++) {
        if (i == 0 || sorted[i] != sorted[i - 1])
            sorted[m++] = sorted[i];
    }

    for (int i = 0; i < n; i++) {
        int l = 0, r = m - 1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (sorted[mid] == nums[i]) {
                rank[i] = mid + 1;
                break;
            }
            if (sorted[mid] < nums[i]) l = mid + 1;
            else r = mid - 1;
        }
    }

    long long *cnt = calloc(m + 1, sizeof(long long));
    long long *sum = calloc(m + 1, sizeof(long long));
    long long *cost = malloc((n + 1) * sizeof(long long));

    for (int i = 0; i <= n; i++)
        cost[i] = 0;

    // Calculate cost of every window of size x
    for (int i = 0; i < n; i++) {
        update(cnt, m, rank[i], 1);
        update(sum, m, rank[i], nums[i]);

        if (i >= x) {
            update(cnt, m, rank[i - x], -1);
            update(sum, m, rank[i - x], -nums[i - x]);
        }

        if (i >= x - 1) {
            int medIdx = kth(cnt, m, (x + 1) / 2);
            long long median = sorted[medIdx - 1];

            long long leftCount = query(cnt, medIdx);
            long long leftSum = query(sum, medIdx);

            long long totalSum = query(sum, m);
            long long rightCount = x - leftCount;
            long long rightSum = totalSum - leftSum;

            cost[i + 1] =
                median * leftCount - leftSum +
                rightSum - median * rightCount;
        }
    }

    // Dynamic Programming
    long long *prev = malloc((n + 1) * sizeof(long long));
    long long *curr = malloc((n + 1) * sizeof(long long));

    for (int i = 0; i <= n; i++)
        prev[i] = 0;

    for (int j = 1; j <= k; j++) {
        for (int i = 0; i <= n; i++)
            curr[i] = INF;

        for (int i = 1; i <= n; i++) {
            curr[i] = curr[i - 1];

            if (i >= x && prev[i - x] != INF) {
                long long take = prev[i - x] + cost[i];

                if (take < curr[i])
                    curr[i] = take;
            }
        }

        long long *temp = prev;
        prev = curr;
        curr = temp;
    }

    long long ans = prev[n];

    free(sorted);
    free(rank);
    free(cnt);
    free(sum);
    free(cost);
    free(prev);
    free(curr);

    return ans;
}