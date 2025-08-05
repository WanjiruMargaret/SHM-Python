
# your function only takes 3 parameters
# your function 4 or 5 or 6
#Args -> arguments
#def stuff(name,age,gender,is_married):

# parametrs<fixed> how many of taken

#def  greet(*args):
#    for value in args:
#        print("Name is",value)

def greet(*args):
    for arg in args:
        print("Name is" ,args)

#greet("John","Samuel","Mandy","Joan","Mary","Odhiambo")
#greet(123,True,False,None,[1,2,3])

#how 10,10, -> 100,200,150
def sum(*args):
    ans=0
    for n in args:
        print(f"{ans}={ans}+{n}")
        ans=ans+n
        
    print("Ans is ",ans)
    return ans

sum(100,50,20,30,150,200,700)