class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        c = Counter(nums)
        i=0
        k=-1
        d=0
        while i < len(c):
            key = list(c.keys())[i]
            val = c[key]
            if key%2==0:
                if val>d or(val==d and (k == -1 or key<k)):
                    k=key
                    d=val
            i+=1
        return k
            

       
            

        