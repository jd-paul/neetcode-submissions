class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        lst = []
        previous_max_value = float('-inf')
        max_value = float('-inf')
        
        """
        idea: iterate in reverse, saving the max at each step and creating a whole new array
        """
        for i in range(n-1, -1, -1):
            current = arr[i]
            max_value = max(max_value, current)
            lst.append(previous_max_value)

            previous_max_value = max_value
        
        lst[0] = -1
        return lst[::-1]