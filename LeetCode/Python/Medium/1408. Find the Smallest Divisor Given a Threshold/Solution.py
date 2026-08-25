class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        def summ(mid):

            sum1 = 0
            for i in range(len(nums)):
                sum1 += ( nums[i] + mid - 1)//mid
                
            return sum1

        low = 1
        high = max(nums)

        while low <= high:
            mid = (low+high)//2

            total = summ(mid)

            if total <= threshold:
                high = mid - 1

            else:
                low = mid + 1

        return low