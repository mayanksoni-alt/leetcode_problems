
int uniquePaths(int** grid, int gridSize, int* gridColSize) {
    const int MOD = 1000000007;

    int m = gridSize;
    int n = gridColSize[0];

    if (m == 1 && n == 1)
        return 1;

    int size = m * n;

    int* right = (int*)malloc(size * sizeof(int));
    int* down = (int*)malloc(size * sizeof(int));

    long long* dp = (long long*)calloc(size, sizeof(long long));

    // Precompute destinations backwards
    for (int i = m - 1; i >= 0; i--) {
        for (int j = n - 1; j >= 0; j--) {

            int id = i * n + j;

            // Attempt to move right
            if (j + 1 >= n) {
                right[id] = -1;
            }
            else {
                int next = id + 1;

                if (next == size - 1 || grid[i][j + 1] == 0) {
                    right[id] = next;
                }
                else {
                    right[id] = down[next];
                }
            }

            // Attempt to move down
            if (i + 1 >= m) {
                down[id] = -1;
            }
            else {
                int next = id + n;

                if (next == size - 1 || grid[i + 1][j] == 0) {
                    down[id] = next;
                }
                else {
                    down[id] = right[next];
                }
            }
        }
    }

    // Dynamic programming
    dp[0] = 1;

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {

            int id = i * n + j;

            if (dp[id] == 0 || id == size - 1)
                continue;

            // Move right
            int r = right[id];

            if (r != -1) {
                dp[r] = (dp[r] + dp[id]) % MOD;
            }

            // Move down
            int d = down[id];

            if (d != -1) {
                dp[d] = (dp[d] + dp[id]) % MOD;
            }
        }
    }

    int answer = dp[size - 1];

    free(right);
    free(down);
    free(dp);

    return answer;
}
