# mylst = []
numbers = [1,2,3,4,5,"apple","ornage",3.14, True,3.14,"dates"]
#process 20 line
###

numbers[2] ="Modified"
#another 2-0 line pocss

print(numbers)
numbers.insert(9,"Watermelon")
numbers.insert(10, "dates")
print(numbers)
##
numbers.remove("dates")
numbers.pop()
numbers.pop(1)
del numbers[0]
# numbers.clear()


# print(len(numbers))

# for number in numbers:
#     print(number)

# i=0
# while i < len(numbers):
#     print(numbers[i])
#     i +=1

# print(type(numbers))

# another_list =list(("Abc","CDE",1,2))
# print(another_list[0])

# count = [x for x in range(50)]
# even_numbers = [x for x in range(50) if x%2== 0]
# testData = [4, 3, 5, 2]
# sortedData = sorted(testData)  
# print(sortedData)

# To do list 
#input 
# add in the list 
# to do 


todo_list = []

def add_task():
    task = input("Enter task to add").strip()
    if task:
        todo_list.append(task)
    else:
        print("Task cannot be empty")

def remove_task():
    if not todo_list:
        print("Nothing to remove")
        return
    view_task()
    try:
        task_num = int(input("Enter task no to remove"))
        if(1<= task_num <= len(todo_list)):
            remove_task = todo_list.pop(task_num -1)
            print(f'Rmoved task:" "{remove_task}"')
        else:
            print("invalid task number")
    except ValueError:
        print("Please enter a valid number")            

def view_task():
    if not todo_list:
        print("No task in the list")
    else:
        print("\n To do List:")
        # for task in todo_list:
        #     print(task)
        for i, task in enumerate(todo_list,1):
            print(f"{i}. {task}")
        print()

def main():
    while True:
        print("\n **** To do list ***")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Task")
        print("4. Exit")

        choice  = input("Choose an option 1 -4"). strip()

        if choice == "1":
            add_task()
        elif choice =="2":
            remove_task()
        elif choice =="3":
            view_task()
        elif choice =="4":
            print("Ok then Bye")
            break            
        else:
            print("Invalid choice, Try again")

if __name__ == "__main__":
    main()