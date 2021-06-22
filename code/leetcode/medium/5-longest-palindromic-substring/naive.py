def find_palindrome(s, left, right):
    '''
    Scan out from the left and right positions and return the longest palindrome 
    that results. Returns the empty string on no palindrome.
    '''
    while True:
        # Characters don't match
        if s[left] != s[right]:
            return s[left + 1:right]

        # We're about to hit a boundary
        if left == 0 or right == len(s) - 1:
            return s[left:right + 1]

        left -= 1
        right += 1


def longest_palindromic_substring(s):
    longest = ''

    odd = ''
    even = ''

    for i in range(len(s)):
        odd = find_palindrome(s, i, i)
        if i != len(s) - 1:
            even = find_palindrome(s, i, i + 1)

        if len(odd) > len(longest):
            longest = odd
        if len(even) > len(longest):
            longest = even

    return longest


class Solution:
    def longestPalindrome(self, s: str) -> str:
        return longest_palindromic_substring(s)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser('Prints the longest palindromic substring')
    parser.add_argument('input_string')
    args = parser.parse_args()

    print(longest_palindromic_substring(args.input_string))
