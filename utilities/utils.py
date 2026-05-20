
def username_extracter(email):
    return email.find("@") and email[:email.find("@")]

def simple_interest(principal, time_in_months, rate_of_interest):
    return (principal * time_in_months * rate_of_interest)/100