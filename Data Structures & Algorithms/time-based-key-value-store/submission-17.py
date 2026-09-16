from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""

        # binary search value pairs (value, timestamp) for the corrct timestamp 
        l, r = 0, len(self.timeMap[key]) - 1
        
        latestM = 0
        
        while l <= r:
            m = (l + r) // 2
            latestM = m 

            if self.timeMap[key][m][1] <= timestamp:
                # This is a valid candidate.
                # Try to find a later valid timestamp.
                l = m + 1
            else:
                # This timestamp is too large.
                r = m - 1
        
        if r >= 0:
            return self.timeMap[key][r][0]

        return ""