import logging,threading
try:
    def findeven(getlist):
        for i in getlist:
            if(i%2==0):
               print(i)
    def findodd(getlist):
        for i in getlist:
            if(i%2!=0):
               print(i)    
    if(__name__=="__main__"):
        mylist=[1,2,3,4,5,6,7,8,9,10]  

        t1=threading.Thread(target=findeven,args=(mylist,))    
        t2=threading.Thread(target=findodd,args=(mylist,))  
        t1.start()
        t1.join()
        t2.start()
        t2.join() 
except:
    logging.error("Oops! Something is not right ")   
finally:
    print("Thank You!!")    