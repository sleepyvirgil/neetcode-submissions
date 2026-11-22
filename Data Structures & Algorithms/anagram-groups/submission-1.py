class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram_dict = defaultdict(list)

        for s in strs:
            letters = [0] * 26
            for l in s:
                letters[ord(l) - ord("a")] += 1
            letters = tuple(letters)
            anagram_dict[letters].append(s)

        return list(anagram_dict.values())

        