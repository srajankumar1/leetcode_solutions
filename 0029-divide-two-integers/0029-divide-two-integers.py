class Solution:
    def divide(self, dividend, divisor):
        if dividend==-2**31 and divisor==-1:
            return 2**31-1
        sign=-1 if (dividend<0)^(divisor<0) else 1
        a=abs(dividend)
        b=abs(divisor)
        res=0
        while a>=b:
            temp=b
            cnt=1
            while a>=temp+temp:
                temp+=temp
                cnt+=cnt
            a-=temp
            res+=cnt
        return sign*res