#2019/7/29
#5
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
    def printLinkedListFromTailToHead(self, listNode):
        if listNode is None:
            return None
        result = []
        cur = listNode
        while cur:
            result.insert(0, cur.val)
            cur = cur.next
        return result


#16
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def reverseLinkedList(self, head):
        pre = None
        while head:
            temp = head
            head = head.next
            head.next = pre
            pre = temp
        return pre

    def reverseLinkedListRe(self, head):
        if not head or not head.next:
            return None
        else:
            self.reverseLinkedListRe(head.next)
            head.next.next = head
            head.next = None
        return head

#14
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def findKthToTail(self, head, k):
        if head == None or k <= 0:
            return None
        slow = fast = head
        for i in range(k-1):
            if fast.next != None:
                fast = fast.next
            else:
                break
        while fast.next != None:
            slow, fast = slow.next, fast.next
        return slow
#17
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoSortedLinkedList(self, head1, head2):
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

    def mergeTwoSortedLinkedListRe(self, head1, head2):
        if head1 == None:
            return head2
        if head2 == None:
            return head1
        mergehead = None
        if head1.val < head2.val:
            mergehead = head1
            self.mergeTwoSortedLinkedListRe(head1.next, head2)
        else:
            mergehead = head2
            self.mergeTwoSortedLinkedListRe(head1, head2.next)
        return mergehead

#remove duplicates from sorted linked list
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        cur = head
        while cur:
            runner = cur.next
            while runner and cur.val == runner.val:
                runner = runner.next
            cur.next = runner
            cur = runner
        return head

#intersection node of two linked list
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, head1, head2):
        p1, p2 = head1, head2
        while p1 != p2:
            if not p1:
                p1 = head2
            else:
                p1 = p1.next
            if not p2:
                p2 = head1
            else:
                p2 = p2.next
        return p1


#base operation of linked list

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class linkedList(object):
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.__head == None

    def length(self):
        cur = self.__head
        count = 0
        while cur:
            cur = cur.next
            count += 1
        return count

    def travel(self):
        cur = self.__head
        while cur:
            print(cur.val)
            cur = cur.next
    
    def add(self, val):
        node = ListNode(val)
        node.nxet = self.__head
        self.__head = node
    
    def append(self, val):
        node = ListNode(val)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next:
                cur = cur.next
            cur.next = node


    def insert(self, pos, val):
        if pos <= 0:
            self.add(val)
        elif pos > (self.length()-1):
            self.append(val)
        else:
            cur = self.__head
            count = 0
            while count < pos-1:
                count += 1
                cur = cur.next
            node = ListNode(val)
            node.next = cur.next
            cur.next = node


    def remove(self, val):
        pre = None
        cur = self.__head
        while cur:
            if cur.val == val:
                if not pre:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next
    
    def search(self, val):
        cur = self.__head
        while cur:
            if cur.val == val:
                return True
            else:
                cur = cur.next
        return False






        
    
            