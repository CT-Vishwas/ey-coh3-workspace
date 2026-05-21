
def username_extracter(email: str) -> str:
    '''
    Returns the username or -1 if invalid email
    '''
    return email.find("@") and email[:email.find("@")]

def simple_interest(principal: float, time_in_months: int, rate_of_interest: float) -> float:
    '''
    Returns the simple interest using si = ptr/100
    '''
    return (principal * time_in_months * rate_of_interest)/100