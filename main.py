import random


class ShamirSecret:
    _coef = []

    def __init__(self, s, n, t):
        self.s = s  # The secret
        self.n = n  # The number of shares
        self.t = t  # The number of participants needed to reconstruct the secret

        # Generate the coefficients of the polynomial
        for _ in range(t):
            self._coef.append(random.randint(1, 1000))

    # Generate the shares

    def generate_shares(self):
        shares = []
        for xi in range(1, self.n + 1):
            share = self.s
            for pow_i in range(1, self.t):
                share += self._coef[pow_i - 1] * xi ** pow_i

            shares.append((xi, share))

        return shares
