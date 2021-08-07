import json,smtplib,re,logging
slist=[]
class Student:
    def addStudent(self,name,roll,admNo,college,parentName,mobileNumber,emailId):
        self.name=name
        self.roll=roll
        self.admNo=admNo
        self.college=college
        self.parentName=parentName
        self.mobileNumber=mobileNumber
        self.emailId=emailId
        stud1=[self.name,self.roll,self.admNo,self.college,self.parentName,self.mobileNumber,self.emailId]
        return stud1
class Sem1Result(Student):
    def addStudentResult(self,sub1,sub2,sub3,sub4,sub5):
        self.sub1=sub1
        self.sub2=sub2
        self.sub3=sub3
        self.sub4=sub4
        self.sub5=sub5
        stud2=[self.sub1,self.sub2,self.sub3,self.sub4,self.sub5]
        return stud2
k=Sem1Result()
def validate(name,roll,mobileNumber,emailId,sub1,sub2,sub3,sub4,sub5):
        name1=re.search("[A-Za-z]{0,25}$",name)
        print(name1)
        roll1=re.search("[0-9]{0,7}$",roll)
        print(roll1)
        mobileNumber1=re.search("[6-9]\d{9}$",mobileNumber)
        print(mobileNumber1)
        emailId1=re.search("[A-Za-z0-9]{0,20}@[a-z]+\.[a-z]{2,4}$",emailId)
        print(emailId1)
        submark1=re.search("[0-3]{1}[0-9]{1}|40$",sub1)
        print(submark1)
        submark2=re.search("[0-3]{1}[0-9]{1}|40$",sub2)
        print(submark2)
        submark3=re.search("[0-3]{1}[0-9]{1}|40$",sub3)
        print(submark3)
        submark4=re.search("[0-3]{1}[0-9]{1}|40$",sub4)
        print(submark4)
        submark5=re.search("[0-3]{1}[0-9]{1}|40$",sub5)
        print(submark5)
        if name1 and roll1 and mobileNumber1 and emailId1 and submark1 and submark2 and submark3 and submark4 and submark5 :
            return True
        else:
            return False
try:
    if __name__ == "__main__":
        while(True):
            print("1.Add Student with Mark")
            print("2.View all student details with marks using JSON File")
            print("3.View all student details based on Ranking using JSON File")
            print("4.Send an email to all parents less than 50% mark")
            print("5.Exit")
            choice=int(input("Enter your choice :"))
            if choice==1:
                name = input("Enter the name of student: ")
                roll=input("Ënter the RollNo of student:")
                admNo=input("Enter the admno of Student:")
                college=input("Enter the college of student:")
                parentName=input("Enter the parent name:")
                mobileNumber=input("Enter the mobilenumber:")
                emailId=input("Enter the email:")
                sub1=input("Enter the sub1 mark:")
                sub2=input("Enter the sub2 mark:")
                sub3=input("Enter the sub3 mark:")
                sub4=input("Enter the sub4 mark:")
                sub5=input("Enter the sub5 mark:")
                total=int(sub1)+ int(sub2)+int(sub3)+int(sub4)+int(sub5)
                if validate(name,roll,mobileNumber,emailId,sub1,sub2,sub3,sub4,sub5)==True:
                    print(1)
                    u=k.addStudent(name,roll,admNo,college,parentName,mobileNumber,emailId)
                    di1={'totalmarks':total}
                    print(di1)
                    v=k.addStudentResult(sub1,sub2,sub3,sub4,sub5)
                    student=["name","roll","admNo","college","parentName","mobileNumber","emailId"]
                    marks=["sub1","sub2","sub3","sub4","sub5"]
                    for i in range(len(u)):
                        di1[student[i]]=u[i]
                    for j in range(len(v)):
                        di1[marks[j]]=v[j]
                    slist.append(di1)
                    print(slist)
                else:
                    logging.error("wrong")
            
            
            
            if choice==2:
                jsondata=json.dumps(slist)
                with open("mstud.json","w+",encoding="utf-8") as s1:
                    s1.write(jsondata)

            if choice==3:
                data1=(sorted(slist,key=lambda i:i["totalmarks"],reverse=True))
                print(data1)
                jsondata=json.dumps(data1)
                with open("nstud.json","w+",encoding="utf-8") as s2:
                    s2.write(jsondata)

            if choice==4:
                for i in slist:
                    if i['totalmarks']<100:
                        message=str(i)
                        print(message)
                        connection=smtplib.SMTP("smtp.gmail.com",587)
                        connection.starttls()
                        connection.login("Arifkhanstar0786@gmail.com","Absrkhan078621")
                        connection.sendmail("Arifkhanstar0786@gmail.com",i["emailId"],message)
                        connection.quit
                        print("Mail sent successfully")

            if choice==5:
                break
except:
    logging.error("something went wrong")
    print("error") 