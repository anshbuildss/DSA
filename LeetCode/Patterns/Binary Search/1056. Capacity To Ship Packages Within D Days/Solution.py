class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def checkvalid(mid):
            load = 0 
            day = 0
            for i in range(len(weights)):

                if (load + weights[i]) > mid:
                    day +=1
                    load = weights[i]
                else:        
                    load += weights[i]

            return day

        low = max(weights)
        high = sum(weights)

        while low <= high:
            mid = (low + high)//2

            vday = checkvalid(mid)

            if vday >= days:
                low = mid + 1
            else:
                high = mid - 1

        return low
        
