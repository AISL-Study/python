def square(first,second):
    value=first ** second
    return value
    
def gcd(first, second):
    i=1
    while i<=int(first) and i<= int(second):
        if int(first) % i == 0 and int(second) % i == 0:
            value =i
        i=i+1
    
    if value == 1:
        return "두 수는 서로소 입니다. "
    else:
        return print(value)