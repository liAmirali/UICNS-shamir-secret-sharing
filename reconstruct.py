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


reconstruct = ReconstructShamirSecret(3, 5, 13, [(1, 4), (2, 8), (5, 6)])
print(reconstruct._lagrange_interpolation(0, [1, 2, 5], [4, 8, 6]))