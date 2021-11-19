# LINEAR REGRESSION MODEL (Inverse Matrix)

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
    # Write code here!
    x_T = np.transpose(x_train)
    X_X_T = np.matmul(x_T, x_train)
    x_inv = inv(X_X_T)
    x_inv_X = np.matmul(x_inv, x_T)
    theta_hat = np.matmul(x_inv_X, y_train)
    # Find theta_hat.
    y_pred = np.matmul(x_test, theta_hat)

    # STEP 3: PLOT ----------------------------------------------------------------------------------------------------#
    idx_min = np.argmin(x_test[:, 1])
    idx_max = np.argmax(x_test[:, 1])
    ax = plt.figure(figsize=(9, 7), constrained_layout=True).subplots(1, 1)
    ax.plot(x_test[:, 1], y_test, 'bo', label='Ground-truth')
    ax.plot(x_test[:, 1], y_pred, 'ro', label='Prediction')
    ax.plot([x_test[idx_min, 1], x_test[idx_max, 1]],
            [y_pred[idx_min], y_pred[idx_max]], 'r-')
    plt.legend()
    plt.show()
