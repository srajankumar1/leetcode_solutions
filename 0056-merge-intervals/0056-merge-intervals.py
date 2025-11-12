class Solution:
    def merge(self, intervals):
        if not intervals:
            return []
        intervals.sort(key=lambda x:x[0])
        merged=[]
        start=intervals[0][0]
        end=intervals[0][1]
        for i in range(1,len(intervals)):
            s=intervals[i][0]
            e=intervals[i][1]
            if s<=end:
                if e>end:
                    end=e
            else:
                merged.append([start,end])
                start=s
                end=e
        merged.append([start,end])
        return merged