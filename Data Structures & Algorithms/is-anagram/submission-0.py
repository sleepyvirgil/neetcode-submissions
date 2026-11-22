class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       
        mapS = {}
        mapT = {}

        if len(s) != len(t):
            return False

        for char in s:
            if char not in mapS:
                mapS[char] = 1
            else: 
                mapS[char] += 1
        
        for char in t:
            if char not in mapT:
                mapT[char] = 1
            else: 
                mapT[char] += 1

        if mapS == mapT:
            return True

        return False
