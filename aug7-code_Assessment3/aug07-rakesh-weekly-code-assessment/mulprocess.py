import logging,multiprocessing
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

        p1=multiprocessing.Process(target=findeven,args=(mylist,))    
        p2=multiprocessing.Process(target=findodd,args=(mylist,))  
        p1.start()
        p1.join()
        p2.start()
        p2.join() 
except:
    logging.error("Oops! Something is not right ")   
finally:
    print("Thank You!!")  