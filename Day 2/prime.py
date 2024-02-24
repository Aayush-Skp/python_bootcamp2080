def checkprime(num1):
    if (num1<=1):
        return False
    for divider in range(2, num1):
        if(num1 % divider == 0):
            return False
    return True   


def primerange(start,end):
    primenumbers=[]
    for number in range (start, end):
        if (checkprime(number)):
            primenumbers.append(number)
    return primenumbers 

