import re
def validationForAll(name,roll,mob,email,pemail,s1 ,s2 ,s3 ,s4 ,s5):
    reg = '^\w+[\._]?\w+[@]\w+[.]\w{2,3}$'
    reg1 = '^\w+[\._]?\w+[@]\w+[.]\w{2,3}$'
    val1=re.match("([a-z]+)([a-z]+)([a-z]+)$",name)
    val2=re.match("[0-9]{0,7}$",roll)
    val3=re.match("[0-9]{0,7}$",mob)
    val4=re.match(reg,email)
    val5=re.match(reg1,pemail)
    val6=re.match("^(40|[1-3][0-9]?)$",s1)
    val7=re.match("^(40|[1-3][0-9]?)$",s2)
    val8=re.match("^(40|[1-3][0-9]?)$",s3)
    val9=re.match("^(40|[1-3][0-9]?)$",s4)
    val10=re.match("^(40|[1-3][0-9]?)$",s5)
    if val1 and val2 and val3 and val4 and val5 and val6 and val7 and val8 and val9 and val10 :
     return True
    else:
     return False