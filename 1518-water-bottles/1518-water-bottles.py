class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        ans=numBottles
        while numBottles>=numExchange:
            newBottles=numBottles//numExchange
            remBottles=numBottles%numExchange
            ans+=newBottles
            numBottles=newBottles+remBottles
        return ans