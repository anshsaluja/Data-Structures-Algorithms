class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        hashmap = {}

        for ch in s:
            if ch in hashmap:
                hashmap[ch]+=1
            else:
                hashmap[ch]=1

        for ch in t:
            if ch not in hashmap:
                return False
            else:
                hashmap[ch]-=1
                if hashmap[ch]<0:
                    return False
        return True

        
        

                
        