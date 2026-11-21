class KthLargest:
    """
    Design a class to find the kth largest integer in a stream
    of values, including duplicates.

    For example, the 2nd largest from [1, 2, 3, 3] is 3. The
    stream is not necessarily sorted.

    NeetCode solution = min heap of size k
    Essentially it's a bit of a hacky solution where because you will
    only ever return the K largest element, we will never care about anything else. 
    """
    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
        return self.minHeap[0]