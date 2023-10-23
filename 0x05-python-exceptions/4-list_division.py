#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    newlist = []
    div = 0
    for i in range(list_length):
        div = 0
        try:
            a = my_list_1[i]
            b = my_list_2[i]
            div = a / b
        except IndexError:
            print("out of range")
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        finally:
            newlist.append(div)
    return(newlist)

