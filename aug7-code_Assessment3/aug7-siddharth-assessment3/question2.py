import re,time,logging,json,smtplib,collections
from validatexm import validationForAll
logging.basicConfig(filename='error2.log',level=logging.INFO)
studentlist=[]
x=collections.deque(studentlist)
class Student:
    def studentdetails():
         name=" "
         rollnum=0
         email=""
         parentmail=""
         adminnum=0
         college=' '
         Father_name=" "
         Mother_name=" "
class Sem1Result:
    def stumarks():
        sub1Marks=0
        sub2Marks=0
        sub3Marks=0
        sub4Marks=0
        sub5Marks=0
class studentdetails(Student,Sem1Result):
    def addstudentdetails(self,name,rollnum,mobile,email,parentmail,adminnum,college,Father_name,Mother_name,sub1Marks,sub2Marks,sub3Marks,sub4Marks,sub5Marks):
        total=int(sub1Marks)+int(sub2Marks)+int(sub3Marks)+int(sub4Marks)+int(sub5Marks)
        current_local_time=time.strftime("%H:%M:%S",time.localtime())
        dict1={"name":name,"rollnum":rollnum,"mobile":mobile,"email":email,"parentemail":parentmail,"adminnum":adminnum,"college":college,"Father_name":Father_name,"Mother_name":Mother_name,"sub1Marks":sub1Marks,"sub2Marks":sub2Marks,"sub3Marks":sub3Marks,"sub4Marks":sub4Marks,"sub5Marks":sub5Marks,"total":total,"addedon":current_local_time}
        x.append(dict1)
        return x
obj1=studentdetails()
# def validationForAll(name,roll,mob,email,pemail,s1 ,s2 ,s3 ,s4 ,s5):
#     reg = '^\w+[\._]?\w+[@]\w+[.]\w{2,3}$'
#     reg1 = '^\w+[\._]?\w+[@]\w+[.]\w{2,3}$'
#     val1=re.match("([a-z]+)([a-z]+)([a-z]+)$",name)
#     val2=re.match("[0-9]{0,7}$",roll)
#     val3=re.match("[0-9]{0,7}$",mob)
#     val4=re.match(reg,email)
#     val5=re.match(reg1,pemail)
#     val6=re.match("^(40|[1-3][0-9]?)$",s1)
#     val7=re.match("^(40|[1-3][0-9]?)$",s2)
#     val8=re.match("^(40|[1-3][0-9]?)$",s3)
#     val9=re.match("^(40|[1-3][0-9]?)$",s4)
#     val10=re.match("^(40|[1-3][0-9]?)$",s5)
# if validationForAll.val1 and validationForAll.val2 and validationForAll.val3 and validationForAll.val4 and validationForAll.val5 and validationForAll.val6 and validationForAll.val7 and validationForAll.val8 and validationForAll.val9 and validationForAll.val10 :
#     return True
# else:
#     return False
while(True):
    print("1. Add Students:")
    print("2. display students details in API: ")
    print("3. Students according to ranking in API")
    print("4. Send email if percentage of marks is less tahn 50%")
    print("5. exit")
    try:
        choice=int(input("enter your choice: "))
    except ValueError:
        print("Enter correct choice")
        logging.error("User pressed different key")
    
    if choice==1:
        while(True):
            name=input("Enter your name: ")
            rollnum=(input("enter your rollnum: "))
            mobilenum=(input("enter your mobile: "))
            emailid=(input("enter your email id: "))
            parents_emailid=(input("enter parents email id: "))
            adminum=(input("enter your admission number: "))
            college=(input("enter your college name: "))
            Father_name=(input("enter your father's name: "))
            Mother_name=(input("enter your mother's name: "))
            sub1Marks=input("enter subject1 marks: ")
            sub2Marks=input("enter subject2 marks: ")
            sub3Marks=input("enter subject3 marks: ")
            sub4Marks=input("enter subject4 marks: ")
            sub5Marks=input("enter subject5 marks: ")
           
            if validationForAll(name,rollnum,mobilenum,emailid,parents_emailid,sub1Marks,sub2Marks,sub3Marks,sub4Marks,sub5Marks):
                 obj1.addstudentdetails(name,rollnum,mobilenum,emailid,parents_emailid,adminum,college,Father_name,Mother_name,sub1Marks,sub2Marks,sub3Marks,sub4Marks,sub5Marks)        
            else:
                print("Please Try again by entering valid details and marks should be below 40")
                continue
            break
    
    if choice==2:

         jsondatafile=json.dumps(studentlist)
         with open("jsonfilestudent.json","w",encoding="UTF8",newline="") as f:
             f.write(jsondatafile)
             logging.info(" Date Written to json file")
             print("File got created")
    
    if choice==3:
         sortedlist=sorted(studentlist,key=lambda i:i["total"],reverse=True)
         jsondatafileranking=json.dumps(sortedlist)
         with open ("jsonfilestudentrank.json","w",encoding="UTF8",newline="") as f1:
             f1.write(jsondatafileranking)
             logging.info(" Date Written to json file in ranking order")
             print("File got created on basis of ranking ")
    if choice==4:
         per=(obj1.addstudentdetails.total/200)*100
         if per<=50:
            print("Your Child has scored less than 50 percent ")
                
            message="score of your child is "+str(per)
            connection=smtplib.SMTP("smtp.gmail.com",587)
            connection.starttls()
            connection.login("hariompateldada@gmail.com","Sparsh@01")
            connection.sendmail("hariompateldada@gmail.com",obj1.parentmail,message)
            logging.info("Mail sent")
         print("Sending email")
    if choice==5:
        break