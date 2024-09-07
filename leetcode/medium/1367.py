class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def checkPath(self, head, root):
        if not head:
            return True
        
        if not root or head.val != root.val:
            return False

        return self.checkPath(head.next,root.left) or self.checkPath(head.next,root.right)

        
    def isSubPath(self, head, root):
        if not root:
            return False
        return ((head.val == root.val and self.checkPath(head, root)) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right))     


        
        