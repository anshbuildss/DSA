class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum1 = (n*(n+1))//2
        s2 = 0 

        for i in range(n):
            s2 += nums[i]
        
        return sum1 - s2