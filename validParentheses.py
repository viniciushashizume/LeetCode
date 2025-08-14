class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenthesesMap = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in parenthesesMap:
                if stack and stack[-1] == parenthesesMap[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return not stack