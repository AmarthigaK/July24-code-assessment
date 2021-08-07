import threading,time,logging
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
        t1=threading.Thread(target=findeven,args=(mylist,))
        t2=threading.Thread(target=findodd,args=(mylist,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        print('........')


except:
    print("unable to process")