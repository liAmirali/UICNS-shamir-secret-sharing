import tkinter as tk
from tkinter import messagebox

class ReconstructShamirSecret:
    def __init__(self, t, n, p, shares):
        self.t = t  # Threshold (minimum shares required to reconstruct the secret)
        self.n = n  # Total number of shares provided
        self.p = p  # Prime number used for modulo operations
        self.shares = shares  # List of (x, y) shares provided

    def _lagrange_interpolation(self, input, x, y):
        result = 0
        for i in range(len(y)):
            term = 1
            for j in range(len(y)):
                if i == j:
                    continue
                multiplicative_inverse_denominator = pow(x[i] - x[j], -1, self.p)
                term *= (input - x[j]) * multiplicative_inverse_denominator
            term *= y[i]
            result = (result + term) % self.p
        return result

    def reveal_secret(self):
        x = [x for x, y in self.shares]
        y = [y for x, y in self.shares]
        return self._lagrange_interpolation(0, x, y)

class ReconstructSecretApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Shamir's Secret Sharing - Reconstruct Secret")
        self.create_widgets()  # Create GUI widgets

    def create_widgets(self):
        # Labels and Entry fields
        tk.Label(self.root, text="Threshold:").grid(row=0, column=0)
        self.entry_threshold = tk.Entry(self.root)
        self.entry_threshold.grid(row=0, column=1)

        tk.Label(self.root, text="Prime Number:").grid(row=1, column=0)
        self.entry_prime = tk.Entry(self.root)
        self.entry_prime.grid(row=1, column=1)

        # Text area for entering shares (x, y)
        tk.Label(self.root, text="Shares (x y):").grid(row=2, column=0, columnspan=2)
        self.text_shares = tk.Text(self.root, height=10, width=50)
        self.text_shares.grid(row=3, column=0, columnspan=2)

        # Button to reconstruct secret
        self.btn_reconstruct = tk.Button(self.root, text="Reconstruct Secret", command=self.reconstruct_secret)
        self.btn_reconstruct.grid(row=4, column=0, columnspan=2)

        # Text area to display reconstructed secret
        self.text_result = tk.Text(self.root, height=5, width=50)
        self.text_result.grid(row=5, column=0, columnspan=2)

    def reconstruct_secret(self):
        try:
            # Get input values from entry fields
            threshold = int(self.entry_threshold.get())
            prime_mod = int(self.entry_prime.get())

            # Read shares input from text area
            shares_input = self.text_shares.get(1.0, tk.END).strip().split("\n")
            shares = [(int(x.split()[0]), int(x.split()[1])) for x in shares_input if x]

            # Validate if enough shares are provided
            if len(shares) < threshold:
                messagebox.showerror("Invalid input", "Not enough shares provided")
                return

            # Create ReconstructShamirSecret object with input parameters
            reconstruct = ReconstructShamirSecret(threshold, len(shares), prime_mod, shares)
            secret = reconstruct.reveal_secret()  # Reveal the reconstructed secret

            # Clear previous result and display reconstructed secret in text area
            self.text_result.delete(1.0, tk.END)
            self.text_result.insert(tk.END, f"Reconstructed Secret: {secret}\n")
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter valid numbers")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = ReconstructSecretApp(root)
    root.mainloop()
