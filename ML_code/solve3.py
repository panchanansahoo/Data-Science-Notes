import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)


def generate_data(sigma, n, m):
    X_features = np.random.randn(n, m)
    X = np.hstack((np.ones((n, 1)), X_features))
    beta = np.random.randn(m + 1, 1)
    e = np.random.normal(loc=0.0, scale=sigma, size=(n, 1))
    y = X @ beta + e
    return X, y, beta


def linear_regression_gd(X, y, k, tau, lam):
    n = X.shape[0]
    beta = np.zeros((X.shape[1], 1))
    previous_cost = np.inf

    for _ in range(k):
        predictions = X @ beta
        error = predictions - y
        gradient = (X.T @ error) / n
        beta = beta - lam * gradient

        current_cost = np.sum(error**2) / (2 * n)
        if abs(previous_cost - current_cost) < tau:
            break
        previous_cost = current_cost

    final_predictions = X @ beta
    final_error = final_predictions - y
    final_cost = np.sum(final_error**2) / (2 * n)
    return beta, final_cost


def linear_regression_closed_form(X, y):
    return np.linalg.pinv(X.T @ X) @ X.T @ y


m = 3
runs = 10
sigma = 1
n_values = [10, 50, 100, 500, 1000]

n_errors = []
n_costs = []

for n in n_values:
    beta_errors = []
    costs = []

    for _ in range(runs):
        X, y, true_beta = generate_data(sigma, n, m)
        learned_beta, final_cost = linear_regression_gd(
            X, y, k=10000, tau=1e-8, lam=0.01
        )
        beta_error = np.linalg.norm(true_beta - learned_beta.reshape(-1, 1))
        beta_errors.append(beta_error)
        costs.append(final_cost)

    n_errors.append(np.mean(beta_errors))
    n_costs.append(np.mean(costs))

print("Effect of n")
print("-" * 60)
print(f"{'n':<10} | {'Avg Beta Error':<18} | {'Avg Cost':<15}")
print("-" * 60)

for i in range(len(n_values)):
    print(f"{n_values[i]:<10} | {n_errors[i]:<18.6f} | {n_costs[i]:<15.6f}")

plt.figure()
plt.plot(n_values, n_errors, marker="o")
plt.xlabel("Number of observations (n)")
plt.ylabel("Average Beta Error")
plt.title("Effect of Dataset Size on Beta Learning")
plt.grid(True)

n = 500
sigma_values = [0, 0.5, 1, 2, 5]

sigma_errors = []
sigma_costs = []

for sigma in sigma_values:
    beta_errors = []
    costs = []

    for _ in range(runs):
        X, y, true_beta = generate_data(sigma, n, m)
        learned_beta, final_cost = linear_regression_gd(
            X, y, k=10000, tau=1e-8, lam=0.01
        )
        beta_error = np.linalg.norm(true_beta - learned_beta.reshape(-1, 1))
        beta_errors.append(beta_error)
        costs.append(final_cost)

    sigma_errors.append(np.mean(beta_errors))
    sigma_costs.append(np.mean(costs))

print("\nEffect of sigma")
print("-" * 60)
print(f"{'Sigma':<10} | {'Avg Beta Error':<18} | {'Avg Cost':<15}")
print("-" * 60)

for i in range(len(sigma_values)):
    print(f"{sigma_values[i]:<10} | {sigma_errors[i]:<18.6f} | {sigma_costs[i]:<15.6f}")

plt.figure()
plt.plot(sigma_values, sigma_errors, marker="o")
plt.xlabel("Noise standard deviation (sigma)")
plt.ylabel("Average Beta Error")
plt.title("Effect of Noise on Beta Learning")
plt.grid(True)


X, y, true_beta = generate_data(1, 500, m)
ols_beta = linear_regression_closed_form(X, y)
print("\nClosed-form OLS benchmark")
print(f"True beta: {true_beta.flatten()}")
print(f"OLS beta:  {ols_beta.flatten()}")
print(f"OLS beta error: {np.linalg.norm(true_beta - ols_beta):.6f}")

plt.show()
