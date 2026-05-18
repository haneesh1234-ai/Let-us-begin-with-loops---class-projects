# Write a program to print all the prime numbers which come in the range entered by the user?
# take two input from user
lower = int(input("enter a starting range of number: "))
upper = int(input("enter a ending range of number : "))
print("Prime numbers between", lower, "and", upper, "are:")
# iterate loop from lower limit to upper limit
for num in range(lower, upper + 1):

# all prime numbers are greater than 1

    if num > 1:

        for i in range(2, num):

            if (num % i) == 0:

                break

        else:

            print(num)