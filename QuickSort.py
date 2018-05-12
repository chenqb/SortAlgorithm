#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'chenquanbin'
# __date__ = '2018/5/12'


def partition(datalist, left, right):
    privot = right
    while left<right:
        while left<right and datalist[left] < datalist[privot]:
            left += 1
        if left<right:
            datalist[left],datalist[privot] = datalist[privot], datalist[left]
            privot = left
        while left<right and datalist[right] > datalist[privot]:
            right -= 1
        if left<right:
            datalist[privot], datalist[right] = datalist[right],datalist[privot]
            privot = right
    return privot



def quick_sort(datalist, left, right):
    if left<right:
        dp = partition(datalist, left, right)
        quick_sort(datalist, left, dp-1)
        quick_sort(datalist, dp+1, right)


if __name__ == '__main__':
    datalist = [5,3,8,1,-4,0,100,66,32,75]
    quick_sort(datalist, 0, len(datalist)-1)
    print(datalist)




