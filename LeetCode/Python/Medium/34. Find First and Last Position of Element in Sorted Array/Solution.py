class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        #lower bound

        low = 0 
        high = len(nums) - 1
        while low <= high:
            mid = (low + high)//2

            if nums[mid] >= target:
                high = mid-1
            else:
                low = mid+1

        first = low

        #upper bound
        low = 0 
        high = len(nums) - 1
        while low <= high:
            mid = (low + high)//2

            if nums[mid] > target:
                high = mid-1
            else:
                low = mid+1

        last = low - 1

        if first == len(nums) or nums[first] != target:
            return[-1, -1]
        else:
            return[first, last]
        


        

        
 
       