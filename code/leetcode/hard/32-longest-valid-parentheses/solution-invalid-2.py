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


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        start, end = None, None
        longest_paren = 0

        for region in parse(s):
            level, s, e = region
            print(region)

            if start is None:
                start, end = s, e
                print('Initial set')
                continue

            # The start of this paren is before the current one, meaning it 
            # contains the current one
            if s < start:
                assert e > end
                start, end = s, e
                print('popping up')

            if end == s - 1:
                # This paren comes right after the current one, meaning they 
                # should be concatenated together
                end = e
                print('extending right')
            else:
                # This paren comes is not immediately after the current one, 
                # meaning we can count the current one and move on
                longest_paren = max(longest_paren, end - start + 1)
                start, end = s, e
                print('moving on')

        if start is not None and end is not None:
            longest_paren = max(longest_paren, end - start + 1)

        return longest_paren


if __name__ == '__main__':
    print(Solution().longestValidParentheses('()(())'))
