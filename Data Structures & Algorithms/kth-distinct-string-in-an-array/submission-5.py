class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        unique = []
        lst = []

        for i in arr:
            if not i in unique:
                if i not in lst:
                    lst.append(i)
                    unique.append(i)
                else:
                    lst.remove(i)
            else:
                if i in lst:
                    lst.remove(i)
        
        if len(lst) < k-1:
            return ""
        elif len(lst) == 0:
            return ""

        return lst[k-1]