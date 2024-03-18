import bisect


class TimeMap:
    q1 = None
    q2 = None

    def __init__(self):
        self.q1 = {}
        self.q2 = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if timestamp in self.q1:
            self.q1[timestamp][key] = value
        else:
            self.q1[timestamp] = {key: value}
        if key in self.q2:
            bisect.insort(self.q2[key], timestamp)
        else:
            self.q2[key] = [timestamp]

    def get(self, key: str, timestamp: int) -> str:
        if key in self.q2:
            if self.q2[key][len(self.q2[key]) - 1] <= timestamp:
                return self.q1[self.q2[key][len(self.q2[key]) - 1]][key]
            if self.q2[key][0] <= timestamp:
                index = self.search_index(self.q2[key], 0, len(self.q2[key]) - 1, timestamp)
                return self.q1[self.q2[key][index]][key]
            else:
                return ''
        else:
            return ''

    def search_index(self, sorted_list, left, right, target):
        mid = left + (right - left) // 2
        if sorted_list[left] == target:
            return left
        if sorted_list[right] == target:
            return right
        if sorted_list[mid] == target:
            return mid
        if right - left <= 1:
            return left
        if sorted_list[mid] < target:
            return self.search_index(sorted_list, mid, right, target)
        if sorted_list[mid] > target:
            return self.search_index(sorted_list, left, mid, target)
    def print_ds(self):
        print(self.q1)
        print(self.q2)


# Your TimeMap object will be instantiated and called as such:
timeMap = TimeMap()
timeMap.set("ctondw", "ztpearaw", 1)
timeMap.set("vrobykydll", "hwliiq", 2)
timeMap.set("gszaw", "ztpearaw", 3)
timeMap.set("ctondw", "gszaw", 4)
timeMap.print_ds()
print(timeMap.get("gszaw", 5))
