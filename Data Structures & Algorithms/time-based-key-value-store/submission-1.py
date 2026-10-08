class TimeMap:
    def __init__(self):
        self.dct_main = {}
        """
        dct_main = {
            # We call the value here `inner_lst`
            "Alice" = [
            [1, "Mad"],
            [2, "Angry"],
            [3, "Satisfied],
            [4, "Happy"]
            ],

            "Jack" = [
                [1, "Mad"],
            [2, "Angry"],
            [3, "Satisfied],
            ]
        }
        """

    def set(self, key: str, value: str, timestamp: int) -> None:
        dct_main = self.dct_main

        if key not in dct_main:
            dct_main[key] = [[timestamp, value]]
        else:
            dct_main[key].append([timestamp, value])

    # get("alice", 1)
    def get(self, key: str, timestamp: int) -> str:
        outer_dct = self.dct_main
        if key not in outer_dct:
            return ""
        inner_lst = outer_dct[key]
        """
        [
            [1, "Mad"],
            [2, "Angry"],
            [3, "Satisfied],
            [4, "Happy"]
        ],
        """

        l, r = 0, len(inner_lst)-1
        return self.recursiveSearch(key, timestamp, l, r)
    
    # Indices (l and r)
    def recursiveSearch(self,
        key: str,
        target: int, 
        l: int,
        r: int
    ) -> str:
        outer_dct = self.dct_main
        inner_lst = outer_dct[key]
        mid = (l + r) // 2

        # We couldn't find the timestamp.
        if l > r:
            return "" if r < 0 else inner_lst[r][1]
        
        l_timestamp = inner_lst[l][0]
        r_timestamp = inner_lst[r][0]
        m_timestamp = inner_lst[mid][0]

        if m_timestamp == target:
            return inner_lst[mid][1]
        
        elif m_timestamp > target:
            return self.recursiveSearch(key, target, l, mid - 1)
        elif m_timestamp < target:
            return self.recursiveSearch(key, target, mid + 1, r)


