class Solution:
    def isValid(self, s: str) -> bool:
        m = {
            "(": ")",
            "[": "]",
            "{": "}",
        }

        stack = []
        for chr in s:
            # record open parenthesis
            if chr in ["(", "[", "{"]:
                stack.append(chr)
            else:
                # cannot close parenthesis
                if not stack:
                    return False

                # close order not correct
                tail = stack[-1]
                match = m[tail]
                if match != chr:
                    return False

                # close parenthesis
                stack.pop()

        # unclosed parenthesis
        if stack:
            return False

        # no gard condition detected
        return True


solution = Solution()
assert solution.isValid("()") is True
assert solution.isValid(r"()[]{}") is True
assert solution.isValid(r"(])") is False
assert solution.isValid(r"{(})") is False
