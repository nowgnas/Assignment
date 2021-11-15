# LINEAR REGRESSION MODEL (Inverse Matrix + Nonlinear Basis)

import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt


if __name__ == '__main__':
    # STEP 1: SET DATA ------------------------------------------------------------------------------------------------#
    data_x = np.linspace(1.0, 10.0, 100)[:, np.newaxis]
    data_y = np.sin(data_x) + 0.1 * np.power(data_x, 2) + 0.5 * np.random.randn(100, 1)
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
    def apply_exp_basis(X, s=0.5):
        # Write code here (1)!

        Phi = np.copy(X)  # 코드 작성시 이부분을 지우세요!
        return Phi

    phi_train = apply_exp_basis(x_train)

    # Write code here (2)!


    # Find theta_hat.
    theta_hat = np.ones((2, 1))  # 코드 작성시 이부분을 지우세요!

    phi_test = apply_exp_basis(x_test)
    y_pred = np.matmul(phi_test, theta_hat)

    # STEP 3: PLOT ----------------------------------------------------------------------------------------------------#
    ax = plt.figure(figsize=(9, 7), constrained_layout=True).subplots(1, 1)
    ax.plot(x_test[:, 1], y_test, 'bo', label='Ground-truth')
    ax.plot(x_test[:, 1], y_pred, 'ro', label='Prediction')
    plt.legend()
    plt.show()



