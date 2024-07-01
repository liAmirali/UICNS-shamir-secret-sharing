import random


class ShamirSecret:
    _coef = []

    def __init__(self, s, n, t, p):
        self.s = s % p  # The secret
        self.n = n      # The number of shares
        self.t = t      # The number of participants needed to reconstruct the secret
        self.p = p      # The mode of numbers

        # Generate the coefficients of the polynomial
        for _ in range(t - 1):
            self._coef.append(random.randint(1, p))

    def _print_polynomial(self):
        print(f"f(x) = {self.s}", end="")
        for i in range(1, self.t):
            print(f" + {self._coef[i-1]}x^{i}", end="")
        print()

    # Generate the shares
    def generate_shares(self):
        shares = []
        for xi in range(1, self.n + 1):
            share = self.s
            for pow_i in range(1, self.t):
                share += self._coef[pow_i - 1] * xi ** pow_i

            shares.append((xi, share % self.p))

        return shares


shamir_secret = ShamirSecret(1005, 10, 6, 100)
shamir_secret._print_polynomial()
shares = shamir_secret.generate_shares()
print(shares)
