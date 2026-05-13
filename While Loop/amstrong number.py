# Find the number of 3 digits is armstrong or not

number = int(input("Enter 3 digit number : "))

sum = 0

i = number

while i > 0:

    digit = i % 10

    sum = sum + digit ** 3

    i = i // 10

if number == sum:

    print(number, "is an armstrong number")

else:

    print(number, "is not an armstrong number")