from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        uniques = set()
        for num in nums:
            if num not in uniques:
                uniques.add(num)
            else:
                return True
        return False


if __name__ == "__main__":
    ans = Solution.containsDuplicate(Solution, [1, 2, 3, 4])
    print(ans)
