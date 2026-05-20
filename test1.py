
def si(principal, rate, time_in_months):
    return (principal * time_in_months * rate) / 100


p = 100
t = 10
r = 0.07
print(si(p,r,t))
