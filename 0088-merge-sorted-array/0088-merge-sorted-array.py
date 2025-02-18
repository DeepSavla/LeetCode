class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        curChange = len(nums1) - 1
        ptrM = m-1
        ptrN = n-1
        while ptrM >= 0 and ptrN >=0:
            if nums1[ptrM] > nums2[ptrN]:
                nums1[curChange] = nums1[ptrM]
                ptrM -= 1
            else:
                nums1[curChange] = nums2[ptrN]
                ptrN -= 1
            curChange -=1
        while ptrM >=0:
            nums1[curChange] = nums1[ptrM]
            ptrM -= 1
            curChange -=1
        while ptrN >=0:
            nums1[curChange] = nums2[ptrN]
            ptrN -= 1
            curChange -=1
        return nums1
