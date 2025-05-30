# custom exception for insuficient funs

class InsuficientFundsError(Exception):
    def __init__(self, balance, amount):
        super().__init__(f"Insuficient funds: Balance is {balance}, but {amount} was requested.")
        self.balance = balance
        self.amount = amount

car_price = 20000
balance = 50000  # replace 50000 with 50

if balance < car_price:
    raise InsuficientFundsError(balance, car_price)
print("Yes! I can buy the car!")

        