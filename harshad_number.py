


# num=int(input("enter any number:"))
# a=num
# sum=0
# while a>0:
#     b=num%10
#     sum=sum+b
#     a=a//10
# a=a+1    
# if num%sum==0:
#     print(num,"is a harshad number")
# else:
#     print(num,"is not a harshad number")    



num=int(input("enter any number:"))        
a=num
while num>0:
    sum=0
    j=0
    while j<num:
        b=num%10
        sum=sum+b
        num=num//10
    j=j+1         
    if a%sum==0:
        print(a,"is a harshad number")    
    else:
        print(a,"is not a harshad number")