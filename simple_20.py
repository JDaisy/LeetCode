#coding=utf-8


'''
题目：有效的括号
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：
	左括号必须用相同类型的右括号闭合。
	左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

解题思路：用栈，左括号入栈，右括号比较：如果右括号跟栈顶数据匹配，则出栈。如果是有效的括号，那么最后栈里没有数据。
'''


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
		#把匹配的左右括号当成字典的key和value
        dict={'(':')','[':']','{':'}'}
		#使用栈这种数据结构
        stack=[]
		#先比较字符串长度，如果是奇数或者空字符串直接输出false
        if len(s)%2 != 0 or len(s) == 0:
            print ("false")
        else:
            for current in s:
				#如果是左括号，直接进栈
                if current in dict.keys():
                    stack.append(current)
				#如果是右括号
                elif current in dict.values():
					#且栈里没有数据或者当前右括号与栈顶元素对应的右括号不相等，输出false
                    if len(stack) == 0 or current != dict.get(stack[-1]):
                        print ("false")
					#如果相等，则将栈顶的元素删除（python：list.pop()是删除列表末尾元素）
                    else:
                        stack.pop()
			#循环结束之后来查看栈里元素个数，如果为空则是有效括号,不为空则为false
            if len(stack) == 0:
                print ("true")
            else:
                print ("false")			
			
											
			
if __name__ == "__main__":
    s1 = Solution()
    s1.isValid("({1})")
        






