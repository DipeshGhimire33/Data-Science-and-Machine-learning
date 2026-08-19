import time

total_amount = 2560

class InsufficientAmount(Exception):
    pass

def get_cash(withdraw_amt):
    if total_amount >= withdraw_amt:
        print("Sufficient balance available. Wait a moment.")
        time.sleep(3)
        print("Thank you for using us.")
        
    else:
        raise InsufficientAmount("Insufficient amount available.")
    
get_cash(1500)
# get_cash(3000)