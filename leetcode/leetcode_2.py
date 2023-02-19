
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_n = self.reverse_list(l1)
        l2_n = self.reverse_list(l2)
        str_result = str(l1_n + l2_n)
        b = list(str(self.reverse_list(list(str_result))))
        c = []
        for n in b:
            c.append( int(n))
        print(c)


    def reverse_list(self, li):
        li_new = []
        number = ""
        for n in li:
            if n ==1:
                li_new.append(str(n))
            else:
                li_new.insert(0, str(n))
        for n in li_new:
            number += n
        num_number = int(number)
        return num_number



c = Solution()
c.addTwoNumbers([9,9,9,9,9,9,9], [9,9,9,9])





# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.