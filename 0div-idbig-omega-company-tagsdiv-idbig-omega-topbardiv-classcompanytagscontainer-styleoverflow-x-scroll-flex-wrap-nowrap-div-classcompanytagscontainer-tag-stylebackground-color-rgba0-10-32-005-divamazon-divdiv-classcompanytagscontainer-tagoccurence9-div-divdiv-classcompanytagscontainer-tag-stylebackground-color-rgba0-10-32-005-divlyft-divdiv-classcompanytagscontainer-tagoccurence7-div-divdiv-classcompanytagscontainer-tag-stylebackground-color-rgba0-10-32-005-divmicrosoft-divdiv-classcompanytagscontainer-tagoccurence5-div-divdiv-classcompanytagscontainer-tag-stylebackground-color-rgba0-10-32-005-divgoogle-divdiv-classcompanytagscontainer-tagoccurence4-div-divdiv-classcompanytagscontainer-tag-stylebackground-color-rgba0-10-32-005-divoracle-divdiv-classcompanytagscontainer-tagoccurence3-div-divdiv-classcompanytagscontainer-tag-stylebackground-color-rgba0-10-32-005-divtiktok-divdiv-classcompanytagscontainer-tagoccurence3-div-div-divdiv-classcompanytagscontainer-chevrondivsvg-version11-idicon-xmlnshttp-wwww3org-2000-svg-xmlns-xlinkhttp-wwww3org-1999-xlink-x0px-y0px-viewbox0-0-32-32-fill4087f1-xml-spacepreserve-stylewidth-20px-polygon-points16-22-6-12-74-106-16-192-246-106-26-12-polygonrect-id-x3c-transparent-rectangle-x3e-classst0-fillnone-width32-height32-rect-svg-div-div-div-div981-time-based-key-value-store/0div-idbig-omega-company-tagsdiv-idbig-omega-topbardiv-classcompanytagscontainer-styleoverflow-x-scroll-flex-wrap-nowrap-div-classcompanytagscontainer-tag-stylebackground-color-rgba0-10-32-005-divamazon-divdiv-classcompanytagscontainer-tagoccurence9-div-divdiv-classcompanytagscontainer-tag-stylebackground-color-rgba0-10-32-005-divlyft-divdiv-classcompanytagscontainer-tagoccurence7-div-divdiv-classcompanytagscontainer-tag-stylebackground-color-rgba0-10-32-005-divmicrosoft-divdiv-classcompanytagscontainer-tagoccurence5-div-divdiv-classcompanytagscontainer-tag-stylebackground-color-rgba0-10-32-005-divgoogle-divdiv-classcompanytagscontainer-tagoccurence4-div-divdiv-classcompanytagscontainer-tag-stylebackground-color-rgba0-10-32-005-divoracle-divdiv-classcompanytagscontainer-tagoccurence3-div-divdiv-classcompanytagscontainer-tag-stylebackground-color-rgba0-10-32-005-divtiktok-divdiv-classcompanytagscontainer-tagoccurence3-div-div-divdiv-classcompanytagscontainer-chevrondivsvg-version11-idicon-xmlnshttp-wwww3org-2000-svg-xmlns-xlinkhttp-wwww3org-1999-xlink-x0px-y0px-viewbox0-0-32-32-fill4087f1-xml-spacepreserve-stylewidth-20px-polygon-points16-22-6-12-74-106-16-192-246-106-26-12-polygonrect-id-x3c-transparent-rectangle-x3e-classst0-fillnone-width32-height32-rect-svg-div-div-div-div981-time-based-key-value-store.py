class TimeMap:

    def __init__(self): # O(1)
        self.value_dict = collections.defaultdict(list)
        self.time_dict = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.value_dict[key].append(value) # O(1)
        self.time_dict[key].append(timestamp) # O(1)
        
    def get(self, key: str, timestamp: int) -> str:
        l = 0
        r = len(self.time_dict.get(key,[])) - 1
        
        while l <= r:
            mid = (l+r) // 2
            current_ts = self.time_dict[key][mid]
            
            if current_ts == timestamp:
                return self.value_dict[key][mid]
            elif current_ts > timestamp:
                r = mid - 1
            else:
                l = mid + 1
            
        return self.value_dict[key][r]  if r >= 0 else ""
    
    # TC: log(n)
    # SC: O(1)
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)