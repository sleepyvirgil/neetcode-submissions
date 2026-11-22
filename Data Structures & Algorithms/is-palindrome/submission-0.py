class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0 
        j = len(s) - 1 

        text = s.lower()

        while i < j:
            if not text[i].isalnum():
                i += 1
                continue
            elif not text[j].isalnum():
                j -= 1
                continue
            else:
                if text[i] != text[j]:
                    return False
                i += 1
                j -= 1
        
        return True