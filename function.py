
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(5))    

x = 10
def outer():
    x=5
    print('x =', x)

outer()
print('outisde function x =', x)    


# def calculate(num1, num2, operation):
#     num1 = float(num1)
#     num2 = float(num2)

#     expression = f"{num1} {operation} {num2}"
#     result = eval(expression)
#     return result

# # print('Enter the first number: ')
# # num1 = float(input())
# # print('Enter the operation: ')
# # operation = input()
# # print('Enter the second number: ')
# # num2 = float(input())

# # result  = calculate(num1 =10, num2 =20, operation = '+')
# # print(result)

# def add_numbers(*numbers):
#     total = sum(numbers)
#     print(total)

# add_numbers(1,2,3)  


# def info(**kwargs):
#     for key, value in kwargs.items():
#         print(f'{key} : {value}')

# info(name = 'John', age = 22, country = 'USA')        

# square = lambda x,y: x**y
# print(square(5,10))

# def outer_function():
#     message = 'Hi'

#     def inner_function():
#         print(message)
#     return inner_function 
# outer_function()()