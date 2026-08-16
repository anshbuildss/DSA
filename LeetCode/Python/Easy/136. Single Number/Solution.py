class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict1 = {}

        for num in nums:
            dict1[num] = dict1.get(num,  0)+1

        for num in dict1:
            if dict1[num] == 1:
                return num

        