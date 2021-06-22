'''
A stackless recursive implementation
'''

from typing import List

def valid_parens(s, parens_open, parens_remaining):
    if parens_open == 0 and parens_remaining == 0:
        yield ''.join(s)

    if parens_open > 0:
        s.append(')')
        yield from valid_parens(s, parens_open - 1, parens_remaining)
        s.pop()
    if parens_remaining > 0:
        s.append('(')
        yield from valid_parens(s, parens_open + 1, parens_remaining - 1)
        s.pop()


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return list(set(valid_parens([], 0, n)))


if __name__ == '__main__':
    print(Solution().generateParenthesis(4))
