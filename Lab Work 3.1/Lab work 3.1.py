#Q-1
num = int(input("Enter your number: "))

if num %2 == 0:
    print("Even")
else:
    print("Odd")

#Q-2
age = int(input("Enter your age: "))

if age <= 12:
    print("Child")
elif age <= 19:
    print("Teenager")
elif age <= 59:
    print("Adult")
elif age >= 60:
    print("Senior")

#Q-3
num1 = int(input("Enter your number: "))
num2 = int(input("Enter your number: "))
num3 = int(input("Enter your number: "))

if num1 > num2 and num1 > num3:
    print("Largest num is: ", num1)
elif num2 > num1 and num2 > num3:
    print("Largest num is: ", num2)
elif num3 > num1 and num3 > num2:
    print("Largest num is: ", num3)
else:
    print("All are Equal")

#Q-4
num = int(input("Enter your number: "))

if num == 0:
    print("It is an additive neutral number.")
elif num == 1:
    print("It is an multiplicative neutral number.")
else:
    print("It is not a neutral number.")

