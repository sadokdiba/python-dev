class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

# real world solution:

class SolutionReal:
    def __init__(self, nums1, m, nums2, n):
        self.nums1 = nums1
        self.m = m
        self.nums2 = nums2
        self.n = n

    def merge(self):
        i, j, k = self.m - 1, self.n - 1, self.m + self.n - 1
        while i >= 0 and j >= 0:
            if self.nums1[i] > self.nums2[j]:
                self.nums1[k] = self.nums1[i]
                i -= 1
            else:
                self.nums1[k] = self.nums2[j]
                j -= 1
            k -= 1
        while j >= 0:
            self.nums1[k] = self.nums2[j]
            j -= 1
            k -= 1
    
sol = SolutionReal([1,2,3,0,0,0], 3, [2,5,6], 3)
sol.merge()
print(sol.nums1)  

