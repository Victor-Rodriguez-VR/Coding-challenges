# LeetCode - add two numbers
# Definition for singly-linked list. Lists will be non-empty.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0  # Working with single digits, therefore we must account for overflow when adding. (ex: 7+5 = 12)
        solution = number = ListNode(0)  # Make both solution and number a ListNode.
        while l1 or l2 or carry:  # While none of them are null
            v1 = v2 = 0  # temporary ints.
            if l1:  # if list1 is not empty, we copy its value and go to the next.
                v1 = l1.val
                l1 = l1.next
            if l2:  # if list2 is not empty, we copy its value and go to the next.
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1+v2+carry, 10)  # Sum to calculate total, then divide to get overflow (carry)  and
            # the remainder is our single digit.
            number.next = ListNode(val)  # Save our new digit
            number = number.next  # Move onto the next index for a new number.
        return solution.next
