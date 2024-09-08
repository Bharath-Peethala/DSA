# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def splitListToParts(self, head, k):
        result = [None for i in range(k)]
        n = 0
        iterator = head
        while(iterator):
            n+=1
            iterator = iterator.next

        if k >= n:
            iterator = head
            i = 0
            while(iterator):
                appendingNode = ListNode(iterator.val)
                result[i] = appendingNode
                iterator = iterator.next
                i+=1
            return result
        
        noOfExtra = n%k
        iterator = head
        index = 0
        while iterator:
            sliceValue = n//k
            if noOfExtra > 0:
                sliceValue +=1
                noOfExtra -=1
            result[index] = iterator
            for _ in range(1,sliceValue):
                iterator = iterator.next
            if iterator:
                prev = iterator.next
                iterator.next = None
                iterator = prev
            index = index + 1      
        return result