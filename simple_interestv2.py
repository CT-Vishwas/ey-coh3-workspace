principal = input("Enter the principal amount: ")
principal = float(principal)

rate_of_interest = float(input("Enter the rate of interest in decimal (Eg. 7% is 0.07): "))
time_in_months = int(input("Enter the time in months(Eg. 3 years is 36 months): "))

simple_interest = (principal * time_in_months * rate_of_interest) / 100

# print(simple_interest)
# print("The simple interest is: ", simple_interest)
# print("The simple interest is", simple_interest, sep=":")
# print("The simple interest is", simple_interest, sep=":", end="---")
# print("The simple interest is", simple_interest,sep=":", end="\nThank You\n")
# print("The simple interest is "+str(simple_interest))
# print("The simple interest is %f"%(simple_interest))
# print("The amount %i kept for %i months, at %f rate of interest gives simple interest: %f"%(principal, time_in_months, rate_of_interest, simple_interest))
# print("The amount {} kept for {} months, at {} rate of interest gives simple interest: {}".format(principal, time_in_months, rate_of_interest, simple_interest))
print(f"The amount {principal} kept for {time_in_months} months, at {rate_of_interest:.2f} rate of interest gives simple interest: {simple_interest:.2f}")