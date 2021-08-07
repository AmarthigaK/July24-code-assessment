import threading,logging
# mylist=[1,2,3,4,5,56,7,8,56,67,89,90]
def even(getlist):
    even_no=list(filter(lambda x:(x%2==0),mylist))
    print("even numbers in the list is:",even_no)
def odd(getlist):
    odd_no=list(filter(lambda x:(x%2==1),mylist))
    print("odd number in the list is",odd_no)
            
mylist=[1,2,3,4,5,56,7,8,56,67,89,90]
try:
    t1=threading.Thread(target=even,args=(mylist,))
    t2=threading.Thread(target=odd,args=(mylist,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("done with printing")
except:
    logging.error("incorrect input pls check it")
finally:
    print("Thank you")






