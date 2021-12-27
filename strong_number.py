"A STRONG NUMBER IS A SPECIAL NUMBER WHOSE SUM OF THE ALL DIGIT FACTORIAL SHOULD BE EQUAL"
"TO THE NUMBER ITSELF"

num1=int(input("enter the number"))
i=0
while i<num1:
    x=1
    y=0
    while i>x:
        a=i%10
        b=(i//10)%10
        c=(i//10)//10
        d=a+b+c
        if d%10==0:
            print(i,"is a strong number")
        x=x+i      
    i=i+1

