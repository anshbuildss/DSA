class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        right = 0 
        dict1 = {}
        n = len(s)
        maxlen = 0

        while right < n:
            if s[right] in dict1:
                left = max(left, dict1[s[right]]+1)

            maxlen = max(maxlen, right - left +1)
            dict1[s[right]] = right
            right +=1
        
        return maxlen
