class Solution:
    """
    Input:
        points = [[0,2],[2,2]]
        k = 1
    

    """
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = [] # Max size of `k`, composed of tuples like (Euclidean distance, [x1, y1])
        dct = {} # key, value = euclidean_key, coordinate
        heapq.heapify(minHeap)
        x1, y1 = 0, 0

        for coordinate in points:
            x2, y2 = coordinate[0], coordinate[1]
            euclidean_key = -(math.sqrt(abs((x1 - x2)**2 + (y1 - y2)**2)))
            tuple_coordinate = (euclidean_key, coordinate)
            heapq.heappush(minHeap, tuple_coordinate)
            
            if len(minHeap) > k:
                heapq.heappop(minHeap)

        
        lst = []
        for i in minHeap:
            res = i[1]
            lst.append(res)
        return lst