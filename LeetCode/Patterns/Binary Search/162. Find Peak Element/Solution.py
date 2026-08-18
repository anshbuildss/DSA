class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        x

        n = len(nums)
        low = 0 
        high = n - 1

        while low <= high:
            mid = (low + high)//2

            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid 

            if nums[mid] > nums[mid-1]:
                low = mid + 1
            else:
                high = mid - 1

        return 0
        