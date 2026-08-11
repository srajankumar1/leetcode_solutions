class Solution(object):
    def maxArea(self, height):
        start=0
        end=len(height)-1
        maxArea=0
        while start<end:
            h=min(height[start],height[end])
            area=h*(end-start)
            if area>maxArea:
                maxArea=area
            if height[start]<height[end]:
                start+=1
            else:
                end-=1
        return maxArea