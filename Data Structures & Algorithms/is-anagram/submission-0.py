class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        is_same = sorted(s) == sorted(t)
        return is_same