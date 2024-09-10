class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        if not head:
            return head
        gcd = lambda a, b: a if b == 0 else gcd(b, a % b)
        prev = head
        curr = head.next
        while(curr):
            temp = prev.next
            gcdVal = gcd(prev.val,curr.val)
            newNode = ListNode(gcdVal)
            prev.next = newNode
            newNode.next = temp
            prev  = curr
            curr = curr.next
        return head