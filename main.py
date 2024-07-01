import random


class ShamirSecret:
    _coef = []

    def __init__(self, s, n, t):
        self.s = s # The secret
        self.n = n # The number of shares
        self.t = t # The number of participants needed to reconstruct the secret

        # Generate the coefficients of the polynomial
        for i in range(t):
            self._coef.append(random.randint(1, 1000))

