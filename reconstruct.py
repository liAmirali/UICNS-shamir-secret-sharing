class ReconstructShamirSecret:
    def __init__(self, t, n, p, shares):
        self.t = t
        self.n = n
        self.p = p
        self.shares = shares

    def _lagrange_interpolation(self, input, x, y):
        result = 0
        for i in range(len(y)):
            term = 1
            for j in range(len(y)):
                if i == j:
                    continue
                multiplicative_inverse_denominator = pow(x[i] - x[j], -1, self.p)
                term *= (input -  x[j]) * multiplicative_inverse_denominator
            term *= y[i]
            result = (result + term) % self.p

        return result
    
    def reveal_secret(self):
        x = [x for x, y in self.shares]
        y = [y for x, y in self.shares]
        return self._lagrange_interpolation(0, x, y)


def main():
    print("Welcome to Shamir's Secret Reconstruction")
    threshold = int(input("Enter the threshold number of shares needed to reconstruct the secret: "))
    num_shares = int(input("Enter the total number of shares: "))
    prime_mod = int(input("Enter the prime number for modulo operations: "))
    
    shares = []
    print(f"\nEnter the {threshold} shares (in the format x y):")
    for _ in range(threshold):
        x, y = map(int, input().split())
        shares.append((x, y))
    
    reconstruct = ReconstructShamirSecret(threshold, num_shares, prime_mod, shares)
    secret = reconstruct.reveal_secret()
    print(f"\nThe reconstructed secret is: {secret}")


if __name__ == "__main__":
    main()
