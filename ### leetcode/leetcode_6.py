class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        rows = {}
        for n in range(numRows):
            rows[f"row{n}"] = []

        s_list = list(s)
        for idx, n in enumerate(s_list):
            if idx % numRows+2 == 0:
                rows["row1"].append(n)
            elif idx % numRows+2 == 1 or idx % numRows+2 == 5:
                rows["row2"].append(n)
            elif idx % numRows+2 == 2 or idx % numRows+2 == 4:
                rows["row3"].append(n)
            else:
                rows["row4"].append(n)
        dic = []
        for n in range(4):
            dic += rows[f"row{n+1}"]
        dic_string = ''.join(dic)
        print(dic_string)


df = Solution()
df.convert("PAYPALISHIRING", 4)

# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P0     I6    N
# A1   L5 S  I G
# Y2 A4   H R
# P3     I

# P0     A4L5    N
# A1  P3  I6  I G
# Y2    H R
#      I
