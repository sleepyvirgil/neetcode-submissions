class Solution:

    def encode(self, strs: List[str]) -> str:
        coded = []
        for s in strs:
            coded.append(f"{len(s)}#{s}")

        return "".join(coded)


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        # length, sep, word
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            word_len = int(s[i:j])
            res.append(s[j + 1 : j + 1 + word_len])
            i = j + 1 + word_len

        return res




# fstring f"#{len(s)}"