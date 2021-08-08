import re
#def Valid():
#i = input("enter: ")
class validation1:
    def valid1(name):
        re_name = re.compile(r"^(Mr\.|Mrs\.|Ms\.) ([a-z]+)( [a-z]+)*( [a-z]+)*$", re.IGNORECASE)
        val1 = re_name.search(name)
        if val1:
            print("Name Validated")
        else:
            print("Name is invalid")
    def Valid2(val2):
        mobile= re.search("^\+91?[6-9]\d{9}$",val2)
        if mobile:
            print("Mobile Number validated")
        else:
            print("error")

    # def Valid3(val3):
    #     email ="r^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

    #     if email:
    #         print("Vaild Email")
    #     else:
    #         print("Error")

      
  
    def Valid3(email):  
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$' 
        if(re.search(regex,email)):   
            print("Valid Email")   
        else:   
            print("Invalid Email")   
      
    if __name__ == '__main__' :   
        email = "rohit.gupta@mcnsolutions.net"  
        Valid3(email)   
        email = "praveen@c-sharpcorner.com"  
        Valid3(email)   
        email = "inform2atul@gmail.com"  
        Valid3(email) 
