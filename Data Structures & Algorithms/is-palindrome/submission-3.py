class Solution:
    def isPalindrome(self, s: str) -> bool:
        forwards, backwards = [], []

        # forwards pass
        for char in s:
            if char.isalnum():
                forwards.append(char.lower())

        # backwards pass
        for char in reversed(s):
            if char.isalnum():
                backwards.append(char.lower())

        print(forwards)
        print(backwards)
        return forwards == backwards