class Solution:
    from collections import defaultdict
    
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        max_freq = 0
        window = defaultdict(int)

        for r in range(len(s)):
            window[s[r]] += 1
            max_freq = max(max_freq, window[s[r]])

            while (r - l + 1) - max_freq > k:
                window[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res
            