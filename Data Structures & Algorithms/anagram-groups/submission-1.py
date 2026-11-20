class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sym = {}
        for chars in strs:
            c = [0] * 26
            for char in chars:
                c[ord(char) - ord('a')] += 1
            key = tuple(c)
            if key not in sym:
                sym[key] = []
            sym[key].append(chars)
        return list(sym.values())
        