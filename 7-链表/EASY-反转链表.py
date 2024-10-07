"""
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
"""

# https://leetcode.cn/problems/reverse-linked-list/solutions/1992225/you-xie-cuo-liao-yi-ge-shi-pin-jiang-tou-o5zy
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur, pre = head, None
        while cur:
            tmp = cur.next
            cur.next = pre

            pre = cur
            cur = tmp
        return pre

# tmp给cur，cur.next给pre

if __name__ == '__main__':
    s = Solution()
    result = s.reverseList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
    while result:
        print(result.val)
        result = result.next