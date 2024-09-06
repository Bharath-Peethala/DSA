# Definition for singly-linked list.
class ListNode(object):
    head = None
    tail = None
    List = []
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def addNode(self,val):
        newNode = ListNode(val)
        self.List.append(val)
        if(self.head==None):
            self.head = ListNode()
            self.head.next = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = self.tail.next
    
    def getList(self, head):
        iterator = head.next
        List = []
        while(iterator):
            List.append(iterator.val)
            iterator= iterator.next
        return List
        
        

class Solution(object):
    def modifiedList(self, nums, head):
        result = ListNode()
        newHead = result
        iterator = head
        nums = {i for i in nums}
        while(iterator):
            if iterator.val not in nums:
                result.next = ListNode(iterator.val)
                result = result.next
            iterator = iterator.next
        return newHead.next
    
singleLinkedList = ListNode()
listValues = [1,2,1,2,1,2]
nums = [2]

for val in listValues:
    singleLinkedList.addNode(val)

sol = Solution()
resultHead = sol.modifiedList(nums,singleLinkedList.head)

print(singleLinkedList.List)
print(singleLinkedList.getList(resultHead))




        