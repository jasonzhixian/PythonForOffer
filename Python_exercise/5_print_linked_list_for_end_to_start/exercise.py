class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def printListFromTailToHead(self, listNode):
        if listNode is None:
            return None
        result = []
        cur = listNode
        while cur:
            result.insert(0, cur.val)
            cur = cur.next
        return result

node1 = ListNode(10)
node2 = ListNode(11)
node3 = ListNode(13)
node1.next = node2
node2.next = node3

singleNode = ListNode(12)

test = ListNode(None)

solution = Solution()
print(solution.printListFromTailToHead(node1))
print(solution.printListFromTailToHead(test))
print(solution.printListFromTailToHead(singleNode))
