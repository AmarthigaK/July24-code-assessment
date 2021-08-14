import re

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
    
    def validpin(pin):
        pincode = re.match("^[1-9]\d{5}$", pin)
        if pincode:
            print("Pincode Validated")
        else:
            print("Invalid pincode")

    def validbld(bldgrp):
        bldgrp1 = re.search("^(A|B|AB|O)([+-]+)(ve)$", bldgrp)

        if bldgrp1:
            print(" ")
        else:
            print("Invalid, please give correct bloodgroup")


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