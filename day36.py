#exception handling
a=input("enter the number:")
print(f"multiplication of {a} is")
try:
   for i in range(1,10):
    print(f"{int(a)} X {i}= {int(a)*i}")
except:
    print("invalid input")
print("byee")