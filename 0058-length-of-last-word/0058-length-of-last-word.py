class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = s.split()
        k = len(l)
        return len(l[k-1])
        