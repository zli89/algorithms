"""
Given a string, find the length of the longest substring without repeating characters.
For example, the longest substring without repeating letters for "abcabcbb" is "abc", 
which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.
"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        char_index = {}
        start = 0
        ans = 0
        for i in range(len(s)):
            if s[i] in char_index and char_index[s[i]] >= start:
                if ans < i - start:
                    ans = i - start
                start = char_index[s[i]] + 1
            char_index[s[i]] = i
        if ans < len(s) - start:
            ans = len(s) - start
        return ans
