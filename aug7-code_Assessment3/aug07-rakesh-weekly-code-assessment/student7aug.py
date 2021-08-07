import re,logging,json,csv,smtplib
std=[]
total=0
try:
    header=["total","studentname","rollno","admno","college","parentname","mobileno","mailid","sub1","sub2","sub3","sub4","sub5"]
    def validate(studentname,rollno,admno,college,parentname,mobileno,mailid):
        valstudentname=re.search("[A-Z]{1}[^A-Z]{0,25}$",studentname)
        valrollno=re.search("^([0-7]{1,5})$",rollno)
        valadmno=re.search("^([0-7]{1,5})$",admno)
        valmobileno=re.search("^[7-9][0-9]{9}$",mobileno)
        valmailid=re.search("^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$",mailid)
        valcollege=re.search("[A-Z]{1}[^A-Za-z]{0,100}$",college)
        valparentname=re.search("[A-Z]{1}[^A-Za-z]{0,100}$",parentname)
        valsub1=re.search("[0-3]{1}[0-9]{1}|40$",sub1)
        valsub2=re.search("[0-3]{1}[0-9]{1}|40$",sub2)
        valsub3=re.search("[0-3]{1}[0-9]{1}|40$",sub3)
        valsub4=re.search("[0-3]{1}[0-9]{1}|40$",sub4)
        valsub5=re.search("[0-3]{1}[0-9]{1}|40$",sub5)
        if valstudentname and valrollno and valadmno and valcollege and valparentname and valmobileno and valmailid and valsub1 and valsub2 and valsub3 and valsub4 and valsub5:
            return True
        else:
            return False    
    class Student:
        def init(self,studentname,rollno,admno,college,parentname,mobileno,mailid):
            self.studentname=studentname
            self.rollno=rollno
            self.admno=admno
            self.college=college
            self.parentname=parentname
            self.mobileno=mobileno
            self.mailid=mailid  
        def addstudent(self,studentname,rollno,admno,college,parentname,mobileno,mailid):
            self.studentname=studentname
            self.rollno=rollno
            self.admno=admno
            self.college=college
            self.parentname=parentname
            self.mobileno=mobileno
            self.mailid=mailid
        def getName(self,studentname):
            return self.studentname
        def getRoll(self,rollno):
            return self.rollno
        def getAdmno(self,admnno):
            return self.admno
        def getCollege(self,college):
            return self.college
        def getPname(self,parentname):
            return self.parentname
        def getMno(self,mobileno):
            return self.mobileno
        def getMid(self,mailid):
            return self.mailid  
    class sem1Result(Student):
        def init(self,sub1,sub2,sub3,sub4,sub5):
            self.sub1=sub1
            self.sub2=sub2
            self.sub3=sub3
            self.sub4=sub4
            self.sub5=sub5
        def addmarks(self,sub1,sub2,sub3,sub4,sub5):
            self.sub1=sub1
            self.sub2=sub2
            self.sub3=sub3
            self.sub4=sub4
            self.sub5=sub5 
        def get1(self,sub1):
            return self.sub1
        def get2(self,sub2):
            return self.sub2
        def get3(self,sub3):
            return self.sub3
        def get4(self,sub4):
            return self.sub4
        def get5(self,sub5):
            return self.sub5 
    obj=sem1Result() 
    if(__name__=="__main__"):
        while True:
            print("1. Add Student details with marks")
            print("2. Generate JSON file and display the API to view all student details with marks ")
            print("3. Generate JSON file and display the API to view all student details based on ranking ")
            print("4. Send an email to all the parents if the total percentage of marks is less than 50")
            print("5. Exit")
            choice=int(input("Select your operation : ")) 
            if choice==1:
                studentname=input("Enter the Student name : ")
                rollno=input("Enter the Student rollno : ")
                admno=input("Enter the Student admno : ")
                parentname=input("Enter the Student Parent name : ")
                college=input("Enter the Student college : ")
                mobileno=input("Enter the Student Mobile no : ")
                mailid=input("Enter the Mail ID : ")
                sub1=input("Enter the marks of sub 1= ")
                sub2=input("Enter the marks of sub 2= ")
                sub3=input("Enter the marks of sub 3= ")
                sub4=input("Enter the marks of sub 4= ")
                sub5=input("Enter the marks of sub 5= ")
                if validate(studentname,rollno,admno,college,parentname,mobileno,mailid)==True:
                    obj.addstudent(studentname,rollno,admno,college,parentname,mobileno,mailid)
                    obj.addmarks(sub1,sub2,sub3,sub4,sub5)
                    total=int(obj.get1(sub1))+int(obj.get2(sub2))+int(obj.get3(sub3))+int(obj.get4(sub4))+int(obj.get5(sub5))
                    dict1={"total":total,'studentname':obj.getName(studentname),"rollno":obj.getRoll(rollno),"admno":obj.getAdmno(admno),"college":obj.getCollege(college),"parentname":obj.getPname(parentname),"mobileno":obj.getMno(mobileno),"mailid":obj.getMid(mailid),"sub1":obj.get1(sub1),"sub2":obj.get2(sub2),"sub3":obj.get3(sub3),"sub4":obj.get4(sub4),"sub5":obj.get5(sub5)}
                    std.append(dict1)
                    print(std)
                else:
                    logging.error("Validation error")    
            if choice==2:
                myjsondata=json.dumps(std)
                print(myjsondata)
                with open("studentmark.json","w",encoding="UTF8") as f:
                    f.write(myjsondata)        
            if choice==3:
                sjson=json.dumps(std)
                print(json)
                with open("studentrank.json","w",encoding="UTF8") as f:
                    f.write(sjson)        
            if choice==4:  
                for i in std:
                    if i["total"]<100:
                        msg="Total marks of student is below 50%, out of 200  : " + str(total)
                        connection=smtplib.SMTP("smtp.gmail.com",587)
                        connection.starttls()
                        connection.login("rakesh.learning.python@gmail.com","9008496668Ra@")
                        connection.sendmail("rakesh.learning.python@gmail.com",i["mailid"],msg)
                        print("EMAIL SENT")
                        connection.quit()
            if choice==5:
                break         
except:
    logging.error("OOPS!....SOMETHING WENT WRONG ")
finally:
    print("Thank you")               