class Solution:
    """
    You should aim for a solution with O(n * (2^n)) time and O(n) space,
    where n is the size of the input array.
    """
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.target = target
        self.output = []
        self.dct = {}
        self.candidates = candidates
        candidates.sort() # We sort so that we can see the duplicates together.
        # e.g. [1, 1, 2, 5, 6, 7, 10]
        # As we iterate forward, we iterate our pointer forward!
        
        self.recurse(0, 0, [])

        return self.output
    
    def recurse(self, index: int, total: int, lst: [int]):
        if total == self.target:                                        
            self.output.append(lst)                                     
            return
        
        if index >= len(self.candidates) or total > self.target:
            return
        
        current = self.candidates[index]

        self.recurse(index + 1, total + current, lst + [current])

        next_index = index
        while next_index < len(self.candidates) and self.candidates[next_index] == current:
            next_index += 1
        
        self.recurse(next_index, total, lst)