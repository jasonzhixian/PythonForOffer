class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    #solution one
    def mergeSortedLinkedList(self, head1, head2):
        cur = dummy = ListNode(0)
        while head1 and head2:
            if head1.val < head2.val:
                cur.next = head1
                head1 = head1.next
            else:
                cur.next = head2
                head2 = head2.next
            cur = cur.next
        cur.next = head1 or head2
        return dummy.next

    #solution recursive
    def mergeSortedLinkedList_2(self, head1, head2):
        if head1 == None:
            return head2
        if head2 == None:
            return head1
        mergehead = None
        if head1.val < head2.val:
            mergehead = head1
            mergehead.next = self.mergeSortedLinkedList_2(head1.next, head2)
        else:
            mergehead = head2
            mergehead.next = self.mergeSortedLinkedList_2(head2.next, head1)
        return mergehead



node1 = ListNode(1)
node2 = ListNode(3)
node3 = ListNode(5)
node1.next = node2
node2.next = node3

node4 = ListNode(2)
node5 = ListNode(4)
node6 = ListNode(6)


node4.next = node5
node5.next = node6

solution = Solution()
solution.mergeSortedLinkedList(node1, node4)
print(node4.next.val)

        