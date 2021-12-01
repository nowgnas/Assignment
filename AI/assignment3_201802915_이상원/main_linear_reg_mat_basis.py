# LINEAR REGRESSION MODEL (Inverse Matrix + Nonlinear Basis)

import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # STEP 1: SET DATA ------------------------------------------------------------------------------------------------#
    data_x = np.linspace(1.0, 10.0, 100)[:, np.newaxis]
    data_y = np.sin(data_x) + 0.1 * np.power(data_x, 2) + 0.5 * np.random.randn(100,
                                                                                1)
    data_x /= np.max(data_x)

    data_x = np.hstack((np.ones_like(data_x), data_x))

    # Set train & test data
    order = np.random.permutation(len(data_x))
    portion = 20
    x_test = data_x[order[:portion]]
    y_test = data_y[order[:portion]]
    x_train = data_x[order[portion:]]
    y_train = data_y[order[portion:]]


    # STEP 2: DO PREDICTION -------------------------------------------------------------------------------------------#
    # Nonlinear basis function
    def get_fraction(x, mu, s):
        x_mu = (x - mu) ** 2
        div_x = x_mu / (2 * (s ** 2))
        return -div_x


    def apply_exp_basis(X, s=0.5):
        # Write code here (1)!
        out_list = []
        mu = [0.0, 0.2, 0.4, 0.6]
        idx_list = []
        for i in X:
            x = i[1]
            idx_list.append(i[0])
            for _mu in mu:
                get_phi = get_fraction(x, _mu, s)
                idx_list.append(get_phi)
            out_list.append(idx_list)
            idx_list = []
        return out_list


    phi_train = apply_exp_basis(x_train)
    x_T = np.transpose(phi_train)
    X_X_T = np.matmul(x_T, phi_train)
    x_inv = inv(X_X_T)
    x_inv_X = np.matmul(x_inv, x_T)

    # Write code here (2)!

    # Find theta_hat.
    theta_hat = np.matmul(x_inv_X, y_train)

    phi_test = apply_exp_basis(x_test)
    y_pred = np.matmul(phi_test, theta_hat)

    # STEP 3: PLOT ----------------------------------------------------------------------------------------------------#
    ax = plt.figure(figsize=(9, 7), constrained_layout=True).subplots(1, 1)
    ax.plot(x_test[:, 1], y_test, 'bo', label='Ground-truth')
    ax.plot(x_test[:, 1], y_pred, 'ro', label='Prediction')
    plt.legend()
    plt.show()
