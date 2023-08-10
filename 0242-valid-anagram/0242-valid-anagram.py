class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)
        if len(s) == len(t):
            #using zip to looping inside two strings
            for char_s, char_t in zip(s, t):
                if char_s != char_t:
                    return False
            return True
        else:
            return False