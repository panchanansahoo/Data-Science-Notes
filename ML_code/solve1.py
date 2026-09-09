import numpy as np


def generate_data(sigma, n, m):

    X_independent = np.random.randn(n, m)

    X = np.hstack((np.ones((n, 1)), X_independent))

    beta = np.random.randn(m + 1, 1)

    e = np.random.normal(loc=0.0, scale=sigma, size=(n, 1))

    y = X @ beta + e

    return X, y, beta


sigma = 2.5
n = 50
m = 4

X, y, beta = generate_data(sigma, n, m)


assert X.shape == (n, m + 1)
assert y.shape == (n, 1)
assert beta.shape == (m + 1, 1)


assert np.all(X[:, 0] == 1)


residuals = y - X @ beta

print("X shape:", X.shape)
print("y shape:", y.shape)
print("beta shape:", beta.shape)
print("Residual mean:", np.mean(residuals))
print("Residual std:", np.std(residuals))
