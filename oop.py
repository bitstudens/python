# #class #object
# class Person:
    
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
        
#     def greet(self):
#         print(f"Hello, Name is {self.name} and age is {self.age}")

# person = Person('Alice',30)
# another_persion =  Person('Bob', 40)

# person.greet()
# another_persion.greet()




# class BankAccount:
    
#     def __init__(self, account_number, balance=0):
#         self.account_number = account_number
#         self.balance = balance
        
#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Deposited {amount}. New balance is {self.balance}")
        
#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficient funds")
#         else:
#             self.balance -= amount
#             print(f"Withdrew {amount}. New balance is {self.balance}")


# account = BankAccount("123456789", 1000)
# account.deposit(500)
# account.withdraw(200)

# class Animal:
    
#     def speak(self):
#         print("Animal speaks")

#     def walk(self):
#         print("Animal walks")    

# class Dog(Animal):
#     def speak(self):
#         print("The Dog barks")   

#enmcapsulation
#inheritance
#polymorphism
#abstraction

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def get_name(self):
#         return self.__name
    
#     def make_sound(self):
#        print(f"{self.name} makes a sound")


# class Dog(Animal):
#     def make_sound(self):
#         print(f"{self.name} barks")


# class Cat(Animal):
#     def make_sound(self):
#         print(f"{self.name} meows")

# dog = Dog("Buddy")
# cat = Cat("Whiskers")
# dog.make_sound()  # Output: Buddy barks
# cat.make_sound()  # Output: Whiskers meows
# dog.get_name()  # Output: Buddy
# dog.__name = "Max"  # This will not change the name   



# from abc import ABC, abstractmethod
# class Animal(ABC):
#     def __init__(self,name):
#         self.__name = name

#     def get_name(self):
#         return self.__name

#     @abstractmethod
#     def make_sound(self):
#         pass

# class Dog(Animal):
#     def make_sound(self):
#         print(f"{self.get_name()} barks")   

# class Cat(Animal):
#     def make_sound(self):
#         print(f"{self.get_name()} meows")             


# a = Animal("Generic Animal")  
# dog = Dog("Buddy")



class Car:
    def start_engine(self):
        print("Engine started")
    def drive(self):
        print("Car is driving")


car = Car()
car.start_engine()
car.drive() 


from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def drive(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")

    def drive(self):
        print("Car is driving")

my_car = Car()
my_car.start_engine()
my_car.drive()  # Output: Car is driving  