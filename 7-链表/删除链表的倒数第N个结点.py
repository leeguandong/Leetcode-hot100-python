"""
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
"""
from typing import Optional


# https://leetcode.cn/problems/remove-nth-node-from-end-of-list/solutions/2004057/ru-he-shan-chu-jie-dian-liu-fen-zhong-ga-xpfs
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 由于可能会删除链表头部，用哨兵节点简化代码
        left = right = dummy = ListNode(next=head)

        for _ in range(n):
            right = right.next  # 右指针先向右走 n 步

        while right.next:
            left = left.next
            right = right.next  # 左右指针一起走
        left.next = left.next.next  # 左指针的下一个节点就是倒数第 n 个节点
        return dummy.next

    # right走到投了，left和right差着n，所以left是倒数的n，直接把下一个copy过来即可


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    result = Solution().removeNthFromEnd(head, 2)
    print(result)
    # 返回具体链表的值
    while result:
        print(result.val)
        result = result.next