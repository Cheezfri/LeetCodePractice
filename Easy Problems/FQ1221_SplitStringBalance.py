import math


class Solution:
    def balanced_string_split(self, s: str) -> int:
        count = 0
        i = 0
        while i < len(s):
            if i == len(s) - 1:
                break
            if s[i] != s[i + 1]:
                i += 1
                count += 1
            print(s[i])
            i += 1
        return count


if __name__ == "__main__":
    ans = Solution.balanced_string_split(Solution, "RLRRRLLRLL")
    print(ans)

'''
NOTES:
INCOMPLETE
'''