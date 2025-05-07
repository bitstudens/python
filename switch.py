print('Calculator')
print("Operations: +, -, *, /, %,**")

while True:
    print('Enter the first number: ')
    num1 = float(input())
    print('Enter the operation: ')
    operation = input()
    print('Enter the second number: ')
    num2 = float(input())
    match operation:
        case '+':
            print(num1 + num2)    
        case '-':
            print(num1 - num2)
        case '*':
            print(num1 * num2)
        case '/':
            if(num2 == 0):
                print('Division by zero is not allowed')
                continue
            print(num1 / num2)
        case '%':
            print(num1 % num2)
        case '**':
            print(num1 ** num2)
        case _:
            print('Invalid operation')
            continue
    cont =  input('Do you want to continue? (y/n): ')
    if cont != 'y':
        print('Goodbye')
        break    