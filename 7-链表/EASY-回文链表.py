"""
给你一个单链表的头节点 head ，请你判断该链表是否为
回文链表。如果是，返回 true ；否则，返回 false 。

输入：head = [1,2,2,1]
输出：true
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []
        current_node = head
        while current_node is not None:
            vals.append(current_node.val)
            current_node = current_node.next
        return vals == vals[::-1]


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(1)
    result = Solution().isPalindrome(head)
    print(result)
