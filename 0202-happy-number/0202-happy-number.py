class Solution(object):
    def isHappy(self, n):
        l=set()
        while n!=1 and n not in l:
            l.add(n)
            n=sum(int(digit)**2 for digit in str(n))
        if n==1:
            return True
        else:
            return False