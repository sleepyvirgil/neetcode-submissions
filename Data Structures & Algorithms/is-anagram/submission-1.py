class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        mapS = {}
        for char in s:
            if char not in mapS:
                mapS[char] = 1
            else:
                mapS[char] += 1
        
        for char in t:
            if char not in mapS:
                return False
            else:
                mapS[char] -= 1
        
        for key in mapS:
            if mapS[key] != 0:
                return False
        
        return True

