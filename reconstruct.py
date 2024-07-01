import tkinter as tk
from tkinter import messagebox

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
                term *= (input - x[j]) * multiplicative_inverse_denominator
            term *= y[i]
            result = (result + term) % self.p
        return result
    
    def reveal_secret(self):
        x = [x for x, y in self.shares]
        y = [y for x, y in self.shares]
        return self._lagrange_interpolation(0, x, y)

def reconstruct_secret():
    try:
        threshold = int(entry_threshold.get())
        prime_mod = int(entry_prime.get())

        shares_input = text_shares.get(1.0, tk.END).strip().split("\n")
        shares = [(int(x.split()[0]), int(x.split()[1])) for x in shares_input if x]

        if len(shares) < threshold:
            messagebox.showerror("Invalid input", "Not enough shares provided")
            return

        reconstruct = ReconstructShamirSecret(threshold, len(shares), prime_mod, shares)
        secret = reconstruct.reveal_secret()

        text_result.delete(1.0, tk.END)
        text_result.insert(tk.END, f"Reconstructed Secret: {secret}\n")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers")
    except Exception as e:
        messagebox.showerror("Error", str(e))

app = tk.Tk()
app.title("Shamir's Secret Sharing - Reconstruct Secret")

tk.Label(app, text="Threshold:").grid(row=0, column=0)
entry_threshold = tk.Entry(app)
entry_threshold.grid(row=0, column=1)

tk.Label(app, text="Prime Number:").grid(row=1, column=0)
entry_prime = tk.Entry(app)
entry_prime.grid(row=1, column=1)

tk.Label(app, text="Shares (x y):").grid(row=2, column=0, columnspan=2)
text_shares = tk.Text(app, height=10, width=50)
text_shares.grid(row=3, column=0, columnspan=2)

btn_reconstruct = tk.Button(app, text="Reconstruct Secret", command=reconstruct_secret)
btn_reconstruct.grid(row=4, column=0, columnspan=2)

text_result = tk.Text(app, height=5, width=50)
text_result.grid(row=5, column=0, columnspan=2)

app.mainloop()
