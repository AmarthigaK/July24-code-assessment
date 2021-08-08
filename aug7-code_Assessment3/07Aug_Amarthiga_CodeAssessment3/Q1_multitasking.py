'''Demonstrate multi-threading OR multi-processing concept with an example to find out the
even and odd numbers from a list'''

import multiprocessing
import logging
import pytz
from datetime import datetime
import glob

logging.basicConfig(filename='multi.log', level=logging.INFO)

std_time = pytz.utc
time = pytz.timezone("Asia/Kolkata")

# Find even no:
def evenNo(l):
    for n in l:
        if n%2 ==0:
            print(n)

# Find odd no:
def oddNo(l):
    for x in l:
        if x%2 ==1:
            print(x)      

l1=[12, 45, 89, 66, 34, 8, 20]
l2=[11, 5, 87, 6, 13, 8, 21]

if (__name__) == "__main__":
    m = multiprocessing.Process(target=evenNo , args=(l1,))
    n = multiprocessing.Process(target=oddNo , args=(l2,))
    m.start()
    n.start()
    print("Even numbers printed")
    m.join()
    print("Odd numbers printed")
    n.join()
    
    try:
        logging.info("Even and Odd numbers were found by using multiprocssing")
        logging.info(datetime.now(time).strftime("Printed Date %d-%m-%y and Time %H:%M:%S"))
    
        print("Click the following file to view Run Time: ")
        #file checking
        for n in glob.glob('m*.log'):
            print(n)
    except:
        logging.error("An error occured")

    



# even =list(filter(lambda n:(n%2 == 0), list))
# print(even)
#even = list(filter(lambda n:(n%2 == 0), l))