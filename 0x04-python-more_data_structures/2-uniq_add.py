#!/usr/bin/python3
def uniq_add(my_list=[]):
    newlst=[]
    sum = 0
    for i in my_list:
        if i not in newlst:
            newlst.append(i)
    for i in newlst:
        sum=sum+i
    return sum
