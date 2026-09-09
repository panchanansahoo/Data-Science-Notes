import numpy as np


def generate_data(sigma, n, m):

    X_features = np.random.randn(n, m)

    X = np.hstack((np.ones((n, 1)), X_features))

    beta = np.random.randn(m + 1, 1)

    e = np.random.normal(loc=0.0, scale=sigma, size=(n, 1))

    y = X @ beta + e

    return X, y, beta


def linear_regression_gd(X, y, k, tau, lam):

    n = X.shape[0]

    beta = np.random.randn(X.shape[1], 1)

    predictions = X @ beta

    error = predictions - y
    previous_cost = np.sum(error**2) / (2 * n)

    current_cost = previous_cost

    for _ in range(k):

        gradient = (X.T @ (predictions - y)) / n

        beta = beta - lam * gradient

        predictions = X @ beta

        error = predictions - y
        current_cost = np.sum(error**2) / (2 * n)

        if abs(current_cost - previous_cost) < tau:
            break

        previous_cost = current_cost

    return beta, current_cost


sigma = 0
n = 100
m = 2


X, y, true_beta = generate_data(sigma, n, m)


learned_beta, final_cost = linear_regression_gd(X, y, k=10000, tau=0.000001, lam=0.01)

print("True beta:")
print(true_beta)

print("\nLearned beta:")
print(learned_beta)

print("\nFinal cost:")
print(final_cost)
