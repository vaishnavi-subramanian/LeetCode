class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals=sorted(intervals, key=lambda x:x[1])
        counter=0
        start1=intervals[0][0]
        end1=intervals[0][1]
        for i in range(1,len(intervals)):
            start2=intervals[i][0]
            end2=intervals[i][1]
            if start2<end1:
                counter+=1
            else:
                start1=start2
                end1=end2
        return counter