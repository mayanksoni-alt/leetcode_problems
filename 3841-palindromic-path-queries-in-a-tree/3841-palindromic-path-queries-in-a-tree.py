class Solution(object):
    def palindromePath(self, n, edges, s, queries):
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # 1. Euler tour: parent, depth, tin, tout
        parent = [0] * n
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        order = []
        timer = 0

        stack = [(0, -1, False)]

        while stack:
            u, p, exiting = stack.pop()

            if exiting:
                tout[u] = timer
                continue

            parent[u] = u if p == -1 else p
            tin[u] = timer + 1
            timer += 1
            order.append(u)

            stack.append((u, p, True))

            for v in reversed(graph[u]):
                if v != p:
                    depth[v] = depth[u] + 1
                    stack.append((v, u, False))

        # 2. Binary lifting table for LCA
        LOG = n.bit_length()
        up = [parent[:]]

        for k in range(1, LOG):
            prev = up[k - 1]
            up.append([prev[prev[v]] for v in range(n)])

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            for k in range(LOG):
                if diff & (1 << k):
                    u = up[k][u]

            if u == v:
                return u

            for k in range(LOG - 1, -1, -1):
                if up[k][u] != up[k][v]:
                    u = up[k][u]
                    v = up[k][v]

            return parent[u]

        # 3. Represent each character with one bit
        chars = [1 << (ord(c) - ord('a')) for c in s]

        # Root-to-node XOR masks
        prefix = [0] * n
        for u in order:
            if u == 0:
                prefix[u] = chars[u]
            else:
                prefix[u] = prefix[parent[u]] ^ chars[u]

        # 4. Fenwick tree supporting range XOR updates
        #    and point queries
        bit = [0] * (n + 1)

        def add(i, value):
            while i <= n:
                bit[i] ^= value
                i += i & -i

        def range_xor(left, right, value):
            add(left, value)
            add(right + 1, value)

        def point_query(i):
            result = 0
            while i > 0:
                result ^= bit[i]
                i -= i & -i
            return result

        # Initialize the Fenwick tree with root-path masks
        for u in range(n):
            range_xor(tin[u], tin[u], prefix[u])

        # 5. Process updates and path queries
        answer = []

        for query in queries:
            parts = query.split()

            if parts[0] == "update":
                u = int(parts[1])
                new_char = parts[2]
                new_mask = 1 << (ord(new_char) - ord('a'))

                delta = chars[u] ^ new_mask

                if delta:
                    # Every descendant's root-path mask changes
                    range_xor(tin[u], tout[u], delta)
                    chars[u] = new_mask

            else:
                u = int(parts[1])
                v = int(parts[2])

                w = lca(u, v)

                path_mask = (
                    point_query(tin[u])
                    ^ point_query(tin[v])
                    ^ chars[w]
                )

                # At most one character may have odd frequency
                answer.append(
                    (path_mask & (path_mask - 1)) == 0
                )

        return answer