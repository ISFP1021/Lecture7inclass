def addition(first, second):
    print("The sum of %d and %d is %d"%(first, second, first+second))
first=int(input("Give me a number"))
second=int(input("Give me another number"))
addition(first,second)

#alternative
def addition(first, second):
    return first+second

first=int(input("Give me a number"))
second=int(input("Give me another number"))
x=addition(first,second)
print (x)