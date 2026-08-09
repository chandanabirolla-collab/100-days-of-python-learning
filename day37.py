#In Python, the finally keyword defines a block of code inside a try...except structure that always executes, whether an error occurred or not. It is primarily used for cleanup tasks, such as closing files, network connections, or database handles.
try:
    c=[1,3,4,7]
    i=int(input("enter the index:"))
    print(c[i])
except:
    print("invalid index")
finally:
    print("bye,bye...")