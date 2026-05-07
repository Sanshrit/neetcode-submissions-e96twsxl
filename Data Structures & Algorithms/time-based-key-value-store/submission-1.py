class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timeMap:
            self.timeMap[key].append((value,timestamp))
        else:
            self.timeMap[key] = [(value,timestamp)]
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        ans = ""
        lists = self.timeMap[key]
        low = 0
        high = len(lists)-1
        while low<=high:
            mid = (low+high)//2
            if lists[mid][1] <= timestamp:
                ans = lists[mid][0]
                low = mid + 1
            else:
                high = mid-1
        return ans