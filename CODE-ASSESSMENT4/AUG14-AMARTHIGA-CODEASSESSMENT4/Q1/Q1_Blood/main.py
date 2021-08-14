#BLOOD BANK MANAGEMENT SYSTEM

#For Database Connection:
import pymongo    
#For sending email:
import smtplib
from email.mime.multipart import MIMEMultipart  
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
#For validation purpose - Custom module
from validation import validation1

#For CSV file creation and locate file
import csv
import glob

#
import logging


customer =pymongo.MongoClient("mongodb+srv://Amar_24:Amar2421@cluster0.g6gs1.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

DataBase = customer["BloodBank"]
collection = DataBase["Donor_Details"]

blood_DB = []

class donors:
    def donor_personal(self,name, address,pincode, bloodgrp, phn_no, email):
        self.name = name
        self.address = address
        self.pincode=pincode
        self.bloodgrp = bloodgrp
        self.phn_no =phn_no
        self.email = email

class donation(donors):
    def blood_donation(self, bld_date, place):
        self.bld_date = bld_date
        self.place = place

class Send_email:
    def content(self,mail_content, sender_address, sender_pass):
        self.mail_content =mail_content
        self.sender_address =sender_address
        self.sender_pass =sender_pass

class pass_message(Send_email):
    def content(message):
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = Donor_mail
        message['Subject'] = 'Emergency: Urgent Blood Requirement'

        message.attach(MIMEText(mail_content, 'plain'))
        attach_file_name = 'BloodNeeded.csv'
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
        session.sendmail(sender_address, donor, text)
        session.quit()
        print('Mail has been sent to blood donors')


BD = donation()
E = pass_message()

while(True):
    print("\n Welcome to BloodBank Management System")
    print("\n")
    print("1. Add Donor details")
    print("2. View all the Donor details")
    print("3. Search Donors based on blood group")
    print("4. Search Donors based on blood group and place")
    print("5. Update the donor details with their mobile number")
    print("6. Delete the donor using mobile number")
    print("7. Display the total number of donors on each blood group")
    print("8. Immediate notification to all via email")  
    print("9. Exit")  

    selection = int(input("Select your choice: "))
    
    if selection==1:
        print("\n")
        print("Add Donor details to the database")
        name = input("Enter donor name (Mr/Mrs/Ms. 'Name'): ")
        #n1 = validation1.valid1(name)

        address = input ("Enter Donor's Address: ")
        pincode = input("Enter Pincode: ")
        #pin = validation1.validpin(pincode)
        bloodgrp = input("Enter Donor's Blood Group: ")
        #bg = validation1.validbld(bloodgrp)
        phn_no = input ("Enter Donor's Mobile No: ")
        #mob =validation1.Valid2(phn_no)
        email = input("Enter E-mail ID: ")
        #emailid= validation1.Valid3(email)
        try:
            n1 = validation1.valid1(name)
            pin = validation1.validpin(pincode)
            bg = validation1.validbld(bloodgrp)
            mob =validation1.Valid2(phn_no)
            emailid= validation1.Valid3(email)
            print("Validated")
        except:
            logging.warning("Error has occured")
      

        bld_date = input("Enter Donor's last blood donated date: ")
        place = input("Enter Donor's last blood donated place: ")

        BD.donor_personal(name,address,pincode, bloodgrp, phn_no,email)
        BD.blood_donation(bld_date, place)
        donor = {"Donors_Name": name,
                "Address":address,
                "Blood_group":bloodgrp,
                "Mobile_No":phn_no,
                "Email_address":email,
                "Last_donated_date":bld_date,
                "Place":place, "del_flag":0
                }

        blood_DB.append(donor)
        bloods =collection.insert_many(blood_DB)

    if selection ==2:
        bloods =collection.insert_many(blood_DB)
        for n in bloods:
            print(n)

    if selection ==3:
        print("\n Search donor details by blood group")
        bld = input("Search donor by typing blood type: ")

        bld_grp = collection.find({"Blood_group":bld},{"_id":0})

        bldList =[]
        for x in bld_grp:
            bldList.append(x)
            print(x)

    if selection ==4:
        print("\n Search donor details by blood group and place")
        bld1 = input("Type donor's blood type: ")
        plc1 = input("Type donor's place: ")

        bld_grp2 = collection.find({"Blood_group":bld1, "Place":plc1},{"_id":0})

        bldList2 =[]
        for n in bld_grp2:
            bldList2.append(n)
            print(n)

    if selection ==5:
        print("Update Donor's Details ")
        mob = input("Enter mobile number to search: ")

        name2 = input("Enter donor's name: ")
        add = input("Enter donor's address: ")
        email1 = input("Enter donor's email address: ")
        bld2 = input("Enter donor's blood group: ")
        date_don = input("Enter last blood donated date: ")
        place_don = input("Enter last blood donated place: ")

        donor_list = collection.update_many({"Mobile_No":mob},{"$set":{"Donors_Name": name2, "Address":add, "Email_address":email1, "Blood_group":bld2, "Last_donated_date":date_don, "Place":place_don,}})

    if selection ==6:
        print('Delete the donor using mobile number ')
        mobile= input('Enter mobile number to delete: ')
        results=collection.update_one({"Mobile_No":mobile},{"$set":{"deflag":1}})
        print(results.deleted_count)
        #print()

    if selection ==7:
        print(" Display the total number of donors on each blood group")
        counts =collection.aggregate([{"$group":{"_id": "$Blood_group","No_of_donors":{"$sum":1}}}])
        for n in counts:
            print(n)

    if selection==8:
        need =[]
        print('Immediate notification to all via email')

        hsptl = input("Type the hospital name: ")
        hsptl_place = input("Type the place of hospital: ")
        blood = input("Type the blood group needed: ")
        Date = input("Blood group needed before: ")
        contact = input("Hospital contact number: ")
        mob1 =validation1.Valid2(contact)
        h_mail = input("Hospital email id: ")
        emailid1= validation1.Valid3(h_mail)

        mail_content = input("Type your message: ")

        user_inputs ={"HospitalName":hsptl,"Hospital_Address":hsptl_place,"Need_Blood":blood, "Need_before":Date, "Hospital_contact":contact, "Hospital_email":h_mail }
        need.append(user_inputs)
        print(need)

        Header = ["HospitalName","Hospital_Address","Need_Blood","Need_before","Hospital_contact","Hospital_email"]
        need_details = [{"HospitalName":hsptl,"Hospital_Address":hsptl_place,"Need_Blood":blood, "Need_before":Date, "Hospital_contact":contact, "Hospital_email":h_mail}]

        with open("BloodNeeded.csv","w+", encoding='UTF8',newline='')as s:        
            writer=csv.DictWriter(s,Header)
            writer.writeheader()
            writer.writerows(need)

        for x in glob.glob('Blood*.csv'):
            print(x)

        
        try:
            sending = collection.find({},{"Email_address":1,"_id":0})
            donor_list=[]
            for x in sending:
                donor_list.append(x)
            print(donor_list)

            donor = [v['Email_address'] for v in donor_list if 'Email_address' in v]
            print(donor)
            Donor_mail = ",".join(donor)


        except:
            logging.warning("Error has occured")


        #mail_content = " "
        sender_address = 'amarproject2021@gmail.com'
        sender_pass = 'Geo@2124'
        E.content()
        

    if selection ==9:
        print("Exit")
        break
    







