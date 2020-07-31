class MaxHeap:

    def __init__(self):
        self.count = 0
        self.data = []

    def insert(self, item):
        self.data.append(item)
        self.count += 1
        self.shift_up(self.count)

    def extract_max(self):
        self.data[0], self.data[-1] = self.data[-1], self.data[0]
        self.count -= 1
        self.shift_down(1)
        self.data.pop(-1)

    def shift_up(self, k):
        while k > 1 and self.data[k - 1] > self.data[k // 2 - 1]:
            self.data[k - 1], self.data[k // 2 - 1] = self.data[k // 2 - 1], self.data[k - 1]
            k //= 2

    def shift_down(self, k):
        while 2 * k <= self.count:
            j = 2 * k
            if j + 1 <= self.count and self.data[j - 1] < self.data[j]:
                j += 1
            if self.data[j - 1] < self.data[k - 1]:
                break
            self.data[k - 1], self.data[j - 1] = self.data[j - 1], self.data[k - 1]
            k = j
