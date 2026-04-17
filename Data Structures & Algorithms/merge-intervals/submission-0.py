class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def _overlaps(a, b):
            return b[0] <= a[1]
        
        intervals.sort(key=lambda x : [x[0]])
        merged = [intervals[0]]

        for interval in intervals[1:]:
            last = merged[-1]
            if _overlaps(last, interval):
                last[1] = max(last[1], interval[1])
            else:
                merged.append(interval)

        return merged