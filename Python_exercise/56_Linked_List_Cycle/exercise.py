class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    #if the linked list has cycle?
    def hasCycle(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                return True
        return False
    #find the cycle node
    def detectCycle(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next,next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow, fast = slow.next, fast.next
                return slow
        return None
