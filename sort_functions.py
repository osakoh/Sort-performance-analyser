import random


class Sort:

    def __init__(self):
        self.swap = True  # so it runs at least once

    def bubble_sort(self, arr):
        while self.swap:
            self.swap = False  # prevents the loop doesn't run infinitely

            for num in range(0, len(arr) - 1):
                if arr[num] > arr[num + 1]:
                    self.swap = True
                    arr[num], arr[num + 1] = arr[num + 1], arr[num]
        return arr

    def insertion_sort(self, arr):

        while self.swap:
            self.swap = False  # prevents the loop doesn't run infinitely
            for index in range(1, len(arr)):
                # arr[index]- the current value in the array
                current = arr[index]
                # index - 1 because the previous line makes current to be a value in the array rather than an index
                previous = index - 1

                if current < arr[previous]:
                    self.swap = True
                    # shift the larger number to its right and the smaller number to previous
                    arr[previous + 1], arr[previous] = arr[previous], current

                current = index + 1
                previous = current - 1

        return arr

    def merge(self, arr1, arr2):
        """
        first and second list are sorted in ascending order
        function returns a sorted merged list
        """
        i = j = 0
        merged_list = []

        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                merged_list.append(arr1[i])
                i += 1
            else:
                merged_list.append(arr2[j])
                j += 1

        while i < len(arr1):
            merged_list.append(arr1[i])
            i += 1

        while j < len(arr2):
            merged_list.append(arr2[j])
            j += 1

        return merged_list

    def divide_and_merge(self, arr):
        # base case for recursion
        if len(arr) < 2:  # 1 element
            return arr

        else:
            midpoint = len(arr) // 2  # integer division
            left = arr[:midpoint]
            right = arr[midpoint:]

            l1 = self.divide_and_merge(left)
            l2 = self.divide_and_merge(right)
        return self.merge(l1, l2)



s = Sort()
l = [-1, 16, 85, 0, 12, 34, 60, 70, 8, 9, 3, 2, 5]
print(f"Bubble sort:    {s.bubble_sort(l)}")
print(f"Insertion sort: {s.insertion_sort(l)}")
print(f"Merge sort:     {s.divide_and_merge(l)}")
