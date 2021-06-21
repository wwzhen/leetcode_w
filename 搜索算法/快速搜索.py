# -*- coding: utf-8 -*-
# @Time    : 2021/6/20 10:49
# @Author  : wwzhen

import random


def partition(sequence, left, right, pivot_index):
    pivot_value = sequence[pivot_index]
    sequence[pivot_index], sequence[right] = sequence[right], sequence[
        pivot_index]  # 交换两个元素，使pivot_index与最右边元素置换位置，即先将pivot移动到最右边
    store_index = left
    for i in range(left, right):
        if sequence[i] < pivot_value:
            sequence[store_index], sequence[i] = sequence[i], sequence[
                store_index]  # 交换两个元素，使当前遍历元素(小于pivot_value的元素)与store_index元素置换位置
            store_index = store_index + 1  # store_index索引增加1
    sequence[store_index], sequence[right] = sequence[right], sequence[
        store_index]  # 交换两个元素，使store_index与最右边元素置换位置，即交换回来pivot最终应该在的位置
    return store_index


def quick_search(sequence, left, right, k):
    if left == right:  # 如果只有一个元素
        return sequence[left]  # 返回该元素
    pivot_index = left + random.randint(0, right - left + 1)  # 初始pivot_index，使pivot_index在无序表随机
    pivot_index = partition(sequence, left, right, pivot_index)  # pivot在已经排好序的位置
    if k == pivot_index:
        return sequence[k]  # 返回该位置元素
    elif k < pivot_index:
        return quick_search(sequence, left, pivot_index - 1, k)  # 需要在[left,pivot_index-1]里面继续快速检索
    else:
        return quick_search(sequence, pivot_index + 1, right, k)  # 需要在[pivot_index+1,right]里面继续快速检索


if __name__ == '__main__':
    sequence = [12, 1, 21, 34, 25, 15, 35, 13, 45, 100, 234, 521, 345, 16, 1314]
    left = 0
    right = len(sequence) - 1
    k = int(input("Find the k'th smallest number in sequence,k=")) - 1
    value = quick_search(sequence, left, right, k)
    print("The %s 'th smallest number in sequence is : %s" % (k + 1, value))
