#coding=utf-8

'''
题目：
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

解题思路1:两个循环，第一个循环为X，第二个循环为Y，如果x+y=target，则返回x、y的下标
解题思路2：一个循环x,如果target-x也在nums中，则返回x、target-x的下标
'''


class Solution(object):
    def twoSum(self, nums, target):
        '''
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
		'''
        n = len(nums)
        #x是第一个加数的下标
        for x in range(n):
            #m是第二个加数
            m = target-nums[x]
            #y是第二个加数的下标
            y = nums.index(m)
            #需要排除同一个下标的值相加刚好是target的情况
            if m in nums and x != y:
                print x,y
                
                
                
if __name__ == "__main__":
    s = Solution()
    s.twoSum([3,2,4], 6)