
import heapq

class Solution(object):
    def assignTasks(self, servers, tasks):
        available = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(available)

        busy = []
        ans = []
        time = 0

        for i, duration in enumerate(tasks):
            time = max(time, i)

            # Release servers that have finished
            while busy and busy[0][0] <= time:
                free_time, weight, idx = heapq.heappop(busy)
                heapq.heappush(available, (weight, idx))

            # If no server is available, wait
            if not available:
                time = busy[0][0]

                while busy and busy[0][0] <= time:
                    free_time, weight, idx = heapq.heappop(busy)
                    heapq.heappush(available, (weight, idx))

            # Choose the best available server
            weight, idx = heapq.heappop(available)

            ans.append(idx)

            # Mark server as busy
            heapq.heappush(
                busy,
                (time + duration, weight, idx)
            )

        return ans
