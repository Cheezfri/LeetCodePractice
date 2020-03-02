from typing import List


class Solution:
    def find_numbers(self, nums: List[int]) -> int:
        counter = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                counter += 1
        return counter


if __name__ == "__main__":
    ans = Solution.find_numbers(Solution, [12, 345, 2, 6, 7896])
    print(ans)