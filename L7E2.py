def isnumberdiv3(n):
    if n%3==0:
        return True
    return False


num=int(input("Give me a number"))
if isnumberdiv3(num):
    print("Number is divisible by 3")
else:
    print("Number is not divisible by 3")