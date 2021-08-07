import re,json,smtp,logging

studentlist=[]
class Student:   
    def addstudent(self,name,rollno,admno,college,parentname,moblienumber,emailid):
        dic={"name":name,"rollno":rollno,"admno":admno,"college":college,"parentname":parentname,"moblienumber":moblienumber,"emailid":emailid}
        studentlist.append(dic) 

class Sem1Result:
    def result(self,sub1mark,sub2mark,sub3mark,sub4mark,sub5mark):
            
        total=((sub1mark+sub2mark+sub4mark+sub5mark)/5)
        dic1={"total":total,"sub1mark":sub1mark,"sub2mark":sub2mark,"sub3mark":sub3mark,"sub4mark":sub4mark,"sub5mark":sub5mark}
        studentlist.append(dic1)

obj1=Student()
obj2=Sem1Result()

while(True):    #menudriven
    print("1 Add student with marks: ")
    print("2 generate JSON file and display the api to view all stusent details with marks :")
    print("3 generate JSON file and display the api to view all stusent details based on ranking:")
    print("4 Send an email to parents if the total prec of marks is less than 50% :")
    print("5 exit:")
    choice=int(input("enter a option:"))
   

    if choice==1:
        name=input("enter name:")
        rollno=int(input("enter roll no:"))
        admino=int(input("enter admno no:"))
        college=input("enter college:")
        parentname=(" enter parent name")
        moblienumber=int(input("enter mobileno"))
        emailid=input("enter emailid")
        sub1mark=int(input("enter sub1 marks:"))
        sub2mark=int(input("enter sub1 marks:"))
        sub3mark=int(input("enter sub1 marks:"))
        sub4mark=int(input("enter sub1 marks:"))
        sub5mark=int(input("enter sub1 marks:"))
       

        def val(name,rollno,admino):
            val1=re.search("^[A-Z]",name)
            val2=re.search('^[1-9]',rollno)
            val3=re.search('^[0-9]',admno)
            val4=re.search('^[A-Z]?[a-z]',college)
            val5=re.search('/d[1-10]',moblienumber)
            if val1 and val2 and val3 and val4 and val5:
                return True
            else:
                return False

obj1.addstudent(name,rollno,admno,college,parentname,moblienumber,emailid)
obj2.Sem1Result(sub1mark,sub2mark,sub3mark,sub4mark,sub5mark)


    if choice==2:
        jsonfilePath='student2.json'
        student_list_json=json.dumps(Studentlist)
        with open(jsonfilePath,'w',encoding='UTF8') as f:
        f.write(student_list_json)
                
    if choice==3:
        jsonfilePath='studentranking.json'
        studentrank_list_json=json.dumps(Studentlist)
        with open(jsonfilePath,'w',encoding='UTF8') as f:
        f.write(sorted(studentr_list_json,key=lambda i:i['total'],reverse=True))
        print(studentlist)
try:
    if choice==4:
        if(total<5):
            print("percentage",total)
            message=str(total)
            connection=smtplib.SMTP("smtp.gmail.com",587)
            connection.starttls()
            connection.login("krupamh0@gmail.com","panipuri23@")
            connection.sendmail("krupa9927@gmail.com",Email,message)
            print("Email successfully send")
            connection.quit()
            break
         else:
            break
        
except:
logging.error("somethin went program")
    print(studentlist)
                

    if choice==5:
        break