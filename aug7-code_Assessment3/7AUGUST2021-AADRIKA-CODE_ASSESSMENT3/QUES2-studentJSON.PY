from os import name
from validmodule import validation_of_Student
import time,logging,json,smtplib,collections


logging.basicConfig(filename='error2.log',level=logging.INFO)

studentlist=[]
stcount=collections.deque(studentlist)

############## parent class STUDENT ##############################################################
class Student:
    def __init__(self,name,rollnum,mobile,emailid,parents_emailid,adminum,college,Father_name,Mother_name):
            self.name=name
            self.rollnum=rollnum
            self.mobilenum=mobile
            self.emailid=emailid
            self.parents_emailid=parents_emailid
            self.adminum=adminum
            self.college=college
            self.Father_name=Father_name
            self.Mother_name=Mother_name

 ######## CHILD CLASS SEM1RESULT DERIVED FROM STUDENT ##################################################      
        
class Sem1Result(Student):

    def __init__(self,name,rollnum,mobile,emailid,parents_emailid,adminum,college,Father_name,Mother_name,sub1Marks,sub2Marks,sub3Marks,sub4Marks,sub5Marks):
            self.sub1Marks=sub1Marks
            self.sub2Marks=sub2Marks
            self.sub3Marks=sub3Marks
            self.sub4Marks=sub4Marks
            self.sub5Marks=sub5Marks
            Student.__init__(self,name,rollnum,mobile,emailid,parents_emailid,adminum,college,Father_name,Mother_name)
    def addstudentdetails(self,name,rollnum,mobile,email,parentmail,adminnum,college,Father_name,Mother_name,sub1Marks,sub2Marks,sub3Marks,sub4Marks,sub5Marks):
        
        total=int(sub1Marks)+int(sub2Marks)+int(sub3Marks)+int(sub4Marks)+int(sub5Marks)
       
        current_local_time=time.strftime("%H:%M:%S",time.localtime())
        dict1={"name":name,"rollnum":rollnum,"mobile":mobile,"email":email,"parentemail":parentmail,"adminnum":adminnum,"college":college,"Father_name":Father_name,"Mother_name":Mother_name,"sub1Marks":sub1Marks,"sub2Marks":sub2Marks,"sub3Marks":sub3Marks,"sub4Marks":sub4Marks,"sub5Marks":sub5Marks,"total":total,"addedon":current_local_time}
        stcount.append(dict1)
        return stcount





################ MENU DRIVEN LIST STARTS HERE##########################

while(True):
    print("1. Add Students:")
    print("2. display students details in API: ")
    print("3. Students according to ranking in API")
    print("4. Send email if percentage of marks is less tahn 50%")
    print("5. exit")
    choice=int(input("enter your choice: "))
    
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
           
            if validation_of_Student(name,rollnum,mobilenum,emailid,parents_emailid,sub1Marks,sub2Marks,sub3Marks,sub4Marks,sub5Marks):
                obj1=Sem1Result(name,rollnum,mobilenum,emailid,parents_emailid,adminum,college,Father_name,Mother_name,sub1Marks,sub2Marks,sub3Marks,sub4Marks,sub5Marks)
                obj1.addstudentdetails(name,rollnum,mobilenum,emailid,parents_emailid,adminum,college,Father_name,Mother_name,sub1Marks,sub2Marks,sub3Marks,sub4Marks,sub5Marks)        
            else:
                print("Please Try again by entering valid details and marks should be below 40")
                continue
            break
    
    if choice==2:

         json_data_file=json.dumps(studentlist)
         with open("jsonfilestudent.json","w",encoding="UTF8",newline="") as fl:
             fl.write(json_data_file)
             
             print("File got created")
             logging.info("Writing of data in JSON file is done")
    
    if choice==3:
         sortedlist=sorted(studentlist,key=lambda i:i["total"],reverse=True)
         json_data_file_ranking=json.dumps(sortedlist)
         with open ("jsonfilestudentrank.json","w",encoding="UTF8",newline="") as fl2:
             fl2.write(json_data_file_ranking)
             
             print("File got created on basis of ranking ")
             logging.info(" Writing of data in JSON file is done using ranking")
    if choice==4:
        per=(int(sub1Marks)+int(sub2Marks)+int(sub3Marks)+int(sub4Marks)+int(sub5Marks)/200)*100
        try:
            if per<=50:
                print("Your Child has scored less than 50 percent , please review the marks ")
                    
                message=str(per)
                connection=smtplib.SMTP("smtp.gmail.com",587)
                connection.starttls()
                connection.login("ridhimathur10@gmail.com","ridhima@10")
                connection.sendmail("ridhimathur10@gmail.com",parents_emailid,message)
            print("Sending email")
        except:
            logging.error("Cant send the mail")

    if choice==5:
         break


