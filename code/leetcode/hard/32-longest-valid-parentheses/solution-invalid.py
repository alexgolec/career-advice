# https://leetcode.com/problems/longest-valid-parentheses/


def parse_one_paren(s):
    level = 0
    
    for idx in range(len(s)):
        c = s[idx]
        print(idx, c, level)

        if c == ')':
            if level == 0:
                return idx, s[idx + 1:]
            else:
                level -= 1
        if c == '(':
            level += 1

    if level == 0:
        return idx + 1, ''
    else:
        return 0, ''


def longest_valid_parenthesis(s):
    longest_length = 0

    while s:
        length, s = parse_one_paren(s)
        if length > longest_length:
            longest_length = length

    return longest_length


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        return longest_valid_parenthesis(s)


if __name__ == '__main__':
    print(Solution().longestValidParentheses('(()'))
