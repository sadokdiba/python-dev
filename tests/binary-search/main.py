# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.

class binarySearch:
    def __init__(self):
        pass

    def search(self, nums, target):
        #initialize pointers
        self.left = 0
        self.right = len(nums) - 1

        # Binary search
        while self.left <= self.right:
            #Find middle index
            mid = (self.left + self.right) // 2

            #if target is found
            if nums[mid] == target:
                return mid
            #if target is smaller, search left half
            elif nums[mid] < target:
                self.left = mid + 1
            #if target is larger, search right half
            else:
                self.right = mid - 1

        #if target is not found
        return -1

nums = [-1,0,3,5,9,12,45,67,89,100]
target = 89

searcher = binarySearch()
print(searcher.search(nums, target)) 