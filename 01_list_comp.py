# 1)this case for list comprehensions
# numbers = [1,2,3,4,5,6,7,8,9,10]

# new_numbers = [n*n for n in numbers]
# print(new_numbers)

# numbers = [1,2,30,50,51,35,43,100,101,106]

# # new_numbers = [n for n in numbers if n%2==0]
# # print(new_numbers)

# new_numbers = [True if n%2==0 else False for n in numbers ]
# print(new_numbers)

# new_numbers = [x**2 for x in numbers]
# print(new_numbers)
# new_numbers = [x**2 for x in range(20)]
# print(new_numbers)


# words = ['ahmed','ali','asmaa','omar','rami']
# # words = [word.upper() for word in words]
# # print(words)
# words = [word.upper() if word.startswith('a') else word for word in words ]
# print(words)
# words = [word.upper() for word in words if word.startswith('a') ]

# ------------------------------------------------------------------
# 2 Generators
numbers = [1,2,3,4,5,6,7,8,9,10]

new_numbers = (n*n for n in numbers)
print(new_numbers)
# in this case when we print it returns <generator object <genexpr> at 0x0000021ADADD9220>
# to call it should convert to list
print(list(new_numbers)) 
