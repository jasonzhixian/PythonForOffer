class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def findKthToTail(self, head, k):
        if head == None or k <= 0:
            return None
        slow = fast = head
        # i = 1
        # while i < k:
        for i in range(k-1):
            if fast.next != None:
                fast = fast.next
                # i += 1
            else:
                break

        while fast.next != None:
            slow = slow.next
            fast = fast.next
        return slow

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node1.next = node2
node2.next = node3
node3.next = node4

s = Solution()
print(s.findKthToTail(node1, 2).val)


        