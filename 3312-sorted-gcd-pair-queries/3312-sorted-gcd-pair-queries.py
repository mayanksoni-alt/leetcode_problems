from bisect import bisect_right

class Solution(object):
    def gcdValues(self, nums, queries):
        mx = max(nums)


        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1


        cnt = [0] * (mx + 1)
        for d in range(1, mx + 1):
            for multiple in range(d, mx + 1, d):
                cnt[d] += freq[multiple]


        exact = [0] * (mx + 1)
        for d in range(mx, 0, -1):
            c = cnt[d]
            pairs = c * (c - 1) // 2
            m = 2 * d
            while m <= mx:
                pairs -= exact[m]
                m += d
            exact[d] = pairs


        prefix = []
        total = 0
        for g in range(1, mx + 1):
            total += exact[g]
            prefix.append(total)

        ans = []
        for q in queries:
            ans.append(bisect_right(prefix, q)+1)

        return ans