from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i, num in enumerate(nums):
            print("I: " + str(i))
            print("Num: " + str(num))
            n = target - num
            if n not in h:  # Checks if n is key in hashmap
                h[num] = i  # adds to hashmap where key: Num and Value: i
            else:
                return [h[n], i]


if __name__ == "__main__":
    GivenNums = [2, 7, 11, 15]
    target = 9
    ans = Solution.twoSum(Solution, GivenNums, target)

'''
NOTES
Enumerate returns the [Index, ValueItself]
'''