class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        target = int(target)
        totals = []

        for idx, num in enumerate(nums):
            for n in range(idx):
                var = int(nums[idx]) + int(nums[n])
                var_list = list((n, idx))
                if var == target:
                    print(var_list)
                totals.append(var)
                print(totals)


a = Solution()
a.twoSum([1,2,3,4], 3)