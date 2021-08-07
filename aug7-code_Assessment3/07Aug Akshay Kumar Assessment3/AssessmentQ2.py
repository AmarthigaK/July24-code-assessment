import json, smtplib,logging,re
from collections import deque

List = []
mydata = []
data = []

sList = deque(List)
try:
    class Student:
        def __init__(self):
            pass

        def addStudent(self, name, rollno, admno, college, parent, mobno, email):
            dict1 = {"name": name, "rollno": rollno, "admno": admno, "college": college, "parent": parent, "mobno": mobno,
                    "email": email}
            sList.append(dict1)


    class sem1Result(Student):
        def __init__(self):
            pass

        def marks(self, s1marks, s2marks, s3marks, s4marks, s5marks,total):
            dict1 = {"s1marks": s1marks, "s2marks": s2marks, "s3marks": s3marks, "s4marks": s4marks, "s5marks": s5marks,
                    "total": total}
            mydata.append(dict1)
            for x in mydata:
                sList.append(x)
    s1 = sem1Result()

    while(1):
        print("1. Add students details with marks:")
        print("2. Generate JSON file to view all students details with marks")
        print("3. Generate JSON File to view all students based on ranking")
        print("4. Send mail to parents, if marks is less than 50%")
        print("5. Exit")
        choice = int(input("Enter your choice:"))

        if choice == 1:
            name = input("Enter your name:")
            rollno = int(input("Enter your rollno:"))
            admno = int(input("Enter admission no:"))
            college = input("Enter the college name:")
            parent = input("Enter your parents name:")
            mobno = int(input("Enter the mobile no:"))
            email = input("Enter your Email-id:")
            s1marks = int(input("Enter sub1 marks:"))
            s2marks = int(input("Enter sub2 marks:"))
            s3marks = int(input("Enter sub3 marks:"))
            s4marks = int(input("Enter sub4 marks: "))
            s5marks = int(input("Enter sub5 marks:"))
            total = s1marks+s2marks+s3marks+s4marks+s5marks

            s1.addStudent(name, rollno, admno, college, parent, mobno, email)
            s1.marks(s1marks, s2marks, s3marks, s4marks, s5marks,total)
        if choice == 2:
            myjsondata = json.dumps(sList)
            with open('sList.json', 'w', encoding="UTF8") as j:
                j.write(myjsondata)
        if choice == 3:
            data = print(sorted(mydata,key=lambda i:i['total'],reverse=True))
            jsondata=json.dumps(data)

            with open('abc.json','w',encoding="UTF8") as j:
            j.write(jsondata) 

        if choice == 4:
            if total > 100:
                print("Your score is above 50%")
            elif total < 100:
                print("Poor Performance")
                print("Your marks is:", total)
                message = str(total)
                connection = smtplib.SMTP("smtp.gmail.com", 587)
                connection.starttls()
                connection.login("sureshbannur6@gmail.com", "aks@123")
                connection.sendmail("sureshbannur6@gmail.com", "akshaykumarn.012@gmail.com", message)

                print("Email sent successfully")
                connection.quit()
                break  
        if choice == 5:
            break 
except Exception:
    logging.error("Something went wrong. Please try again") 
finally:
    print("Thank You")                      
      


              
   
                 



