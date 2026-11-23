class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        `tasks[i]` = uppercase english character
        Each CPU cycle allows the completion of a single task, and tasks may be completed in any order.

        Identical tasks must be separated by at least `n` CPU cycles

        Input: tasks = ["X","X","Y","Y"], n = 2
        Output: 5
        Explanation: A possible sequence is: X -> Y -> idle -> X -> Y.

        O(n * m) # Worst case we have to idle for each task
        """

        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        time = 0

        heapq.heapify(maxHeap)
        
        time = 0
        q = deque() # pairs of [-cnt, idleTime]

        while maxHeap or q:
            time += 1

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        
        return time