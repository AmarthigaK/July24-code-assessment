import csv,re,logging,json,collections,smtplib
#from validate import validatemarks
studentslist=[]
dict1={}
try:
    def validatestudents(name,rollno,admino,college,parentname,mobilenumber,email):
        valname=re.search("^[A-Z]{1}[a-z]{0,25}$",name)
        valroll=re.search("^[0-9]{0,4}$",rollno)
        valadmino=re.search("^[0-9]{0,5}$",admino)
        valcollege=re.search("^[A-Z]{1}[a-z]{0,25}$",college)
        valemail=re.search("[A-Za-z0-9]{0,20}@[a-z]+\.[a-z]{2,4}$",email)
        valnumber=re.search("^(\+91)[6-9]\d{9}$",mobilenumber)
        valparentname=re.search("^[A-Z]{1}[a-z]{0,25}$",parentname)
        if valname and valemail and valparentname and valnumber and valadmino and valroll and valcollege:
            print("your Details are valid")
            logging.info("Your data are valid ",name,mobilenumber,parentname,admino,rollno,college,email)
            return True
    def validatemarks(sub1mark,sub2mark,sub3mark,sub4mark,sub5mark):
        return True

    headerContent=["name","rollno","admin","college","parentname","mobilenumber","emailid","sub1mark","sub2mark","sub3mark","sub4mark","sub5mark"]
    class StudentDetails:
        def addstudent(self,name,rollno,admno,college,parentname,mobilenumber,emailid):
            if validatestudents(name,rollno,admno,college,parentname,mobilenumber,emailid)==True:
                dict1={"name":name,"rollno":rollno,"admno":admno,"college":college,
                "parentname":parentname,"mobilenumber":mobilenumber,"emailid":emailid}
                return dict1
    class sem1Result(StudentDetails):
         def addmarks(self,sub1mark,sub2mark,sub3mark,sub4mark,sub5mark):
            if validatemarks(sub1mark,sub2mark,sub3mark,sub4mark,sub5mark)==True:
                total=sub1mark+sub2mark+sub3mark+sub4mark+sub5mark
                dict2={"total":total,"sub1mark":sub1mark,"sub2mark":sub2mark,"sub3mark":sub3mark,"sub4mark":sub4mark,"sub5mark":sub5mark}   
                return dict2
    obj1=sem1Result()
    while(True):
        print("1)enter students between [0-40] : ")
        print("2)Display students like API: ")
        print("3)Ranking: ")
        print("4)send email to the students whose scores are less than 50%")
        print("5)exit")
        choice=int(input("Enter your choice : "))
        if choice==1:
            name=input("Enter the Student name : ")
            rollno=input("Enter your rollno : ")
            admno=input("Enter your admino : ")
            college=input("Enter your college : ")
            parentname=input("Enter your parentname : ")
            mobilenumber=input("Enter your mobilenumber : ")
            emailid=input("Enter your Science emailid: ")
            sub1mark=int(input("Enter your Sub1Marks : "))
            sub2mark=int(input("Enter your Sub2Marks : "))
            sub3mark=int(input("Enter your Sub3Marks : "))
            sub4mark=int(input("Enter your Sub4Marks : "))
            sub5mark=int(input("Enter your Sub5Marks : "))
            obj1=sem1Result()
            a=obj1.addstudent(name,rollno,admno,college,parentname,mobilenumber,emailid)
            b=obj1.addmarks(sub1mark,sub2mark,sub3mark,sub4mark,sub5mark)
            a.update(b)
            studentslist.append(a)
            print(studentslist)
        if choice==2:
            studentsapi=json.dumps(studentslist)
            with open('Studentdetails.json','w+',encoding="utf-8") as f1:
                f1.write(studentsapi)
        if choice==3:
            studentslist=sorted(studentslist,key=lambda i:i['total'],reverse=True)
            studentsapi=json.dumps(studentslist)
            with open('StudentdetailsRanking.json','w+',encoding="utf-8") as f1:
                f1.write(studentsapi)
        if choice==4:
            for i in studentslist:
                if i['total']<100:
                    message=str(i)
                    connection=smtplib.SMTP("smtp.gmail.com",587)
                    connection.starttls()
                    connection.login("sindhubarathipython@gmail.com","984621@ss")
                    connection.sendmail("sindhubarathipython@gmail.com",i['emailid'],message)
                    connection.quit
                    print("Mail sent")
except Exception:
    logging.error("Something Went Wrong!")
finally:
    print("code completed successfully")