## README

### Shamir's Secret Sharing Project

This project implements Shamir's Secret Sharing scheme in Python. It includes two console applications: one for generating shares of a secret and another for reconstructing the secret from the shares.

### Features

- Generate shares from a secret using a polynomial.
- Reconstruct the secret from the shares using Lagrange interpolation.

### Prerequisites

- Python 3.8 and above

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/liamirali/UICNS-shamir-secret-sharing.git
    ```

2. Navigate to the project directory:

    ```bash
    cd UICNS-shamir-secret-sharing
    ```

### Usage

#### Generating Shares

To generate shares, run the `generate_shares.py` script:

```bash
python generate_shares.py
```

You will be prompted to enter the secret number, the number of shares, the threshold number of shares needed to reconstruct the secret, and a prime number for modulo operations. The script will print the generated polynomial and the shares.

### Reconstructing the Secret
To reconstruct the secret, run the **reconstruct_secret.py** script:
```bash
python python reconstruct_secret.py
```

You will be prompted to enter the threshold number of shares, the total number of shares, and the prime number for modulo operations. Then, you will need to enter the shares in the format **x**, **y**. The script will reconstruct and print the secret.


