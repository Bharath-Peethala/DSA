# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def spiralMatrix(self, m, n, head):
        resultMatrix = [[] for _ in range(m)]
        for i in range(m):
            resultMatrix[i] = [-1 for _ in range(n)]

        iterator = head
        top,bottom =0,m-1
        left,right = 0,n-1
        while(iterator):
            i = left
            while(i<=right and top<=bottom and iterator):
                resultMatrix[top][i] = iterator.val
                iterator=iterator.next
                i+=1
            top+=1

            i = top
            while(i<=bottom and left<=right and iterator):
                resultMatrix[i][right] = iterator.val
                iterator=iterator.next
                i+=1
            right-=1

            i=right
            while(i>=left and top<=bottom and iterator):
                resultMatrix[bottom][i] = iterator.val
                iterator=iterator.next
                i-=1
            bottom-=1

            i=bottom
            while(i>=top and left<=right and iterator):
                resultMatrix[i][left] = iterator.val
                iterator=iterator.next
                i-=1
            left+=1
        return resultMatrix



