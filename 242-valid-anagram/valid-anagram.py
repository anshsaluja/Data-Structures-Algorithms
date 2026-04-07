class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hashmap_s = {}
        hashmap_t = {}

        for i in range(len(s)):
            if s[i] in hashmap_s:
                hashmap_s[s[i]]+=1
            else:
                hashmap_s[s[i]]=1
        
        for i in range(len(t)):
            if t[i] in hashmap_t:
                hashmap_t[t[i]]+=1
            else:
                hashmap_t[t[i]]=1
        
        if hashmap_s == hashmap_t:
            return True
        
        return False
        

                
        