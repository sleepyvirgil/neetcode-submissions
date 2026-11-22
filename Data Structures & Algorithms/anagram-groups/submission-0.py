class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram_dict = {}

        for s in strs:
            letters = [0] * 26
            for l in s:
                letters[ord(l) - ord("a")] += 1
            letters = tuple(letters)
            if letters not in anagram_dict:
                anagram_dict[letters] = []
            
            anagram_dict[letters].append(s)
        
        res = []
        for l, a in anagram_dict.items():
            res.append(anagram_dict[l])

        return res
        