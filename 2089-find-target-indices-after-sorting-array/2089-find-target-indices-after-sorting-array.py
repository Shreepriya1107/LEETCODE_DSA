class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        k = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == target:
                k.append(i)
        return k
                
        