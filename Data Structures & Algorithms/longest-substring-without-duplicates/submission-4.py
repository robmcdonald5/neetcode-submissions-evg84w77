class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        output = 0
        window = set()

        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            print(window)
            output = max(output, r - l + 1)

        return output