import multiprocessing,time,logging
try:

    def even_num(mylist):
     for i in mylist:
    
       if(i % 2 == 0):
         
         print(i)
     
    def odd_num(mylist):
        for i in mylist:
            if(i %2 != 0):
              
              print(i)
    if __name__ == "__main__":
      mylist=[1,2,3,4]
      p1=multiprocessing.Process(target=even_num,args=(mylist,))  #create a thread
      p2=multiprocessing.Process(target=odd_num,args=(mylist,))
      p1.start()
      p2.start()
      p1.join()
      p2.join()
      print(".......")
except Exception:
    logging.error("Something went error")
finally:
    print("done my work!!")    

  #t1=threading.Thread(target=even_num,args=(mylist,))  #create a thread
  #t2=threading.Thread(target=odd_num,args=(mylist,))
  #1.start()
  #t2.start()
  #t1.join()
  #2.join()
  #rint(".......")
  #ogging.error("something went wrong")
  