#coding=utf-8


'''
题目：反转一个单链表
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL

解题思路：建立三个变量:pre、cur、temp互相赋值迭代，并建立指向关系，从而实现单链表的反转
'''

class Node():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
 
 
 def reversal(self, head):
    #反转头节点，将旧链表的头节点变成新链表的尾节点
    pre = head
    cur = head.next
    pre.next = None
    #遍历每个节点，依次反转，直接尾节点结束
    while cur:
        temp = cur.next
        cur.next = pre
        pre = cur
        cur = temp
    #返回新链表头节点
    return pre
     
        
       
if __name__ == "__main__":
    head = Node(1, Node(1, Node(3, Node(4,Node(5)))))
    root = reversal(head)
    #打印出反转后的顺序
    while root:
        print (root.data)
        root = root.next
    
    
    