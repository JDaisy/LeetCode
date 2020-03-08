#coding=utf-8

'''
题目：
统计所有小于非负整数 n 的质数的数量。

示例:
输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 


解题思路1：暴力循环，这种方法在leetcode里跑用例时因为超时不通过
1、质数定义：只能被1或者它本身整除的非负整数。1不是质数
2、两个循环，第一个循环遍历N，做被除数；第二个循环遍历i,做除数。如果除了它自己做除数，还有其他数做除数能整除第一个循环的数，说明他不是质数，跳出循环，count加1


'''

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        #第一个循环遍历N,i做被除数。1不是质数，所以不用考虑，从2开始
        for i in range(2, n)：
            #设置标志位，当flag=1时，count+1
            flag = 1
            #第一个循环遍历i,j做除数
            for j in range(2, i):
                #如果除了自己外，还有其他数能整除i,说明不是质数，则将flag置为0，且跳出此循环
                if i % j == 0:             
                    flag = 0
                    break
            #如果flag=1，则count+1
            if flag == 1：           
                count + = 1
        return count