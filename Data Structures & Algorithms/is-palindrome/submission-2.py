class Solution:
    def isPalindrome(self, s: str) -> bool:
        forward_str = ""
        for char in s:
            if char.isdigit() or char.isalpha():
                forward_str += char.lower()
            else:
                continue
        print(forward_str)

        backward_str = ""
        backward_s = s[::-1]
        for char in backward_s:
            if char.isdigit() or char.isalpha():
                backward_str += char.lower()
            else:
                continue
        print(backward_str)

        return (forward_str == backward_str)