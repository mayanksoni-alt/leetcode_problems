
import heapq

class Solution(object):
    def busiestServers(self, k, arrival, load):
        n = len(arrival)

        # Segment tree: 1 means available, 0 means busy
        size = 1
        while size < k:
            size *= 2

        tree = [0] * (2 * size)

        for i in range(k):
            tree[size + i] = 1

        for i in range(size - 1, 0, -1):
            tree[i] = tree[2 * i] + tree[2 * i + 1]

        # Find first available server >= start
        def find_first(node, left, right, start):
            if right <= start or tree[node] == 0:
                return -1

            if left == right - 1:
                return left

            mid = (left + right) // 2

            result = find_first(
                node * 2, left, mid, start
            )

            if result != -1:
                return result

            return find_first(
                node * 2 + 1, mid, right, start
            )

        # Update server availability
        def update(server, available):
            pos = size + server
            tree[pos] = available

            pos //= 2

            while pos:
                tree[pos] = tree[2 * pos] + tree[2 * pos + 1]
                pos //= 2

        # Min-heap: (finish_time, server_id)
        busy = []

        handled = [0] * k

        for i in range(n):

            # Release servers whose requests have finished
            while busy and busy[0][0] <= arrival[i]:
                finish, server = heapq.heappop(busy)
                update(server, 1)

            start = i % k

            # Find next available server
            server = find_first(1, 0, size, start)

            # Wrap around to server 0 if necessary
            if server == -1:
                server = find_first(1, 0, size, 0)

            # All servers are busy: drop request
            if server == -1:
                continue

            # Assign request
            update(server, 0)
            handled[server] += 1

            heapq.heappush(
                busy,
                (arrival[i] + load[i], server)
            )

        maximum = max(handled)

        return [
            i for i in range(k)
            if handled[i] == maximum
        ]
