class Solution(object):
    def countDigits(self, num):
        l=list(map(int, str(num)))
        count=0
        for digit in l:
            if num%digit==0:
                count+=1
        return count