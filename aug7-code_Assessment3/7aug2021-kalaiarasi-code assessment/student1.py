import re
import logging
import json 
import smtplib
try:

    studentlist=[]
    def validation(name,emailid,mobilenum,sub1,sub2,sub3,sub4,sub5):
        vname=re.search("^[A-Za-z]{2,25}$",name)
        vmail=re.search("^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$",emailid)
        vmob=re.search("^(\+91)?[0]?(91)?[6-9]\d{9}$",mobilenum)
        m1=re.search("^(40|[0-4][0-9]?)$",sub1)
        m2=re.search("^(40|[0-4][0-9]?)$",sub1)
        m3=re.search("^(40|[0-4][0-9]?)$",sub1)
        m4=re.search("^(40|[0-4][0-9]?)$",sub1)
        m5=re.search("^(40|[0-4][0-9]?)$",sub1)
        if vname and vmail and vmob and m1 and m2 and m3 and m4 and m5:
            return True
        else:
            return False
    class Studentdetail:
        def __init__(self):
            name=''
            rollno=''
            admin=''
            college=''
            parentname=''
            mobilenum=''
            emailid=''
        def addstudentdetail(self,name,rollno,admin,college,parentname,mobilenum,emailid):
            name="name"
            rollno="rollno"
            admin="admin"
            college="college"
            parentname="parentname"
            mobilenum="mobilenum"
            emailid="emailid"
            return self.addstudentdetail
    class Marks(Studentdetail):
        def __init__(self):
            sub1=''
            sub2=''
            sub3=''
            sub4=''
            sub5=''
        def addmarks(self,sub1,sub2,sub3,sub4,sub5):
            sub1="sub1"
            sub2="sub2"
            sub3="sub3"
            sub4="sub4"
            sub5="sub5"
        
            return self.addmarks

    obj=Marks()
    if(__name__=='__main__'):
        while(True):
            print("1. add student")
            print("2. generate json file & display student detail api")
            print("3. generate json file & display student detail based on ranking")
            print("4. send less than 50% to email ")
            print("5. exit")

            choice=int(input("enter ur choice:"))
            
            if choice==1:
                name=input("enter your name:")
                rollno=int(input("enter your rollno:"))
                admin=int(input("enter your admin:"))
                college=input("enter your college:")
                parentname=input("enter your parentname:")
                mobilenum=input("enter your mobilenum:")
                emailid=input("enter your emailid:")
                
                sub1=input("enter your sub1:")
                sub2=input("enter your sub2:")
                sub3=input("enter your sub3:")
                sub4=input("enter your sub4:")
                sub5=input("enter your sub5:")
                
                
                
                totalmarks=int(sub1)+int(sub2)+int(sub3)+int(sub4)+int(sub5)
                
                x=validation(name,emailid,mobilenum,sub1,sub2,sub3,sub4,sub5)
                if x:
                    obj.addstudentdetail(name,rollno,admin,college,parentname,mobilenum,emailid)
                    obj.addmarks(sub1,sub2,sub3,sub4,sub5)
                    dict1={"totalmarks":totalmarks,"name":name,"rollno":rollno,"admin":admin,"college":college,"parentname":parentname,"mobilenum":mobilenum,"emailid":emailid,"sub1":sub1,"sub2":sub2,"sub3":sub3,"sub4":sub4,"sub5":sub5}
                    studentlist.append(dict1)
                    print(studentlist)


                else:
                    logging.error("please enter valid data!")
            if choice==2:
                print(studentlist)
                myjsondata=json.dumps(studentlist)
                with open('studentfile1.json','w+',encoding='Utf-8') as t:
                    t.write(myjsondata)

            
            if choice==3:
                x=(sorted(studentlist,key=lambda i:i["totalmarks"],reverse=True))
                print(x)
                myjsondata=json.dumps(x)
                with open('studentfile1.json','w+',encoding='Utf-8') as t:
                    t.write(myjsondata)
                    
                
            if choice==4:
            
                for i in studentlist:
                    if i["totalmarks"]<100:
                    
                        connection =smtplib.SMTP("smtp.gmail.com",587)
                        connection.starttls()
                        connection.login("kalai.iprimed@gmail.com","Kalai@2404")
                        message="hi! your son/daughter got low mark in semester exam"
                        print(message)
                        connection.sendmail("kalai.iprimed@gmail.com",i["emailid"],message)
                        print("email send")
                        connection.quit()
                    
            if choice==5:
                break
                                
except:
    logging.error("please enter correct data")

