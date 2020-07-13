import sys

class Node:
    def __init__(self, data):
        self.info = data
        self.link = None


class Solution:
    def __init__(self):
        self.top = None
        self.front = None
        self.rear = None
        self.queue_size = 0

    def is_s_empty(self):
        return self.top == None

    def pushCharacter(self, data):
        temp = Node(data)
        temp.link = self.top
        self.top = temp

    def popCharacter(self):
        if self.is_s_empty():
            print("Stack is empty")
        else:
            popped = self.top.info
            self.top = self.top.link
            return popped

    def is_q_empty(self):
        return self.front == None

    def enqueueCharacter(self,data):
        temp = Node(data)
        if self.is_q_empty():
            self.front = temp
        else:
            self.rear.link = temp
        self.rear = temp
        self.queue_size += 1

    def dequeueCharacter(self):
        if self.is_q_empty():
            print("Queue is empty")
        x = self.front.info
        self.front = self.front.link
        self.queue_size -=1
        return x
    # Write your code here

# read the string s
s=input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")    