# class Solution(object):
#
#     def longestPalindrome(self, s):
#         print(self.reverse_list(s))
#         s_list = list(s)
#         total_list = []
#         current_idx = 0
#         for n in range(len(s_list)):
#             finished_list = self.make_list(s_list)
#             s_list.pop(0)
#             total_list += finished_list
#         print(total_list)
#
#     def make_list(self, s_list):
#         word_list = []
#         for idx, i in enumerate(s_list):
#             w = ''
#             for j in range(idx+1):
#                 w += s_list[j]
#             word_list.append(w)
#         return word_list
#
#     def reverse_list(self, word):
#         word_list = list(word)
#         reversed_word_list = list(word)
#         reversed_word_list.reverse()
#         if word_list == reversed_word_list:
#             return True
#         else:
#             return False
#
#
# a = Solution()
# a.longestPalindrome("abcde")
#

s = "racecar"
n = len(s)

# Define a helper function to check if a substring is a palindrome
def is_palindrome(substring):
    print(substring[::-1])
    return substring == substring[::-1]

# Find all palindromic substrings of the string
palindromic_substrings = []
for i in range(n):
    for j in range(i+1, n+1):
        substring = s[i:j]
        print(substring)
        if is_palindrome(substring):
            palindromic_substrings.append(substring)

# Print the list of palindromic substrings
print(palindromic_substrings)


