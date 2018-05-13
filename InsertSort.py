#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'chenquanbin'
# __date__ = '2018/5/13'


def insert_sort(datalist):
    for i in range(1,len(datalist)):
        temp = datalist[i]
        for j in range(i,0,-1):
            if datalist[j-1] > temp:
                # 往右移动
                datalist[j] = datalist[j-1]
            else:
                break
            datalist[j-1] = temp




if __name__ == '__main__':
    datalist = [5, 3, 8, 1, -4, 0, 100, 66, 32, 75]
    insert_sort(datalist)
    print(datalist)