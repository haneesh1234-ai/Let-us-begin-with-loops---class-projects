#Exam Eligibility Check
attendence = int(input("enter your attendence percentagea : "))
 
if attendence >=75 :
    print("you are eligibill for exam ")
    med = input("do you have medeical certificate y/n : ")
    if med=="y":
        print("you are allowed to write the exam")
    else :
        print("your are not allowed to write the exam")
else :
    print("you are not eligibill for exam ")

