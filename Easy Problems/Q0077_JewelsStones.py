class Solution:
    def num_jewels_in_stones(self, j: str, s: str) -> int:
        jewels = {}
        for jewel in j:
            if jewel not in jewels:
                jewels[jewel] = 0
        for stone in s:
            if stone in jewels:
                jewels[stone] = jewels[stone] + 1
        num_jewels = 0
        for jewel in j:
            num_jewels = num_jewels + jewels[jewel]
        return num_jewels


if __name__ == "__main__":
    ans = Solution.num_jewels_in_stones(Solution, "z", "ZZ")
    print(ans)

'''
NOTES:
for loop in
    dict_name iterates through KEY ONLY because dictionaries are mapping objects 
        and inherit special methods (ie. iterator object stuff)
    dict_name.keys() iterates through KEY ONLY
    dict_name.items() iterates through VALUE, KEY
    dict_name.values() iterates through VALUE ONLY
'''