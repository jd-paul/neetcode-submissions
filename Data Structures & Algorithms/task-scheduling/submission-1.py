class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        # The 'Counter' subclass gives this output: Counter({'A': 3, 'B': 2, 'C': 1})


        max_freq = max(counts.values())
        count_max = sum(1 for freq in counts.values() if freq == max_freq)

        return max(len(tasks), (max_freq - 1) * (n + 1) + count_max)