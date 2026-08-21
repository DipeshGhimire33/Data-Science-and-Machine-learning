class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative")

        self._balance = amount

    @balance.deleter
    def balance(self):
        print("Deleting account balance...")
        del self._balance


account = BankAccount("Alice", 1000)

# Getter
print(account.balance)
# 1000

# Setter
account.balance = 1500
print(account.balance)
# 1500

# Invalid setter
account.balance = -500
# ValueError: Balance cannot be negative

# Deleter
del account.balance