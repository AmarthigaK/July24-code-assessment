import logging,re,json
Studentlist=[]
import smtp
try:
    class Student:
        def details(self,name,roll,admin,cname,parent,mobile,email):
            self.name=name
            self.roll=roll
            self.admin=admin
            self.cname=cname
            self.parent=parent
            self.mobile=mobile
            self.email=email
            
    obj1=Student()

    class Sem1Result(Student):
        def Marks(self,telugu,hindi,english,maths,science):
            # self.telugu=int(input("enter Telugu marks"))
            # self.hindi=int(input("enter hindi marks"))
            # self.english=int(input("enter english marks"))
            # self.maths=int(input("enter maths marks"))
            # self.science=int(input("enter science marks"))
            total=telugu+hindi+english+maths+science
            student1={"name":name,"roll":roll,"admin":admin,"cname":cname,"parent":parent,"mobile":mobile,"email":email,"telugu":telugu,"hindi":hindi,"english":english,"maths":maths,"science":science,"total":total}
            Studentlist.append(student1)
            
    obj2=Sem1Result()
    def validate(name,roll,mobile,email,telugu,hindi,english,maths,science): 

            valname=re.search("[A-Za-z]{0,25}$",name)
            valroll=re.search("[0-9]\d{0,7}$",roll)
            valmobile=re.search("[6-9]\d{9}$",mobile)
            valemail=re.search("[A-Za-z0-9]{0,20}@[a-z]+\.[a-z]{2,4}$",email)
            valtelugu=re.search("[0-3]{1}[0-9]{1}|40$",telugu)
            valenglish=re.search("[0-3]{1}[0-9]{1}|40$",hindi)
            valhindi=re.search("[0-3]{1}[0-9]{1}|40$",english)
            valmaths=re.search("[0-3]{1}[0-9]{1}|40$",maths)
            valscience=re.search("[0-3]{1}[0-9]{1}|40$",science)
            if valname and valroll and valmobile and valemail and valtelugu and valhindi and valenglish and valmaths and valscience:
                return True
            else:
                return False
    while(True):
            print("1.Add student Details with mark:")
            print("2.Generate json file the API to view all students with marks:")
            print("3.Generate json file the API to view all students based on ranking:")
            print("4.send an email to all the parents if the total percentage of marks is less than 50%:")
            print("5.Exit")
            choice=int(input("enter your choice"))
            if choice==1:
                

                name=input("Enter your name:")
                roll=int(input("enter yor roll number:"))
                admin=int(input("enter your admin number:"))
                cname=input("enter your college name:")
                parent=input("enter your parent name:")
                    
                mobile=int(input("enter mobile number:"))
                email=str(input("enter your email id:"))
                telugu=int(input("enter Telugu marks"))
                hindi=int(input("enter hindi marks"))
                english=int(input("enter english marks"))
                maths=int(input("enter maths marks"))
                science=int(input("enter science marks"))
                obj1.details(name,roll,admin,cname,parent,mobile,email)
                obj2.Marks(telugu,hindi,english,maths,science)
                
                
                
            if choice==2:
                jsonfilePath='student2.json'
                student_list_json=json.dumps(Studentlist)
                with open(jsonfilePath,'w',encoding='UTF8') as f:
                 f.write(student_list_json)
            if choice==3:
                jsonfilePath='studentranking.json'
                studentrank_list_json=json.dumps(Studentlist)
                with open(jsonfilePath,'w',encoding='UTF8') as f:
                 f.write(sorted(studentrank_list_json,key=lambda i:i['total'],reverse=True))
                 break
except:
    logging.error("somethin went program")
            

        


            
