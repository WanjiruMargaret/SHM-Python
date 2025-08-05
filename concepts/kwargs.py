
## *kwargs -> Key word arguments
## Dictionary{key:value}

def greet(name,nationality):
    print("Name is",name)
    print("From ",nationality)

##kwargs solve the mixture
##greet(nationality="Kenya" , name="Kasongo") 
def employee(**kwargs):
    print(kwargs)

    for key,value in kwargs.items():
        print ("For key",key, "The value is",value)
    

##employee(name="Samson" ,age=23, degree="Engineering")
##employee(name="Kasongo",county="Kenya",degree=("Engineering"))

def do_drink(**kwargs):
    drinks=kwargs["drink"]
    prices=kwargs["prices"]

    print(kwargs)

    for index,value in enumerate(drinks):
        print("For index",index)
        print("The Drink",value)
        print("The price",prices[index])


##ARGS AND KWARGS --> DECORATORS
#do_drink(drink=["Glenfidish","KingFisher"],
#         prices=[120,100,40])

def mixed(*args,**kwargs):
    print("kwargs",kwargs)
    print("Args",args)

mixed("cool","drinks",name="John",age=20)

#kwargs and args

def square_all(*args):
    ans=[]
    for n in args:
        ans.append(n*n)
    print(ans)
    return ans

square_all(2,4,6,1)