class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        default_list = list(s)
        split_list = default_list[:]
        last_idx = 0
        longest = []
        is_loop_continue = True

        while is_loop_continue:
            result1 = self.iterate(split_list, last_idx)
            last_idx = result1[1]
            longest_list = result1[0]
            # print(longest_list, len(longest))
            if longest_list:
                if len(longest_list) > len(longest):
                    longest = longest_list
            else:
                is_loop_continue = False
            split_list = default_list[last_idx: len(split_list)]
        return (len(longest))

    def iterate(self, list_s, last_idx):
        longest_list = []
        for idx, n in enumerate(list_s):
            if n not in longest_list:
                longest_list.append(n)
            else:
                last_idx = idx
                break
        return longest_list, last_idx


s = Solution()
print(s.lengthOfLongestSubstring("pwwkew"))






# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:
#
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
#
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.