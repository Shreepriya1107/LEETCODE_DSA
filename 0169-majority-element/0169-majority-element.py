class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]
        #d ={}
        #for x in nums:
        #    d[x] = d.get(x,0)+1
       # for x in d:
        #    if d[x]> len(nums)//2:
         #       return x
