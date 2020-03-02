class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for row in grid:
            for element in reversed(row):
                if element >= 0:
                    break
                else:
                    count += 1
        return count


if __name__ == "__main__":
    print "wow"

'''
Notes:
reversed helps with time complexity
'''