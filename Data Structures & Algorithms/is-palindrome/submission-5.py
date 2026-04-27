class Solution:
    def isPalindrome(self, s: str) -> bool:
        forward = ""
        for i in range(len(s)):
            if s[i].isalnum():
                forward += s[i].lower()
            else:
                continue


        backward = ""
        for i in range(len(s) - 1, -1, -1):
            if s[i].isalnum():
                backward += s[i].lower()
            else:
                continue

        return forward == backward