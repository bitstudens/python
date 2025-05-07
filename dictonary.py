# # my_dict = {
# #     "key":"value1",
# #     "key2":"value",
# #     "key2":"value",
# #     "fruits": ["apple","orange","whatever"]
# #     }

# my_dict = dict(key="value",key2="value2")

# # if "key4" in my_dict:
# #     print("exists")
# # print(my_dict.items())
# my_dict["key"] = "Nepal"
# # my_dict.update({"dictrict":"Bara"})
# # my_dict.pop("key")
# # my_dict.popitem()
# # del my_dict["key"]
# # print(my_dict)

# # for x in my_dict.items():
# #     print(x)

# my_dict1 = dict(my_dict)
# print(my_dict1)

students = {
    "101" : {"name":"Alice","age":30,"grade":"A"},
    "102" : {"name":"John","age":20,"grade":"B"},
    "103" : {"name":"Doe","age":10,"grade":"C"}
}

print(students["102"]["name"])

students["new_id"] = {"name":"Puja","age":14,"grade":"D"}

# print(students)

# for student_id, info in students.items():
#     print(f"ID:{student_id}")
#     for key,value in info.items():
#         print(f"{key} :{value}") 

##Studnt MGMT 
# - Add student
# - Display student
# - search by Id
# update student info
# delete student        

student  =  {
    "name":"whatever",
    "grades":[85,99,100]
}

print(student["grades"][1])

datas = [
    {"name" :"John"},
    {"name" :"Doe"}
]

print(datas[0]["name"])

inventory = {
    "item_id":{
        "name":"Item Name",
        "price":float,
        "quantity": int
    }
}