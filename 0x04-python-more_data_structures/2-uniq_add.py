#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    sum = 0
    for num in my_list:
        if num not in my_list:
            sum += num
            new_list.append(num)
        returm sum
