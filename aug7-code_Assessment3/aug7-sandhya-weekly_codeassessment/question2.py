import re,sys,smtplib,logging,csv,json
header=["name","rollno","admno","college","parent_name","mobile_number","emailId","social","english","science","maths","telugu"]
studentlist=[]
def validate(name,rollno,admno,mobile_number,emailId,social,english,science,maths,telugu):
    val1=re.search("[A-Z]{1}[^A-Z]{0,25}$",name)
    val2=re.search("^([0-7]{1,5})$",rollno)
    val3=re.search("^[7-9]{1}[0-9]{9}$",mobile_number)
    val4=re.search("^([0-7]{1,5})$",admno)
    val5=re.search("^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w[2,3]$",emailId)
    sub1=re.search("[0-3]{1}[0-9]{1}|40$",social)
    sub2=re.search("[0-3]{1}[0-9]{1}|40$",english)
    sub3=re.search("[0-3]{1}[0-9]{1}|40$",science)
    sub4=re.search("[0-3]{1}[0-9]{1}|40$",maths)
    sub5=re.search("[0-3]{1}[0-9]{1}|40$",telugu)
    if val1 and val2 and val3 and val4 and val5 and sub1 and sub2 and sub3 and sub4 and sub5:
        return True
    else:
        return False
try:
    class Student:
        def __init__(self,name,rollno,admno,college,parent_name,mobile_number,emailId):
            self.name=name
            self.rollno=rollno
            self.admno=admno
            self.college=college
            self.parent_name=parent_name
            self.mobile_number=mobile_number
            self.emailId=emailId
    class Semresult(Student):
        def __init__(self,name,rollno,admno,college,parent_name,mobile_number,emailId):
            super().__init__(name,rollno,admno,college,parent_name,mobile_number,emailId)

        def marks(self,social,english,science,maths,telugu):
            self.social=social
            self.english=english
            self.science=science
            self.maths=maths 
            self.telugu=telugu
        # super().__init__(name,rollno,admno,college,parent_name,mobile_number,emailId)
        def adddetails(self):
            totalmarks=int(social)+int(english)+int(science)+int(maths)+int(telugu)
            percentage=(totalmarks/200)*100
            total=200
            dict1={"total":total,"percentage":percentage,"totalmarks":totalmarks,'name':name,'rollno':rollno,'admno':admno,'college':college,'parent_name':parent_name,'mobile_number':mobile_number,'emailId':emailId,'social':social,'english':english,'science':science,'maths':maths,'telugu':telugu}
            studentlist.append(dict1)
            print(studentlist)
    while(True):
        print("\n enter your choice")
        print("1.Add student details with marks:")
        print("2.view all the student details with marks:")
        print("3.view all the student details based on the ranking:")
        print("4.send an email to parents:")
        print("5.exit")
        choice=int(input("enter the choice:"))
        if choice==1:
            name=input("Enter the name : ")
            rollno=input("Enter the roll no : ")
            admno=input("Enter the admission no : ")
            college=input("enter the college name :")
            parent_name=input("enter the parent_name : ")
            mobile_number=input("enter the number : ")
            emailId=input("enter the email_id :")
            social=input("Enter the marks of social : ")
            english=input("Enter the marks of english : ")
            science=input("Enter the marks of Science : ")
            maths=input("Enter the marks of maths : ")
            telugu=input("Enter the marks of telugu : ")
        # if validate(name,rollno,admno,mobile_number,emailId,social,english,science,maths,telugu)==True:
            obj1=Semresult(name,rollno,admno,college,parent_name,mobile_number,emailId)
            obj1.marks(social,english,science,maths,telugu)
            obj1.adddetails()
            # studentlist.append(dict1)
            print(studentlist)
        # else:
        #     logging.error("validation error")
        # print(studentlist)
        if choice==2:
            myjson=json.dumps(studentlist)
            with open("Student_api.json","w",encoding="utf-8") as f:
                f.write(myjson)
        if choice==3:
            rank=sorted(studentlist,reverse=True,key=lambda i:i["totalmarks"])
            myjson=json.dumps(rank)
            with open("Studentmarks_api.json","w",encoding="utf-8") as m:
                m.write(myjson)
        if choice==4:
            for i in studentlist:
                if i['totalmarks']<int(i['total']*0.5):
                    message=str(i)
                    connection=smtplib.SMTP("smtp.gmail.com",587)
                    connection.starttls()
                    connection.login("practicedigital12@gmail.com","sandhya9@9")
                    connection.sendmail("sandhyakopparla24@gmail.com",i["emailId"],message)
                    connection.quit
                    print("Mail sent")
                    print("Done!")
        if choice==5:
            break
except Exception:
    logging.error("Something went wrong")
else:
    print("Your program completed Successfuly")
finally:
    print("Thank you!!")
    
        





        
