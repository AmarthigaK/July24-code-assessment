import json,smtplib,re,logging
try:
    studentlist=[]
    class Student:
        def addStudentDetails(self,name,rollno,admno,college,parentname,mobilenumber,emailid):
            self.name='name'
            self.rollno='rollno'
            self.admno='admno'
            self.college='college'
            self.parentname='parentname'
            self.mobilenumber='mobilenumber'
            self.emailid='emailid'
            return self.addStudentDetails
    class Sem1Result(Student):
        def addStudentResult(self,sub1mark,sub2mark,sub3mark,sub4mark,sub5mark):
            self.sub1mark='sub1mark'
            self.sub2mark='sub2mark'
            self.sub3mark='sub3mark'
            self.sub4mark='sub4mark'
            self.sub5mark='sub5mark'
            return self.addStudentResult
    d=Sem1Result()

    def validate(vname,vrollno,vmobilenumber,vemailid,vsub1mark,vsub2mark,vsub3mark,vsub4mark,vsub5mark):
        name1=re.search("^[A-Z]{1}[a-z]{0,25}$",vname)
        print(name1)
        rollno1=re.search("^[0-9]{0,7}$",vrollno)
        print(rollno1)
        mobilenumber1=re.search("^91[6-9]\d{9}$",vmobilenumber)
        print(mobilenumber1)
        emailid1=re.search("[A-Za-z0-9]{0,20}@[a-z]+\.[a-z]{2,4}$",vemailid)
        print(emailid1)
        sub1mark1=re.search("[0-3]{1}[0-9]{1}|40$",vsub1mark)
        print(sub1mark1)
        sub2mark1=re.search("[0-3]{1}[0-9]{1}|40$",vsub2mark)
        print(sub2mark1)
        sub3mark1=re.search("[0-3]{1}[0-9]{1}|40$",vsub3mark)
        print(sub3mark1)
        sub4mark1=re.search("[0-3]{1}[0-9]{1}|40$",vsub4mark)
        print(sub4mark1)
        sub5mark1=re.search("[0-3]{1}[0-9]{1}|40$",vsub5mark)
        print(sub5mark1)
        if name1 and rollno1 and mobilenumber1 and emailid1 and sub1mark1 and sub2mark1 and sub3mark1 and sub4mark1 and sub5mark1 :
            return True
        else:
            return False

    while(True):
        print("1.Add Student with Mark")
        print("2.View all student details with marks using JSON File")
        print("3.View all student details based on Ranking using JSON File")
        print("4.Send an email to all parents less than 50% mark")
        print("5.Exit")
        option=int(input("Enter your option :"))
        if option==1:
            vname = input("Enter the name of student: ")
            vrollno=input("Ënter the RollNo of student:")
            admno=input("Enter the admno of Student:")
            college=input("Enter the college of student:")
            parentname=input("Enter the parent name:")
            vmobilenumber=input("Enter the mobilenumber:")
            vemailid=input("Enter the email:")
            vsub1mark=input("Enter the sub1 mark:")
            vsub2mark=input("Enter the sub2 mark:")
            vsub3mark=input("Enter the sub3 mark:")
            vsub4mark=input("Enter the sub4 mark:")
            vsub5mark=input("Enter the sub5 mark:")
            totalmarks=int(vsub1mark)+ int(vsub2mark)+int(vsub3mark)+int(vsub4mark)+int(vsub5mark)
            percentage=(totalmarks/500)*100
            if validate(vname,vrollno,vmobilenumber,vemailid,vsub1mark,vsub2mark,vsub3mark,vsub4mark,vsub5mark):
                d.addStudentDetails(vname,vrollno,admno,college,parentname,vmobilenumber,vemailid)
                d.addStudentResult(vsub1mark,vsub2mark,vsub3mark,vsub4mark,vsub5mark)
                dict={"name":vname,"rollno":vrollno,"admno":admno,"college":college,"parentname":parentname,"mobilenumber":vmobilenumber,"emailid":vemailid,"sub1mark":vsub1mark,"sub2mark":vsub2mark,"sub3mark":vsub3mark,"sub4mark":vsub4mark,"sub5mark":vsub5mark,"totalmarks":totalmarks,"percentage":percentage,}
                studentlist.append(dict)
            else:
                logging.error("wrong!Check Your Validation")
        
        if option==2:
            jsondata=json.dumps(studentlist)
            with open("newjson.json","w+",encoding="utf-8") as s:
                s.write(jsondata)

        if option==3:
            data=(sorted(studentlist,key=lambda i:i["totalmarks"],reverse=True))
            print(studentlist)
            jsondata=json.dumps(data)
            with open("newjson1.json","w+",encoding="utf-8") as newj:
                newj.write(jsondata)

        if option==4:
            try:
                connection=smtplib.SMTP("smtp.gmail.com",587)
                connection.starttls()
                connection.login("tamilarasiiprimed@gmail.com","Iprimed@123")                   
                for mail in studentlist:
                    if mail ["percentage"]<50:
                        message=str(mail)
                        message=message+str(mail)
                        connection.sendmail("tamilarasiiprimed@gmail.com",mail["emailid"],message)
                        connection.quit
                        print("Mail Sent Successfully:)")
            except Exception:
                logging.error("Mail Not Send")
                    
        if option==5:
            break
except Exception:
    logging.error("Something Wrong! Check Again")
finally:
    logging.info("Completed All Block")