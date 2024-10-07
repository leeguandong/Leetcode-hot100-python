"""
给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# https://leetcode.cn/problems/intersection-of-two-linked-lists/solutions/12624/intersection-of-two-linked-lists-shuang-zhi-zhen-l
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        A, B = headA, headB
        while A != B:  # 总会相交
            A = A.next if A else headB
            B = B.next if B else headA
        return A


if __name__ == "__main__":
    headA = ListNode([4, 1, 8, 4, 5])
    headB = ListNode([5, 6, 1, 8, 4, 5])
    result = Solution().getIntersectionNode(headA, headB)
    while result:
        print(result.val)
        result = result.next
