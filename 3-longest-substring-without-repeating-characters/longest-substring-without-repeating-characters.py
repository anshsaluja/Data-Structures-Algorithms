class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        char_set = set()
        left = 0
        maxlength = 0


        for right in range(len(s)):

            while s[right] in char_set:
                char_set.remove(s[left])
                left+=1
            
            char_set.add(s[right])
            maxlength = max(maxlength, right-left+1)

        return maxlength


        