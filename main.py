import random


class ShamirSecret:
    _coef = []

    def __init__(self, s, n, t, p):
        self.s = s % p  # The secret
        self.n = n      # The number of shares
        self.t = t      # The number of participants needed to reconstruct the secret
        self.p = p      # The modulo of numbers

        # Generate the coefficients of the polynomial
        self._coef = [random.randint(1, p) for _ in range(t - 1)]

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


def main():
    print("Welcome to Shamir's Secret Sharing Scheme")
    secret = int(input("Enter the secret number: "))
    num_shares = int(input("Enter the number of shares: "))
    threshold = int(input("Enter the threshold number of shares needed to reconstruct the secret: "))
    prime_mod = int(input("Enter a prime number for modulo operations: "))

    shamir_secret = ShamirSecret(secret, num_shares, threshold, prime_mod)
    print("\nGenerated Polynomial:")
    shamir_secret._print_polynomial()
    
    shares = shamir_secret.generate_shares()
    print("\nGenerated Shares:")
    for share in shares:
        print(f"Share {share[0]}: {share[1]}")

if __name__ == "__main__":
    main()