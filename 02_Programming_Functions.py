# 1 Mapping Functions
# numbers = [n for n in  range(1,101)]
# print(numbers)
# def power(number):
#     return number*number

# power_of_number_in_list = map(power,numbers)

# print(list(power_of_number_in_list))
# ----------------------------------------------
# 2 Filter Function
# numbers = [n for n in  range(1,101)]
# def my_filter(n):
#     return n>50

# filter1 = filter(my_filter,numbers)
# print(list(filter1))
# -----------------------------------------------
# 3 reduce function
# from functools import reduce
# numbers = [n for n in  range(1,101)]

# def sum_num(x,y):
#     return x+y

# sum_numbers = reduce(sum_num,numbers)
# print(sum_numbers)
# ------------------------------------------------
# # unpacking
# a,*b = [1,2,3,4,5,6,7,9,8]
# print(a)
# print(b)
