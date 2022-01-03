n=int(input("Enter N value:"))
t=n
r=0
while(n>0):
    d=n%10
    r=r*10+d
    n=n//10
if(t==r):
    print("The number is palindrome!")
else:
    print(" Given number is not a palindrome..!")