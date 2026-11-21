class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)
        c =0
        l = []
        for i in range(len(s)-k+1):
            l.append(s[i:i+k])
        for j in range(len(l)):
            if int(l[j])!=0 and  num%int(l[j])== 0:
                c+=1
        return c



        