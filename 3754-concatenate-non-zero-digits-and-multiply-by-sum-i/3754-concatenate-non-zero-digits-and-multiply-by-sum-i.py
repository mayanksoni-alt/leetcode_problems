class Solution(object):
    def sumAndMultiply(self, n):
        s = str(n)

        num = []
        digit_sum = 0

        for ch in s:
            if ch != '0':
                num.append(ch)
                digit_sum += int(ch)

        if not num:
            return 0

        return int(''.join(num)) * digit_sum