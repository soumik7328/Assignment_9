#Assignment - 9 Full Stack Web Development using Python MySirG While Loop
#1. Write a python script to print MySirG N times on the screen
j=1
i=eval(input("How many time you want to print MySirG:-"))
while(j<=i):
    print("MySirG")
    j=j+1
#2. Write a python script to print first N natural numbers
j=1
i=eval(input("How many first N natural numbers you want to print:-"))
while(j<=i):
    print(j)
    j=j+1
#3. Write a python script to print first N natural numbers in reverse order
j=1
i=eval(input("How many first N natural numbers you want to print in reverse order:-"))
while(i>=j):
    print(i)
    i=i-1
#4. Write a python script to print first N odd natural numbers
j=1
i=eval(input("How many first N odd natural numbers want to print:-"))
e=i*2
while(j<=e):
    if(j%2==1):
        print(j)
    j=j+1
#5. Write a python script to print first N odd natural numbers in reverse order
j=1
i=eval(input("How many first N odd natural numbers want to print in reverse order:-"))
k=i*2
while(k>=j):
    if(k%2==1):
        print(k)
        
    k=k-1 
        
#6. Write a python script to print first N even natural numbers
j=1
i=eval(input("How many first N even natural numbers want to print:-"))
e=i*2
while(j<=e):
    if j%2==0:
        print(j)
    j=j+1
    
#7. Write a python script to print first N even natural numbers in reverse order
j=1
i=eval(input("How many first N even natural numbers want to print in reverse order:-"))
e=i*2
while(e>=j):
    if e%2==0:
        print(e)
    e=e-1
#8. Write a python script to print squares of first N natural numbers
j=1
i=eval(input("How many first N natural numbers squares you want to print:-"))
while(j<=i):
    print(j**2)
    j=j+1
#9. Write a python script to print cubes of first N natural numbers
j=1
i=eval(input("How many first N natural numbers squares you want to print:-"))
while(j<=i):
    print(j**3)
    j=j+1 
#10. Write a python script to print first 10 multiples of N
j=1
i=eval(input("Enter a number whose first 10 multiples you want:-"))
while j<=10:
    print(j*i)
    j=j+1