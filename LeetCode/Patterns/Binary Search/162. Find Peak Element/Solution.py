class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 0

        if len(nums) == 2 and nums[1] > nums[0]:
            return 1

        n = len(nums)
        low = 1
        high = n - 2

        while low <= high:
            mid = (low + high)//2

            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid 

            if nums[mid] > nums[mid-1]:
                low = mid + 1
            else:
                high = mid - 1

        return 0
        