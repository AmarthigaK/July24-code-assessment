import multiprocessing,logging,time

def findodd(getlist):
    for i in getlist:
        time.sleep(1)
        if (i%2!=0):
            print("odd:",i)
        
def findeven(getlist):
    for i in getlist:
        time.sleep(1)
        if (i%2==0):
            print("even:",i)
try:

    if (__name__=='__main__'):    
        mylist=[2,3,4,5,6]
        t1=multiprocessing.Process(target=findodd,args=(mylist,))
        t2=multiprocessing.Process(target=findeven,args=(mylist,))   
        t1.start()
        t2.start()
        t1.join()   
        t2.join()                           
        print("...........")
except Exception:
    print("error")
else:
    print("susseful")
finally:
    print("completed")
