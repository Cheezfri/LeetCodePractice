from typing import List


class Solution:
    def brute_force_fail(self, nums: List[int]) -> List[int]:
        answer = [1 for i in range(len(nums))]
        for i in range(len(nums)):
            for j in range(len(answer)):
                if i != j:
                    answer[j] = answer[j] * nums[i]
        return answer

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward_list = []
        reverse_list = []
        for i in range(len(nums)):
            if i == 0:
                forward_list.append(1)
            else:
                forward_list.append(nums[i - 1] * forward_list[i - 1])
        nums.reverse()
        for i in range(len(nums)):
            if i == 0:
                reverse_list.append(1)
            else:
                reverse_list.append(nums[i - 1] * reverse_list[i - 1])
        reverse_list.reverse()
        answer = [forward * reverse for forward, reverse in zip(forward_list, reverse_list)]
        return answer


if __name__  == "__main__":
    ans = Solution.productExceptSelf(Solution, [1, 2, 3, 4])
    for num in ans:
        print(num)
