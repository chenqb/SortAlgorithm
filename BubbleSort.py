#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'chenquanbin'
# __date__ = '2018/5/13'


def bubble_sort(datalist):
    for i in range(len(datalist),0,-1):
        max_index = 0
        for j in range(0,i):
            if datalist[j] > datalist[max_index]:
                max_index = j
        datalist[max_index],datalist[i-1] = datalist[i-1],datalist[max_index]


if __name__ == '__main__':
    datalist = [5, 3, 8, 1, -4, 0, 100, 66, 32, 75]
    bubble_sort(datalist)
    print(datalist)