"""
Implementation of a binary heap using level ordering. Assuming 1-index:
- Children of k are at position 2k and 2k+1
- Parent of k is at position k/2

http://interactivepython.org/runestone/static/pythonds/Trees/BinaryHeapImplementation.html
"""


class BinHeap(object):
    def __init__(self):
        self.data = [0]  # start at index 1
        self.size = 0

    def _bubbleup(self, i):
        while (i//2) > 0 and self.data[i] < self.data[i//2]:  # i//2 = parent
            self.data[i//2], self.data[i] = self.data[i], self.data[i//2]
            i //= 2

    def add(self, elem):
        self.data.append(elem)
        self.size += 1
        self._bubbleup(self.size)

    def min(self):
        return self.data[1]

    def _bubbledown(self, i):
        data = self.data
        i = 1
        while 2*i <= self.size or (2*i+1) <= self.size:
            if 2*i+1 > self.size and data[i] > data[2*i]:
                data[2*i], data[i] = data[i], data[2*i]
                i = 2*i
            elif data[i] > data[2*i] or data[i] > data[2*i]:
                if data[2*i] < data[2*i+1]:
                    data[2*i], data[i] = data[i], data[2*i]
                    i = 2*i
                else:
                    data[2*i+1], data[i] = data[i], data[2*i+1]
                    i = 2*i+1
            else:
                break

    def pop(self):
        if self.size <= 0:
            return
        root = self.data[1]
        self.data[1] = self.data[self.size]
        del self.data[self.size]
        self.size -= 1
        self._bubbledown(1)
        return root
