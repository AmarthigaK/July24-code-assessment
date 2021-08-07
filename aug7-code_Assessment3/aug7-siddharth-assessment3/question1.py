import threading,logging,collections
logging.basicConfig(filename="multithred.log",level=logging.DEBUG)
try:
    def FindEven(getlist):
        for i in getlist:
            if i%2==0:
                print("even ",i)
    def FindOdd(getlist):
        for i in getlist:
            if i%2!=0:
                print("odd ",i)

    mylist=[23,45,66,12,2,87,98,99,99,23]
    #tried to use counter here
    x2=collections.Counter(mylist)
    print(x2)
    if(__name__=="__main__"):
        t1=threading.Thread(target=FindEven,args=(mylist,))
        t2=threading.Thread(target=FindOdd,args=(mylist,))
        logging.info("Multithreading is achieved")
        t1.start()
        t2.start()
        print("$$$$$$$$$$$$$$$")
        logging.info("Multithreading is achieved")

except:
    print("Something went wrong")
finally:
    ("Multithreading done")