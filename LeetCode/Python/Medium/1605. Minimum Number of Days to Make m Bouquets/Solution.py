class Solution:
    def minDays(self, bloomDay, m, k):

        if m * k > len(bloomDay):
            return -1

        low = min(bloomDay)
        high = max(bloomDay)

        while low <= high:

            mid = (low + high) // 2

            count = 0
            ans = 0

            for i in bloomDay:

                if i <= mid:
                    count += 1

                    if count == k:
                        ans += 1
                        count = 0

                else:
                    count = 0

            if ans >= m:
                high = mid - 1
            else:
                low = mid + 1

        return low
                

            
            

                    



       

        