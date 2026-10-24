class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        l = nums.copy()
        nums.extend(l)
        return nums
        