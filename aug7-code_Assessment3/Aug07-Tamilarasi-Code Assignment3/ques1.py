import time,multiprocessing,logging
try:
    def findeven(getlist):
        even=[i for i in getlist if i%2==0]
        time.sleep(1)
        print("even:",even)
    def findodd(getlist):
        odd=[i for i in getlist if i%2==1]
        time.sleep(1)
        print("odd:",odd)
    if(__name__=='__main__'):
        mylist=[2,3,7,8,9,3,4,6,8]
        p1=multiprocessing.Process(target=findeven,args=(mylist,))
        p2=multiprocessing.Process(target=findodd,args=(mylist,))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
        print("*********CODE COMPLETED*********")
except Exception:
    logging.error("Something Wrong!")
finally:
    logging.info("Done!!!")