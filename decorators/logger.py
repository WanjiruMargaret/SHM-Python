
import time

def logger(func):
    def wrapper(*args,**kwargs):
        start_time=time.time()
        func(*args,**kwargs)
        end_time=time.time()
        diff=end_time-start_time
        txt=f"function:{func._name_}time taken {diff} seconds"
        f_name="logger.txt"
        write_file(f_name=f_name,txt=txt)
    return wrapper    


def write_file(f_name,txt):
    with open(f_name,'a') as file:
        file.write(f"{txt} \n")

@logger
def counter():
    for n in range(0,10000000):
        print(n)

@logger
def sum(*args):
    ans=0
    for n in args:
        print(ans,"=",ans,"+",n)
        ans=ans+n

    print("Ans is ",ans)
    return ans

counter()    
    

