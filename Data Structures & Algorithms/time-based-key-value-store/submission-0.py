class TimeMap:

    def __init__(self):
        self.keyValStore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyValStore:
            self.keyValStore[key] = []
        self.keyValStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        output = ""
        values = self.keyValStore.get(key, [])
        
        l, r = 0, len(values) - 1
        while l <= r:
            midd = (l+r)//2
            if values[midd][1] <= timestamp:
                output = values[midd][0]
                l = midd + 1
            else:
                r = midd - 1
        return output
