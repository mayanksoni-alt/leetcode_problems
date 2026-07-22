import bisect

class Solution(object):
    def maxActiveSectionsAfterTrade(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(s)
        runs = []
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            runs.append((s[i], i, j - 1))
            i = j

        total_ones = s.count('1')

        ones_runs = []
        for idx, (c, st, en) in enumerate(runs):
            if c == '1':
                Zl = (runs[idx-1][2] - runs[idx-1][1] + 1) if idx-1 >= 0 else 0
                Zr = (runs[idx+1][2] - runs[idx+1][1] + 1) if idx+1 < len(runs) else 0
                Lz = st - Zl
                Rz = en + Zr
                ones_runs.append((st, en, Zl, Zr, Lz, Rz))

        m = len(ones_runs)
        Sarr = [x[0] for x in ones_runs]
        Earr = [x[1] for x in ones_runs]
        Lzarr = [x[4] for x in ones_runs]
        Rzarr = [x[5] for x in ones_runs]
        Karr  = [x[0] - x[1] for x in ones_runs]
        Garr  = [x[2] + x[3] for x in ones_runs]
        A2arr = [x[2] - x[1] for x in ones_runs]
        A3arr = [x[0] + x[3] for x in ones_runs]

        NEG = float('-inf')

        def build_sparse(arr):
            L = len(arr)
            if L == 0:
                return []
            table = [arr[:]]
            j = 1
            while (1 << j) <= L:
                prev = table[-1]
                half = 1 << (j - 1)
                table.append([max(prev[k], prev[k + half]) for k in range(L - (1 << j) + 1)])
                j += 1
            return table

        def query_sparse(table, l, r):
            if l > r or not table:
                return NEG
            length = r - l + 1
            k = length.bit_length() - 1
            return max(table[k][l], table[k][r - (1 << k) + 1])

        Kt = build_sparse(Karr)
        Gt = build_sparse(Garr)
        A2t = build_sparse(A2arr)
        A3t = build_sparse(A3arr)

        ans = []
        for l, r in queries:
            if m == 0:
                ans.append(total_ones)
                continue

            i_lo = bisect.bisect_right(Sarr, l)
            i_hi = bisect.bisect_left(Earr, r) - 1

            if i_lo > i_hi:
                ans.append(total_ones)
                continue

            lo, hi = i_lo, i_hi
            p = bisect.bisect_left(Lzarr, l, lo, hi + 1)
            qplus = bisect.bisect_right(Rzarr, r, lo, hi + 1)
            b1, b2 = min(p, qplus), max(p, qplus)

            gain = 0

            if b1 - 1 >= lo:
                v = query_sparse(A3t, lo, b1 - 1)
                if v != NEG:
                    gain = max(gain, v - l)

            if b2 - 1 >= b1:
                if p <= qplus:
                    v = query_sparse(Gt, b1, b2 - 1)
                    if v != NEG:
                        gain = max(gain, v)
                else:
                    v = query_sparse(Kt, b1, b2 - 1)
                    if v != NEG:
                        gain = max(gain, v + (r - l))

            if hi >= b2:
                v = query_sparse(A2t, b2, hi)
                if v != NEG:
                    gain = max(gain, v + r)

            ans.append(total_ones + gain)

        return ans