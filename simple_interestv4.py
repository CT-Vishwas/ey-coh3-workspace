
def si(principal, rate, time_in_months):
    return (principal * time_in_months * rate) / 100


if __name__ == '__main__':
    principal = input("Enter the principal amount: ")
    principal = float(principal)

    #rate_of_interest = list(map(float,input("Enter the rates of interest in decimal (Eg. 7% is 0.07) seperated by spaces: ").split()))
    rate_of_interest = input("Enter the rates of interest in decimal (Eg. 7% is 0.07) seperated by spaces: ") # String seperated by spaces
    rate_of_interest = rate_of_interest.split() # list of strings
    rate_of_interest = map(float, rate_of_interest) # Map of floats
    rate_of_interest = list(rate_of_interest) # list of floats


    time_in_months = int(input("Enter the time in months(Eg. 3 years is 36 months): "))

    interest_list = []
    for rate in rate_of_interest:
        simple_interest = si(principal,rate, time_in_months)
        interest_list.append(simple_interest)
        print(f"The amount {principal} kept for {time_in_months} months, at {rate:.2f} rate of interest gives simple interest: {simple_interest:.2f}")

    print("Calculations completed successfully....")