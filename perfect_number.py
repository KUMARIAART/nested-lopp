"A PERFECT NUMBER IS A POSITIVE INTEGER THAT IS EQUAL TO THE SUM OF ITS DIVISORS.EXCLUDING THE "
"THE NUMBER ITSELF"

n=int(input("enter the number:"))

i=1
while i<n:
    sum=0
    j=1
    while j<i:
        if i%j==0:
            sum=sum+j
        j=j+1   

    if sum==i:
        print(i,"it is perfect number")
    i+=1
    
    



 


