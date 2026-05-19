
principal = input("Enter the principal amount: ")
principal = float(principal)

rate_of_interest = list(map(float,input("Enter the rates of interest in decimal (Eg. 7% is 0.07) seperated by spaces: ").split()))
time_in_months = int(input("Enter the time in months(Eg. 3 years is 36 months): "))

interest_list = []
for rate in rate_of_interest:
    simple_interest = (principal * time_in_months * rate) / 100
    interest_list.append(simple_interest)
    print(f"The amount {principal} kept for {time_in_months} months, at {rate:.2f} rate of interest gives simple interest: {simple_interest:.2f}")
print("Calculations completed successfully....")