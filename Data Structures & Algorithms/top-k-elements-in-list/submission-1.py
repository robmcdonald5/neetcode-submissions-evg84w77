class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import collections

        freq_map = defaultdict(int)
        output = []

        for num in nums:
            freq_map[num] += 1

        sorted_map = sorted(freq_map.items(), key=lambda x: x[1], reverse=True)

        for i in range(k):
            output.append(sorted_map[i][0])

        return output