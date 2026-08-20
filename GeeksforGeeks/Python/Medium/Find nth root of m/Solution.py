class Solution:
    def nthRoot(self, n, m):
        
        if m == 0:
            return 0
        
        low = 1
        high = m

        while low <= high:
            mid = (low + high) // 2
            val = mid ** n  # Calculate mid to the power of n

            if val == m:
                return mid   # Found the exact nth root
            elif val < m:
                low = mid + 1
            else:
                high = mid - 1

        return -1