import multiprocessing,time,logging
try:
    def findeven(getlist):
        for i in getlist:
            time.sleep(2)
            if i%2==0:
                print(i,"is even")
    def findodd(getlist):
        for i in getlist:
            time.sleep(2)
            if i%2!=0:
                print(i,"is odd")
    if(__name__=="__main__"):
        mylist=[2,3,4,5]
        p1=multiprocessing.Process(target=findeven,args=(mylist,))
        p2=multiprocessing.Process(target=findodd,args=(mylist,))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
        print('........')

except:
    logging.error("unable to process")

