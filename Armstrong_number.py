"ARMSTRONG NUMBER IS A NUMBER THAT IS EQUAL TO THE SUM OF CUBES OF ITS DIGITS"

num1=int(input("enter the number"))  
j=num1
count=0
while j>0:
    count=count+1
    j=j//10
sum=0
j=num1
while j>0:
    digit=j%10
    x=1
    pro=1
    while x<=count:
        pro=pro*digit
        x=x+1
    sum=sum+pro
    j=j//10
if sum==num1:
    print("number is armstrong",sum) 
else:
    print("number is not a armstrong",sum) 