#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'chenquanbin'
# __date__ = '2018/5/13'

def merge(datalist1, datalist2):
    result = []
    i=0
    j=0
    while i<len(datalist1) and j < len(datalist2):
        if datalist1[i] < datalist2[j]:
            result.append(datalist1[i])
            i+=1
        else:
            result.append(datalist2[j])
            j+=1
    if i< len(datalist1):
        result = result + datalist1[i:len(datalist1)]
    if j< len(datalist2):
        result = result + datalist2[j:len(datalist2)]
    return result



def merge_sort(datalist):
    if len(datalist) == 1:
        return datalist
    mid = int(len(datalist)/2)
    return merge(merge_sort(datalist[0:mid]), merge_sort(datalist[mid:len(datalist)]))



if __name__ == '__main__':
    datalist = [5,3,8,1,-4,0,100,66,32,75]
    print(merge_sort(datalist))




