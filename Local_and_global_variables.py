# here v is a global variable
v= 4

def func():
    # here v is a local variable
    v=("I am learning Python")
    print(v)
func()
print(v)