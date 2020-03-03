class Solution:
    def subtract_product_sum(self, n: int) -> int:
        product_dig = 1
        sum_dig = 0
        for digit in str(n):
            sum_dig = sum_dig + int(digit)
            product_dig = product_dig * int(digit)
        return product_dig - sum_dig


if __name__ == "__main__":
    ans = Solution.subtract_product_sum(Solution, 4421)
    print(ans)
