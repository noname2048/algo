class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for chr in s:
            # record open parenthesis
            if chr == "(" or chr == "[" or chr == "{":
                stack.append(chr)
            else:
                # cannot close parenthesis
                if not stack:
                    return False
                elif (
                    (chr == ")" and stack[-1] == "(")
                    or (chr == "]" and stack[-1] == "[")
                    or (chr == "}" and stack[-1] == "{")
                ):
                    stack.pop()
                else:
                    return False

        return not stack


solution = Solution()
assert solution.isValid("()") is True
assert solution.isValid(r"()[]{}") is True
assert solution.isValid(r"(])") is False
assert solution.isValid(r"{(})") is False
