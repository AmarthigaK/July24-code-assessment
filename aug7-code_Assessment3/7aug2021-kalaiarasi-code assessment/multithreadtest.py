import time,threading,logging
try:

    def even(getlist):
        for i in getlist:
            time.sleep(1)
            if i%2==0:
                print("even:",i)
    def odd(getlist):
        for i in getlist:
            time.sleep(1)
            if i%2!=0:
                print("odd:",i)
    if(__name__=='__main__'):
        lis=[1,2,3,4,5,6,7,8]
        t1=threading.Thread(target=even,args=(lis,))
        t2=threading.Thread(target=odd,args=(lis,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        print(".........")
except:
    logging.error("something went wrong")