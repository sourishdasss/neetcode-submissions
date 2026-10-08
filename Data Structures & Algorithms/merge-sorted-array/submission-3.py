class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """


        i = len(nums1) - 1
        m -= 1
        n -= 1

        if not nums2:
            return nums1

        while i > -1:
            
            if m > -1 and nums1[m] > nums2[n]:
                nums1[i] = nums1[m]
                m -= 1

            elif n > -1:
                nums1[i] = nums2[n]
                n -= 1
            
            i -= 1

        print(nums1)