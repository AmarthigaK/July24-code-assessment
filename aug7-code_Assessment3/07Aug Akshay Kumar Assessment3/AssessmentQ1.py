import time,multiprocessing

def findEven(getList):
    for i in getList:
        time.sleep(3)
        if i%2 == 0:
            print("Even->",i)

def findOdd(getList):
    for i in getList:
        time.sleep(3)
        if i%2 != 0:
            print("Odd->",i)
myList = [1,2,3,4,5,6] 

if (__name__ =="__main__"):

    p1 = multiprocessing.Process(target=findEven,args=(myList,))  #Creating a thread
    p2 = multiprocessing.Process(target=findOdd,args=(myList,))
    p1.start()
    p2.start()


    p1.join()
    p2.join() # when we use join, first thread will get executed , and then *****
    print("******")

    
