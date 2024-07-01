import tkinter as tk
from tkinter import messagebox
import random

class ShamirSecret:
    def __init__(self, s, n, t, p):
        self.s = s % p  # The secret
        self.n = n      # The number of shares
        self.t = t      # The threshold (minimum shares required to reconstruct the secret)
        self.p = p      # The prime number used for modulo operations
        self._coef = [random.randint(1, p) for _ in range(t - 1)]  # Generate random coefficients

    def _print_polynomial(self):
        polynomial = f"f(x) = {self.s}"  # Start with the constant term
        for i in range(1, self.t):
            polynomial += f" + {self._coef[i-1]}x^{i}"  # Add each coefficient with its power
        return polynomial

    def generate_shares(self):
        shares = []
        for xi in range(1, self.n + 1):
            share = self.s
            for pow_i in range(1, self.t):
                share += self._coef[pow_i - 1] * xi ** pow_i  # Calculate each share value
            shares.append((xi, share % self.p))  # Append (x, y) share tuple
        return shares

class GenerateSharesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Shamir's Secret Sharing - Generate Shares")
        self.create_widgets()  # Create GUI widgets

    def create_widgets(self):
        # Labels and Entry fields
        tk.Label(self.root, text="Secret:").grid(row=0, column=0)
        self.entry_secret = tk.Entry(self.root)
        self.entry_secret.grid(row=0, column=1)

        tk.Label(self.root, text="Number of Shares:").grid(row=1, column=0)
        self.entry_num_shares = tk.Entry(self.root)
        self.entry_num_shares.grid(row=1, column=1)

        tk.Label(self.root, text="Threshold:").grid(row=2, column=0)
        self.entry_threshold = tk.Entry(self.root)
        self.entry_threshold.grid(row=2, column=1)

        tk.Label(self.root, text="Prime Number:").grid(row=3, column=0)
        self.entry_prime = tk.Entry(self.root)
        self.entry_prime.grid(row=3, column=1)

        # Button to generate shares
        self.btn_generate = tk.Button(self.root, text="Generate Shares", command=self.generate_shares)
        self.btn_generate.grid(row=4, column=0, columnspan=2)

        # Text area to display polynomial and generated shares
        self.text_result = tk.Text(self.root, height=15, width=50)
        self.text_result.grid(row=5, column=0, columnspan=2)

    def generate_shares(self):
        try:
            # Get input values from entry fields
            secret = int(self.entry_secret.get())
            num_shares = int(self.entry_num_shares.get())
            threshold = int(self.entry_threshold.get())
            prime_mod = int(self.entry_prime.get())

            # Create ShamirSecret object with input parameters
            shamir_secret = ShamirSecret(secret, num_shares, threshold, prime_mod)
            polynomial = shamir_secret._print_polynomial()  # Get polynomial representation
            shares = shamir_secret.generate_shares()  # Generate shares using Shamir's Secret Sharing

            # Clear previous result and display new results in text area
            self.text_result.delete(1.0, tk.END)
            self.text_result.insert(tk.END, f"Polynomial: {polynomial}\n\nShares:\n")
            for share in shares:
                self.text_result.insert(tk.END, f"Share {share[0]}: {share[1]}\n")
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter valid numbers")

if __name__ == "__main__":
    root = tk.Tk()
    app = GenerateSharesApp(root)
    root.mainloop()
