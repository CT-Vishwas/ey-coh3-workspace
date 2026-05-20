# Import Statements

# Constant Definitions
m = 100
n = 200
# Function Definitions
def display_greeting(nme):
    global n
    n = 75
    print(f"Value of n is {n} inside display greeting")
    print(f"Value of m is {m} inside display greeting")
    print("Hello World", nme)

def add(a,b):
    print(f"Value of n is {n}  inside add")
    print(f"Value of m is {m}  inside add")
    return a+b

# Function Calling
print(f"Value of m is {m} ")
print(f"Value of n is {n}")

print("Iam outside function definition")
display_greeting("Vishwas")
print(add(23,45))

print(f"Value of n is {n}")
print(f"Value of m is {m}")