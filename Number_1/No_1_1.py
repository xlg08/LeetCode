'''
    @User: LG
    @Auther: http://www.xlonggang.cn
    @Date: 2025/4/8 0008 19:43 
    @Description: 
    @Project ：LeetCode 
    @File    ：No_1_1.py
    @version: 1.0
'''

# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

# 你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。
import time
nums = [13, 11, 7, 15, 2]
target = 9

startTime = time.time()
# for i in range(len(nums) // 2 + 1):
for i in range(len(nums)):
    # print(i)
    a = target - nums[i]
    if a in nums and nums.index(a) != i:
        print(a, nums[i])
        print([i, nums.index(a)])
        break
else:
    print("没有找到")
endTime = time.time()
print(endTime - startTime)
