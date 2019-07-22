class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
#solution one
    def reverseLinkedList(self, head):
        pre = None
        while head:
            temp = head
            head = head.next
            temp.next = pre
            pre = temp
        return pre
       
#recurive solution
    def reverseListedListRe(self, head):
        if not head or not head.next:
            return head
        else:
            self.reverseListedListRe(head.next)
            head.next.next = head
            head.next = None
            return head

solution = Solution()
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = None
result = solution.reverseLinkedList(node1)
print(result.val)
print(result.next.val)
print(result.next.next.val)
print(result.next.next.next.val)





            