import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):

        #Write your code here
        if root is None:
            return 
        queue=[]
        str1 = ""
        queue.append(root)
        
        while len(queue)>0:
            str1+=str(queue[0].data)+" "
            removed = queue.pop(0)
            if removed.left is not None:
                queue.append(removed.left)
            if removed.right is not None:
                queue.append(removed.right)
        print(str1.rstrip())





T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
