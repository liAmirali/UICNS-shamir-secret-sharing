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
                term *= (input -  x[j]) / (x[i] - x[j])
            term *= y[i]
            result = (result + term) % self.p

        return result
