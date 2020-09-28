lower=[]
upper=[]
odd=[]
even=[]
x=input()
for i in sorted(x):
    if i.isalpha():
        if i.isupper():
            y=upper
        else:
            y=lower
    else:
        if int(i)%2==0:
            y=even
        else:
            y=odd
    y.append(i)
print("".join(lower+upper+odd+even))