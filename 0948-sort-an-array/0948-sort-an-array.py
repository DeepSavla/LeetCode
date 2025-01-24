class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(nums):
            #divide
            if len(nums)<=1:
                return nums
            mid = len(nums)//2
            leftHalf = merge(nums[:mid])
            rightHalf = merge(nums[mid:])

            return mergesort(leftHalf, rightHalf)

        def mergesort(leftArray, rightArray):
            #conquer
            result = []
            i = 0
            j = 0
            while i<len(leftArray) and j<len(rightArray):
                if leftArray[i] <= rightArray[j]:
                    result.append(leftArray[i])
                    i+=1
                else:
                    result.append(rightArray[j])
                    j+=1
            if j!=len(rightArray):
                for k in range(j,len(rightArray)):
                    result.append(rightArray[k])
            else:
                for k in range(i,len(leftArray)):
                    result.append(leftArray[k])
            return result
                


        return merge(nums)