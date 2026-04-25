class Solution:
    from collections import defaultdict

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)
        output = []

        for num in nums:
            freq_map[num] += 1

        top_k = sorted(freq_map.items(), key=lambda x: x[1], reverse=True)[:k]

        for num, freq in top_k:
            output.append(num)

        return output