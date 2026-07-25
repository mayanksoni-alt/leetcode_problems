class Solution:
    def uniqueXorTriplets(self, nums):

        unique_nums = list(set(nums))


        s1 = set(unique_nums)


        s2 = set()
        for a in s1:
            for b in unique_nums:
                s2.add(a ^ b)


        s3 = set()
        for a in s2:
            for b in unique_nums:
                s3.add(a ^ b)

        return len(s3)


