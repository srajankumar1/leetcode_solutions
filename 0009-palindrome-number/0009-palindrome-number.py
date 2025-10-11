class Solution(object):
    def isPalindrome(self, num):
        temp=num
        new=0
        while num>0:
            rem=num%10
            new=new*10+rem
            num=num//10
        if temp==new:
            return True
        else:
            return False

        