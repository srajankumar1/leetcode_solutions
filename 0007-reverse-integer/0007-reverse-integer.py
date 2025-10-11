class Solution(object):
    def reverse(self, num):
        new=0
        if num>0:
            sign=1
        else:
            sign=-1
            num=(-1)*num
        
        while num>0:
            rem=num%10
            new=new*10+rem
            num=num//10
        val=new*sign
        if -2**31<=val and val<=(2**31)-1:
            return val
        else:
            return 0
        

        
        