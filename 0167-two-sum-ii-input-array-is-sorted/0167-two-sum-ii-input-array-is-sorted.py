class Solution(object):
    def twoSum(self, numbers, target):
        a=0
        b=len(numbers)-1
        while a<b:
            if numbers[a]+numbers[b]<target:
                a+=1
            elif numbers[a]+numbers[b]>target:
                b-=1
            else:
                return [a+1,b+1]