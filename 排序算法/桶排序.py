# -*- coding: utf-8 -*-
# @Time    : 2021/6/20 9:38
# @Author  : wwzhen

def radix_sort(nums):
    max_num = max(nums)
    pos = len(str(max_num))  # 获取最大数的位数
    buckets = [[] for i in range(10)]  # 构建10个桶
    # 从低位到高位依次执行循环
    for i in range(pos):
        # 对序列的每一个数字进行操作
        for num in nums:
            # 获取每个数字的基数
            radix = (num // (10 ** i)) % 10
            # 将数字放到基数对应的桶中
            buckets[radix].append(num)

        # 将桶中的元素按顺序放回原数列
        idx = 0
        for bt in range(10):
            while len(buckets[bt]) > 0:
                nums[idx] = buckets[bt].pop(0)
                idx += 1
    return nums


print(radix_sort([24, 15, 32, 446, 1321, 10]))
