''' write a program to find the reverse of the given number'''

def reverse(num):
    rev=0
    while num>0:
        rev=rev*10+num%10
        num//=10
    return rev

def ispalidrome(num):
    return num==reverse(num)
print(reverse(121))
print(ispalidrome(121))

def getpalidrome(start,end):
    res=""
    for i in range(1,end+1):
        if ispalidrome(i):
            res=res+str(i)+"."
    return res
print(getpalidrome(1,1000))
