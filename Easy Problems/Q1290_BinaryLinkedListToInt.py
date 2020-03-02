class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def get_decimal_value(self, head: ListNode) -> int:
        temp = head
        temp_string = ""
        answer = 0
        while temp.next is not None:
            temp_string = temp_string + str(temp.val)
            temp = temp.next
        temp_string = temp_string + str(temp.val)
        length = len(temp_string) - 1
        for val in temp_string:
            answer = answer + (int(val) * (2 ** length))
            length -= 1
        return answer


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(0)
    head.next.next = ListNode(1)
    ans = Solution.get_decimal_value(Solution, head)
    print(ans)

'''
NOTES
Python uses 'None' instead of null, use 'is not' to compare them
'**' is the exponent operator 
'^' is the XOR operator
'''