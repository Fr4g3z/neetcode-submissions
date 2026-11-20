class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = dict()
        b = dict()
        if len(s) != len(t):
            return False
        for char, char1 in zip(s,t):
            if char not in a:
                a[char] = 1
            else:
                a[char] += 1
            if char1 not in b:
                b[char1] = 1
            else:
                b[char1] += 1
        if a == b:
            return True
        else: 
            return False
            

        