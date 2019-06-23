#coding=utf-8


'''
题目：给定一个链表，判断链表中是否有环

解题思路1：依次遍历每个节点，并将该节点放入set中，每次遍历节点时看set中是否已存在该节点，若存在则有环，若不存在则无环
解题思路2: 定义两个指针，一快一慢，快的每次走两步，慢的每次走一步，如果有环，则两指针必定会相遇
'''

class Node():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        

def solution(self, head):
    fast = head
    slow = head
    while fast and slow and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            print ("true")
    print ("false")
    
    
if __name__ == "__main__":
    head = Node(1, Node(2, Node(1)))
    solution(head)
    
    
    
    