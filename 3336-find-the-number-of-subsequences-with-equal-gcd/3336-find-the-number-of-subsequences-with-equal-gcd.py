from functools import cache
from math import gcd

MOD = 10**9 + 7


class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:

        n = len(nums)

        @cache
        def dfs(i, g1, g2):
            if i == n:
                return 1 if g1 == g2 and g1 != 0 else 0


            ans = dfs(i + 1, g1, g2)


            ng1 = nums[i] if g1 == 0 else gcd(g1, nums[i])
            ans += dfs(i + 1, ng1, g2)

            ng2 = nums[i] if g2 == 0 else gcd(g2, nums[i])
            ans += dfs(i + 1, g1, ng2)

            return ans % MOD

        return dfs(0, 0, 0)
        