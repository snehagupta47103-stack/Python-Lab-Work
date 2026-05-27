# Q-1
number = input("Enter your number : ")

int_value = int(number)
float_value = float(number)
bool_value = bool(number)
str_value = str(number)

print("Integer value :", int_value,  "Type :", type(int_value))
print("Float value :", float_value,  "Type :", type(float_value))
print("Boolean value :", bool_value, "Type :", type(bool_value))
print("String value :", str_value, "Type :", type(str_value))

#Q-2
number = float(input("Enter your number : "))

int_value = int(number)

print("Integer value :", int_value)

#Q-3
value = bool(input("Enter your value : "))

int_value = int(value)
str_value = str(value)

print("Integer value :", int_value)
print("String value :", str_value)

#Q-4
integer = 33
float = 44.55
string = "Python"
boolean = True
list = [1, 2, 3, 4]
tuple = (5, 6, 7, 8)
dictionary = {"name": "Ali", "age": 20}

print(integer,type(integer),id(integer))
print(float,type(float),id(float))
print(string,type(string),id(string))
print(boolean,type(boolean),id(boolean))
print(list,type(list),id(list))
print(tuple,type(tuple),id(tuple))
print(dictionary,type(dictionary),id(dictionary))

#Q-5
number = 44
value = 44

print("number:",number , "-->", " " "Memory Address:",id(number))
print("value:",value , "-->", " "  "Memory Address:",id(value))

print("-----------")

number = 44
value = 47

print("Modified number and value")
print("number:",number , "-->", " "   "Memory Address:",id(number))
print("value:",value , "-->", " "   "Memory Address:",id(value))




































