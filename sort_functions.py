class Sort:

    def __init__(self):
        self.swap = True  # so it runs at least once

    def bubble_sort(self, arr):
        while self.swap:
            self.swap = False

            for num in range(0, len(arr) - 1):
                if arr[num] > arr[num + 1]:
                    self.swap = True
                    arr[num], arr[num + 1] = arr[num + 1], arr[num]
        return arr

s = Sort()
l = [-1, 16, 85, 0, 12, 34, 60, 70, 8, 9, 3, 2, 5]
print(s.bubble_sort(l))