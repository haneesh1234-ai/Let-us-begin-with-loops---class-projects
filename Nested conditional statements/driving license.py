age = int(input("Enter your age : "))

if age >= 18:

    print("You are eligible for driving license")

    license = input("Do you have license : (y/n)")

    if license=='y':

        print("You have license")

        license_date = input("Is the date is valid y/n : ")

        if license_date=="y":

            print("You are free to go")

        else:

            print("Please renew your driving license")

    else:

            print("You have to apply for a license")

else:

    print("You are not eligible for driving license")