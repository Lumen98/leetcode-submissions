from collections import defaultdict
class TimeMap:

    def __init__(self):
        # key : list of tuples (value, timestamp)
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        # perform a binary search at self.timeMap[key], return recent timestmap if it exists, if not then return ""

        arr = self.timeMap.get(key, [])
        if not arr:
            return ""

        l, r = 0, len(arr) - 1
        res = ""  # best value with t <= timestamp

        while l <= r:
            m = (l + r) // 2
            v, t = arr[m]

            if t == timestamp:
                return v
            elif t < timestamp:
                res = v      # candidate: latest so far that is <= target
                l = m + 1
            else:
                r = m - 1

        return res
        
