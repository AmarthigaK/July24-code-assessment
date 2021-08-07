import multiprocessing,logging
try:
    def odd(getlist):
        for i in getlist:
            
            if (i%2!=0):
                print("odd:",i)
            
    def even(getlist):
        for i in getlist:
            
            if (i%2==0):
                print("even:",i)

    if (__name__=='__main__'):    
        mylist=[2,3,4,5,6]
        t1=multiprocessing.Process(target=odd,args=(mylist,))
        t2=multiprocessing.Process(target=even,args=(mylist,))   
        t1.start()
        t2.start()
except:
    logging.error("somethig went wrong")
          
                                  
    