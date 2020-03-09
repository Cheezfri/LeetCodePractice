from typing import List
import sys

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        answers = set()
        ans = 0
        for num in nums:
            if ans + num < 0:
                answers.add(num)  # Takes care of edge case of highest negative number
                ans = 0
            else:
                ans = ans + num
                answers.add(ans)
        return max(answers)


if __name__ == "__main__":
    # ans = Solution.maxSubArray(Solution, [-2, 1, -3, 4, -1, 2, 1, -5, 4])
    ans = Solution.maxSubArray(Solution, [-1])
    print(ans)
