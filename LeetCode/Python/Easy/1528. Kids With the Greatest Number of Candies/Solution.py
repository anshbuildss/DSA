class Solution:
    def kidsWithCandies(self, candies, extraCandies):

        maximum = max(candies)

        ans = []

        for i in range(len(candies)):

            if candies[i] + extraCandies >= maximum:
                ans.append(True)
            else:
                ans.append(False)

        return ans