class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct = {}

        for i in nums:
            if i in dct:
                dct[i] += 1
            else:
                dct[i] = 1
        
        sorted_items = sorted(dct.items(), key=lambda item: item[1], reverse=True)
        
        return [item[0] for item in sorted_items[:k]]