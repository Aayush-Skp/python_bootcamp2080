def checkodd(num1):
    if (num1 % 2 == 0):
        return False 
    else:
        return True

def oddrange(num2,num3):
    numbers=[]
    for number in range(num2,num3):
        if(number % 2 != 0):
            numbers.append(number)
    return numbers