import json
import glob
import csv
import re
import smtplib
from email.mime.multipart import MIMEMultipart  
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import logging
from test1 import validation1

Student_Database= []

class students:
    def std_database(self, Name, rollno, adminno, parentname, mobileno, emailid):
        self.Name=Name
        self.rollno=rollno
        self.adminno=adminno
        self.parentname = parentname
        self.mobileno = mobileno
        self.emailid = emailid
        
class sem_reults(students):
    def std_marks(self, EnggPhy, EnggChe, ComputerPro, EnggGraphics, Maths, Total, Percentage):
        self.EnggPhy = EnggPhy
        self.EnggChe = EnggChe
        self.ComputerPro = ComputerPro
        self.EnggGraphics = EnggGraphics
        self.Maths = Maths
        self.Total = Total
        self.Percentage = Percentage

class Send_email:
    def content(self,mail_content, sender_address, sender_pass):
        self.mail_content =mail_content
        self.sender_address =sender_address
        self.sender_pass =sender_pass

class pass_message(Send_email):
    def content(message):
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = Parent_mail
        message['Subject'] = 'Semester Result of Student'

        message.attach(MIMEText(mail_content, 'plain'))
        attach_file_name = 'SemResult.csv'
        attach_file = open(attach_file_name, 'rb')
        payload = MIMEBase('application', 'csv',Name=attach_file_name)
        payload.set_payload((attach_file).read())
        encoders.encode_base64(payload)

        payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
        message.attach(payload)

        session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
        session.starttls() #enable security
        session.login(sender_address, sender_pass) #login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, Parent_mail, text)
        session.quit()
        print('Mail has been sent to parent')              

R=sem_reults()
S=pass_message()

while(True):
    print("\n")
    print("1. Add student details with mark")
    print("2. View all student details in a file")
    print("3. View all student details based on ranking")
    print("4. Send email to student's parent who scored less than 50%")
    print("5. Exit")

    Selection = int(input("Select your choice: "))

    if Selection==1:
        print("\n")
        print("Add student details to the database")
        Name = input("Enter student name: ")
        n1 = validation1.valid1(Name)
        parentname = input("Enter Father Name of the student: ") 
        n2 = validation1.valid1(parentname)
        mobileno = input("Enter Mobile Number: ")
        mob =validation1.Valid2(mobileno)
        emailid = input("Enter E-mail ID: ")
        email= validation1.Valid3(emailid)

        rollno = int(input("Enter student RollNo: "))
        adminno = int(input("Enter student Admission No: "))
        EnggPhy = int(input("Enter the mark in Engineering Physics (Out of 40): "))
        EnggChe = int(input("Enter the mark in Engineering Chemistry (Out of 40): "))
        ComputerPro = int(input("Enter the mark in Computer Programming (Out of 40): "))
        EnggGraphics = int(input("Enter the mark in Engineering Graphics (Out of 40):")) 
        Maths = int(input("Enter the mark in Engineering Mathematics (Out of 40): "))
        Total = EnggPhy+EnggChe+EnggGraphics+ComputerPro+Maths 
        Percentage = (Total/200)*100
               
        R.std_database(Name, rollno, adminno, parentname, mobileno, emailid )
        R.std_marks(EnggPhy, EnggChe, ComputerPro, EnggGraphics, Maths, Total, Percentage)

        Student_details ={"Student Name":Name, 
                          "Roll_No":rollno, 
                          "Admission_No":adminno, 
                          "Father_Name": parentname, 
                          "Mobile_No": mobileno, 
                          "Email_ID": emailid, 
                          "Engineering_Physics": EnggPhy,
                          "Enngineering_Chemistry": EnggChe,
                          "Computer Programming": ComputerPro,
                          "Enngineering Graphics" : EnggGraphics,
                          "Mathematics":  Maths,
                          "Total_Score":Total,
                          "Total_Percentage":Percentage
        }
                            
        Student_Database.append(Student_details)  

        print("\n", Student_Database)


    if Selection==2:
        print("\n")
        print("You can select the following file to view all student details: ")
        Std_list =json.dumps(Student_Database)
        
        with open('StudentDatabase.json', 'w+', encoding='UTF-8') as s:
            s.write(Std_list)

        #Checking and Showing the file
        for i in glob.glob('StudentD*.json'):
            print(i)
    

    if Selection==3:
        print("\n")
        print("You can select the following file to view all student details based on ranking: ")

        sorted(Student_Database,key=lambda i:i ['Total_Score'], reverse=True)

        Ranking_list =json.dumps(Student_Database)

        #Checking and Showing the file
        with open('StudentRanking.json', 'w+', encoding='UTF-8') as u:
            u.write(Ranking_list)

        for n in glob.glob('StudentRa*.json'):
            print(n)


    if Selection==4:
        print("\n")
        print("Email will be sent to the student's parent who scored less than 50%")

        Std50 = [x for x in Student_Database if x ['Total_Percentage']<50]
        print(Std50)
        
        Header = ["Student Name", "Roll_No", "Engineering_Physics", "Enngineering_Chemistry", "Computer Programming", "Enngineering Graphics", "Mathematics", "Total_Score", "Total_Percentage" ]
        Details =[{"Student Name":Name, 
                          "Roll_No":rollno, 
                          "Engineering_Physics": EnggPhy,
                          "Enngineering_Chemistry": EnggChe,
                          "Computer Programming": ComputerPro,
                          "Enngineering Graphics" : EnggGraphics,
                          "Mathematics":  Maths,
                          "Total_Score":Total,
                          "Total_Percentage":Percentage
        }]

        with open("SemResult.csv","w+", encoding='UTF8',newline='')as s:        
            writer=csv.DictWriter(s,Header)
            writer.writeheader()
            writer.writerows(Details)
        
        R.std_database(Name,rollno, adminno, parentname, mobileno, emailid )
        R.std_marks(EnggPhy, EnggChe, ComputerPro, EnggGraphics, Maths, Total, Percentage)

        for x in glob.glob('Sem*.csv'):
            print(x)
        
        
        try:
            Parent_mail =input("Please enter parent's email ID: ")
            val_email = validation1.Valid3(Parent_mail)
            print(Parent_mail)
        except:
            logging.warning("Error in validation")

        mail_content = """Dear Parent,
        Here is an attachment of your son/daughter Semester Result.
        Please, find the attachment and refer it.
                  
        Thanks and Regards,
        College Administration"""
        sender_address = 'amarproject2021@gmail.com'
        sender_pass = 'Geo@2124'  

        S.content() 

    if Selection==5:
        print("Exit")
        break
