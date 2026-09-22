class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:

        def countSubarray(maxSum):
            subarray = 1
            currentsubarray = 0 

            for num in nums:
                if num + currentsubarray <= maxSum:
                    currentsubarray += num
                else:
                    subarray += 1
                    currentsubarray = num
            return subarray

        low = max(nums)
        high = sum(nums)

        while low <= high:

            mid = (low + high)//2
            subarray = countSubarray(mid)

            if subarray > k:
                low = mid + 1
            else:
                high = mid -1 
            
        return low

        