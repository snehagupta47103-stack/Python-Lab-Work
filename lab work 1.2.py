#Q-2
name = input("Enter your name : ")
age = input("Enter your age : ")
hobby = input("Enter your hobby : ")

print(f"Hello, {name}! At {age}, enjoying {hobby} sounds fun!")

#Q-3
a = 20
b = 45

print("Addition : ",a + b)
print("Subtraction : ",a - b)
print("Multiplication : ",a * b)
print("Division : ",a / b)
print("Floor Division : ",a // b)
print("Modulus : ",a % b)
print("Exponentiation : ",a ** b)

#Q-4
data = 11,22,33,44,55,66        #string
print(type(data))

data = 66        #integer
print(type(data))

data = 55.66        #float
print(type(data))

data = 11+2j       #complex
print(type(data))

data = True        #boolean
print(type(data))

data = False        #boolean
print(type(data))

#Q-5
height = float(input("Enter your height : "))
weight = int(input("Enter your weight : "))

print(f"Your height is {height} and weight is {weight}")


#Q-6
a = input("Enter your number: ")
b = input("Enter your number: ")

a = a == "True"
b = b == "True"

print("a AND b = ",a and b)
print("a OR b = ",a or b)
print("NOT b = ",not b)
print("NOT a = ",not a)


#Q-7
a = 10
print("Initial value of a = ",a)

a += 7
print("After a += 7, a = ",a)

a -= 8
print("After a -= 8, a = ",a)

a *= 5
print("After a *= 5, a = ",a)

a /= 4
print("After a /= 4, a = ",a)



