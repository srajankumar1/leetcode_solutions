class Solution(object):
    def average(self, salary):
        mins=salary[0]
        maxs=salary[0]
        sums=0
        for num in salary:
            if num<mins:
                mins=num
            if num>maxs:
                maxs=num
            sums+=num
        return float(sums-maxs-mins) / (len(salary)-2)