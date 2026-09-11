class Solution(object):
    def uniqueOccurrences(self, arr):
        counts = {}
        for i in arr:
            counts[i] = counts.get(i, 0) + 1

        values = list(counts.values())
        return len(values) == len(set(values))