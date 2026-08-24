class Solution:
    def maximumWealth(self, accounts):
        ans = 0

        for i in accounts:
            total = 0

            for j in i:
                total += j

            if total > ans:
                ans = total

        return ans