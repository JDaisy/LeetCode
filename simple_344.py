#coding=utf-8


'''
题目：编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。
不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。

输入：["h","e","l","l","o"]
输出：["o","l","l","e","h"]

解题思路：由于只能原地修改字符串，所以不能使用str[::-1]的方式，更不能使用高级函数reverse()。两个循环：i(从头往后)，j(从尾往前)，当i<j的时候，就交换两个值
'''


class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s)-1
        while i < j:
            s[i],s[j] = s[j],s[i]
            i = i + 1
            j = j - 1
        return s
        
s = Solution()
L = ["h","e","l","l","o"]
print(s.reverseString(L))
print(L)

#输出结果如下：
#['o', 'l', 'l', 'e', 'h']
#['o', 'l', 'l', 'e', 'h']




'''
L = ["h","e","l","l","o"]
print(L[::-1])
print(L)

切片的反转字符串不会修改原字符串的。
以上代码的输出如下：
['o', 'l', 'l', 'e', 'h']
['h', 'e', 'l', 'l', 'o']
'''




