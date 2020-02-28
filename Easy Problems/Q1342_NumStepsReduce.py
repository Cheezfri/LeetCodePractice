from typing import List


class Solution:
    def numberOfSteps (self, num: int) -> int:
        count = 0
        while num != 0:
            if num % 2 == 0:
                num /= 2
                count += 1
            else:
                num -= 1
                count += 1
        return count


if __name__ == "__main__":
    ans = Solution.numberOfSteps(Solution, 14)
    print(ans)
'''
NOTES:
None
'''