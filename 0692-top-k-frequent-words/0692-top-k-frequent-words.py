class Solution:
    def topKFrequent(self, words, k):
        freq={}
        for w in words:
            freq[w]=freq.get(w,0)+1
        arr=list(freq.items())
        arr.sort(key=lambda x:(-x[1],x[0]))
        res=[]
        for i in range(k):
            res.append(arr[i][0])
        return res