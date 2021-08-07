import json,csv
import smtplib
import re,logging
#Baseclass
try:
    class Student:
        def _init_(self,name,rollno,admno,college,parentname,mobilenumber,emailid):
            self.name=''
            self.rollno=''
            self.admno=''
            self.college=''
            self.parentname=''
            self.mobilenumber=''
            self.emaid=''
        def SetData(self,name,rollno,admno,college,parentname,mobilenumber,emailid):
            self.name=name
            self.rollno=rollno
            self.admno=admno
            self.college=college
            self.parentname=parentname
            self.mobilenumber=mobilenumber
            self.emailid=emailid
        def getName(self):
            return self.name
        def getRollNo(self):
            return self.rollno
        def getadmno(self):
            return self.admno
        def getcollege(self):
            return self.college
        def getparentname(self):
            return self.parentname
        def getmobilenumber(self):
            return self.mobilenumber
        def getemailid(self):
            return self.emailid
#Derived class
    class Sem1Results(Student):
        def _init_(self,sub1mark,sub2mark,sub3mark,sub4mark,sub5mark):
            self.sub1mark=''
            self.sub2mark=''
            self.sub3mark=''
            self.sub4mark=''
            self.sub5mark=''
        def SetData2(self,sub1mark,sub2mark,sub3mark,sub4mark,sub5mark): 
            self.sub1mark=sub1mark
            self.sub2mark=sub2mark
            self.sub3mark=sub3mark
            self.sub4mark=sub4mark
            self.sub5mark=sub5mark
        def getsub1mark(self):
            return self.sub1mark
        def getsub2mark(self):
            return self.sub2mark
        def getsub3mark(self):
            return self.sub3mark
        def getsub4mark(self):
            return self.sub4mark
        def getsub5mark(self):
            return self.sub5mark
    def validate(name,college,parentname,emailid,sub1mark,sub2mark,sub3mark,sub4mark,sub5mark): #validation
        valname=re.search("[A-Z]{1}[^A-Z]{0,25}$",name)
        valcollege=re.search("[A-Z]{1}[^A-Z]{0,25}$",college) 
        valparentname=re.search("[A-Z]{1}[^A-Z]{0,25}$",parentname)
        valemail=re.match("^\w+[\._]?\w+[@]\w+[.]\w{2,3}$",emailid)
        valsub1mark=re.search("[0-3]{1}[0-9]{1}|40$",sub1mark)
        valsub2mark=re.search("[0-3]{1}[0-9]{1}|40$",sub2mark)
        valsub3mark=re.search("[0-3]{1}[0-9]{1}|40$",sub3mark)
        valsub4mark=re.search("[0-3]{1}[0-9]{1}|40$",sub4mark)
        valsub5mark=re.search("[0-3]{1}[0-9]{1}|40$",sub5mark)
        if valname and valcollege and valparentname and valemail and valsub1mark and valsub2mark and valsub3mark and valsub4mark and valsub5mark:
            return True
        else:
            return False
        
    student_list=[]
    hilist=[]
    list1=[]
    dict1={}
    email_list=[]
    name1=[]
    obj1=Sem1Results()
    if(__name__=="__main__"):
        while True:
            print("Please Enter your choice")
            print("1.Add student details with marks")
            print("2.Generate json file and display the api to view all the details with marks")
            print("3.Generate json file and display the api to view all the details based on ranking")
            print("4.Send an email to all the parents if the total percentage of marks less than 50%")
            print("5 OOPs do you want to Exit the press 5")
            choice=int(input("Enter your choice : "))
            if choice==1:
                name=input("Enter the name : ")
                rollno=int(input("Enter the roll no : "))
                admno=int(input("Enter the admission no : "))
                college=input("Enter the college name:")
                parentname=input("Enter the parent name:")
                mobilenumber=int(input("Enter the mobilenumber:"))
                emailid=input("Enter email id:")
                sub1mark=input("Enter the marks of sub1mark : ")
                sub2mark=input("Enter the marks of sub2mark : ")
                sub3mark=input("Enter the marks of sub3mark : ")
                sub4mark=input("Enter the marks of sub4mark : ")
                sub5mark=input("Enter the marks of sub5mark : ")
                obj1.SetData(name,rollno,admno,college,parentname,mobilenumber,emailid)
                obj1.SetData2(sub1mark,sub2mark,sub3mark,sub4mark,sub5mark)
                a=validate(name,college,parentname,emailid,sub1mark,sub2mark,sub3mark,sub4mark,sub5mark)
                if a:
                    totalmarks=int(obj1.getsub1mark())+int(obj1.getsub2mark())+int(obj1.getsub3mark())+int(obj1.getsub4mark())+int(obj1.getsub5mark())
                    percentage=(totalmarks/200)*100
                    dict1={"total":totalmarks,"percentage":percentage,"name":obj1.getName(),"rollno":obj1.getRollNo(),"admin":obj1.getadmno(),"college":obj1.getcollege(),"parentname":obj1.getparentname(),"mobilenumber":obj1.getmobilenumber(),"emailid":obj1.getemailid(),"sub1mark":obj1.getsub1mark(),"sub2mark":obj1.getsub2mark(),"sub3mark":obj1.getsub3mark(),"sub4mark":obj1.getsub4mark(),"sub5mark":obj1.getsub5mark()} 
                    student_list.append(dict1) 
                else:
                    logging.error("Invalid input try again")
            if choice==2:
                print(json.dumps(student_list))
                myjson=json.dumps(student_list)
                with open("student.json","w+",encoding="utf-8")as s:
                    s.write(myjson)
            if choice==3:
                hilist=sorted(student_list,key=lambda i:i["total"],reverse=True)
                print(json.dumps(hilist))
                myjson=json.dumps(hilist) 
                with open("ranking.json","w+",encoding="utf-8")as s:
                    s.write(myjson)
            if choice==4:
                list1=list(filter(lambda i:i["percentage"]<50,student_list))
                message="Your son/daughter is scoring very less pls do keep on eye on that"
                print(list1)
                for i in list1:
                    email=i['emailid']
                    email_list.append(email)
                    name=i['name']
                    name1.append(name)
                for i in email_list:
                    print(i)
                    connection=smtplib.SMTP("smtp.gmail.com",587)
                    connection.starttls()
                    connection.login("kanchu954@gmail.com","Kanchu@8+")
                    connection.sendmail("kanchu954@gmail.com",i,message)
                
                for i in name1:
                    print("Email for parent of",i,"is successfully sent")
                connection.quit()
                break
            if choice==5:
                break
            
            
except:
    logging.error("unable to connect")