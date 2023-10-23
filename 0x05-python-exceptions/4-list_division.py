#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    newlist = []
    for i in range(list_length):
        try:
            a = my_list_1[i]
            b = my_list_2[i]
            div = a / b
            newlist.append(div)
        except IndexError:
            print("out of range")
            newlist.append(0) 
        except TypeError:
            print("wrong type")
            newlist.append(0) 
        except ZeroDivisionError:
            print("division by 0")
            newlist.append(0) 
    return(newlist)

