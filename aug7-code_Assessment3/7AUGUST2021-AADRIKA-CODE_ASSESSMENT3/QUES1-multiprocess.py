import multiprocessing ,logging
import collections
logging.basicConfig(filename="multiprocess.log",level=logging.ERROR)

mylist=[12,23,34,45,56,67,78,89,100]
c=collections.Counter(mylist)
print(c)
# n=int(input("Enter the number till which you want to see even odd"))
# for i in range(n):
#     element=int(input("Enter the number"))
#     mylist.append(element)


def findEven(getli):
    try:
        for i in getli:
            if i%2==0:
             print("even ",i)
    except:
        logging.error("Function is not working")

def findOdd(getli):
    try:
        for i in getli:
            if i%2!=0:
                print("odd ",i)
    except:
        logging.error("function is not responding")


if(__name__=='__main__'):
    p1=multiprocessing.Process(target=findEven,args=(mylist,))
    p2=multiprocessing.Process(target=findOdd,args=(mylist,))
   
    p1.start()
    p2.start()
    # p1.join()
    print("******")
