# Imports
# import simple_interestv4
# from simple_interestv4 import si
from simple_interestv4 import si as s
# Constants
VLC = "aeiou"
# Function Definitions
def main():
    p = 100000
    r = 0.07
    t = 12
    # print(f"Simple Interest of {p} at {r} rate is {simple_interestv4.si(p,r,t)}")
    # print(f"Simple Interest of {p} at {r} rate is {si(p,r,t)}")
    print(f"Simple Interest of {p} at {r} rate is {s(p,r,t)}")

# Function Calling
if __name__ == '__main__':
    main()