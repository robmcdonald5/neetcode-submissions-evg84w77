class Solution:
    def isValid(self, s: str) -> bool:
        para_map = {")": "(", "}": "{", "]": "["}
        stack = []

        for char in s:
            if char in para_map:
                if stack and stack[-1] == para_map[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return True if not stack else False