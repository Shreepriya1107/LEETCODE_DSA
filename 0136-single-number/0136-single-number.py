class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        else:
            f = Counter(nums)
            l = min(f,key = f.get)
            return l
        