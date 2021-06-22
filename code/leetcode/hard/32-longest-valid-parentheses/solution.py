from collections import defaultdict


def parse(s):
    stack = [('*', 0)]

    for idx in range(1, len(s) + 1):
        c = s[idx - 1]

        if c == '(':
            stack.append(idx)
        if c == ')':
            if len(stack) == 1:
                continue
            else:
                pos = stack.pop()
                yield len(stack), pos, idx


class ParenParser:
    def __init__(self):
        self.start, self.end = None, None
        self.longest_paren = None

    def add_paren(self, start, end):
        if self.end == start - 1:
            self.end = end
        else:
            self.start, self.end = start, end

        return self.end - self.start + 1


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        levels = defaultdict(ParenParser)
        longest_paren = 0

        for region in parse(s):
            level, start, end = region
            length = levels[level].add_paren(start, end)

            if longest_paren is None or length > longest_paren:
                longest_paren = length

        return longest_paren


if __name__ == '__main__':
    print(Solution().longestValidParentheses('(()'))
