class Solution(object):
    def sumAndMultiply(self, s, queries):
        MOD = 10 ** 9 + 7
        n = len(s)

        pow10 = [1] * (n + 1)
        for i in xrange(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        digit_sum = [0] * (n + 1)
        non_zero_cnt = [0] * (n + 1)
        prefix_num = [0] * (n + 1)

        for i in xrange(1, n + 1):
            d = ord(s[i - 1]) - ord('0')

            digit_sum[i] = digit_sum[i - 1] + d
            non_zero_cnt[i] = non_zero_cnt[i - 1]

            if d == 0:
                prefix_num[i] = prefix_num[i - 1]
            else:
                non_zero_cnt[i] += 1
                prefix_num[i] = (prefix_num[i - 1] * 10 + d) % MOD

        ans = []

        for l, r in queries:
            cnt = non_zero_cnt[r + 1] - non_zero_cnt[l]
            sm = digit_sum[r + 1] - digit_sum[l]

            x = (prefix_num[r + 1] -
                 prefix_num[l] * pow10[cnt]) % MOD

            ans.append((x * sm) % MOD)

        return ans