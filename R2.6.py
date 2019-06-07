def make_payment(self, amount):
    if amount<0:
        raise ValueError('Negetive Value')
    else:
        self._balance = amount
