class Solution(object):
    def addToArrayForm(self, num, k):
        a=0
        for n in num:
            a=a*10+n
        b=a+k
        nums=[]
        while b>0:
            nums.append(b%10)
            b=b//10
        return nums[::-1]