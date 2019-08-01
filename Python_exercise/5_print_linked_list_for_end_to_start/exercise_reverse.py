class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def printLinkedListFromHeadToTail(self, listNode):
        if listNode is None:
            return None
        result = []
        cur = listNode
        while cur:
            result.append(cur.val)
            cur = cur.next
        return result

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node1.next= node2
node2.next = node3
node3.next = node4

solution = Solution()
test = ListNode(None)

print(solution.printLinkedListFromHeadToTail(node1))
print(solution.printLinkedListFromHeadToTail(test))
