# Some part of this code is generated with the help of ChatGPT and Copilot

import tkinter as tk
from tkinter import messagebox
import random

class ShamirSecret:
    def __init__(self, s, n, t, p):
        self.s = s % p  # The secret
        self.n = n      # The number of shares
        self.t = t      # The number of participants needed to reconstruct the secret
        self.p = p      # The modulo of numbers
        self._coef = [random.randint(1, p) for _ in range(t - 1)]

    def _print_polynomial(self):
        polynomial = f"f(x) = {self.s}"
        for i in range(1, self.t):
            polynomial += f" + {self._coef[i-1]}x^{i}"
        return polynomial

    def generate_shares(self):
        shares = []
        for xi in range(1, self.n + 1):
            share = self.s
            for pow_i in range(1, self.t):
                share += self._coef[pow_i - 1] * xi ** pow_i
            shares.append((xi, share % self.p))
        return shares

def generate_shares():
    try:
        secret = int(entry_secret.get())
        num_shares = int(entry_num_shares.get())
        threshold = int(entry_threshold.get())
        prime_mod = int(entry_prime.get())

        shamir_secret = ShamirSecret(secret, num_shares, threshold, prime_mod)
        polynomial = shamir_secret._print_polynomial()
        shares = shamir_secret.generate_shares()

        text_result.delete(1.0, tk.END)
        text_result.insert(tk.END, f"Polynomial: {polynomial}\n\nShares:\n")
        for share in shares:
            text_result.insert(tk.END, f"Share {share[0]}: {share[1]}\n")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers")

app = tk.Tk()
app.title("Shamir's Secret Sharing - Generate Shares")

tk.Label(app, text="Secret:").grid(row=0, column=0)
entry_secret = tk.Entry(app)
entry_secret.grid(row=0, column=1)

tk.Label(app, text="Number of Shares:").grid(row=1, column=0)
entry_num_shares = tk.Entry(app)
entry_num_shares.grid(row=1, column=1)

tk.Label(app, text="Threshold:").grid(row=2, column=0)
entry_threshold = tk.Entry(app)
entry_threshold.grid(row=2, column=1)

tk.Label(app, text="Prime Number:").grid(row=3, column=0)
entry_prime = tk.Entry(app)
entry_prime.grid(row=3, column=1)

btn_generate = tk.Button(app, text="Generate Shares", command=generate_shares)
btn_generate.grid(row=4, column=0, columnspan=2)

text_result = tk.Text(app, height=15, width=50)
text_result.grid(row=5, column=0, columnspan=2)

app.mainloop()
