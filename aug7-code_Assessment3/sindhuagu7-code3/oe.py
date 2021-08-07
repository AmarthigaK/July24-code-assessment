import multiprocessing,logging
try:
    def findodd(getlist):
        for i in getlist:
            # time.sleep(3)
            if i%2!=0:
                print("odd=>",i)
    def findeven(getlist):
        for i in getlist:
            # time.sleep(3)
            if i%2==0:
                print("even=>",i)
    if __name__ == "__main__":
        mylist=[2,3,4,5]
        p1=multiprocessing.Process(target=findodd,args=(mylist,))
        p2=multiprocessing.Process(target=findeven,args=(mylist,))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
        print("..........")
except Exception:
    logging.error("Something Wrong!")