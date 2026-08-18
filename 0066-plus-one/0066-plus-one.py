class Solution(object):
    def plusOne(self, digits):
        if digits[-1]!=9:
            digits[-1]+=1
            return digits
        
        index=len(digits)-1
        digits[index]=0
        for i in range(index-1,-1,-1):
            if digits[i]!=9:
                digits[i]+=1
                return digits
            digits[i]=0
        new=[0]*(index+2)
        new[0]=1
        return new