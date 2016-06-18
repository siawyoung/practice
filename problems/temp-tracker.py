
from collections import defaultdict

class TempTracker:
    def __init__(self):
        self.hash_map = defaultdict(int)
        self.size = 0
        self._min = float('inf')
        self._max = float('-inf')
        self.mean = 0
        self.mode_max = 0
        self.mode = []

    def insert(self, item):
        if item > self._max:
            self._max = item
        if item < self._min:
            self._min = item
        self.mean = (self.size * self.mean + item) / (self.size + 1)
        self.size += 1

        self.hash_map[item] += 1
        if self.hash_map[item] == self.mode_max:
            self.mode.append(item)
        elif self.hash_map[item] > self.mode_max:
            self.mode_max = self.hash_map[item]
            self.mode = [item]

    def get_max(self):
        return self._max

    def get_min(self):
        return self._min

    def get_mean(self):
        return self.mean

    def get_mode(self):
        return self.mode

tt = TempTracker()

tt.insert(1)
tt.insert(2)
tt.insert(2)

print(tt.get_mean())
print(tt.get_mode())


