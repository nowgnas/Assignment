# LINEAR REGRESSION MODEL (Gradient Descent)

import numpy as np
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


    # STEP 2: SET PLOT FUNCTION ---------------------------------------------------------------------------------------#
    def plot_per_iter(X, Y, Y_hat, iter):
        idx_min = np.argmin(X[:, 1])
        idx_max = np.argmax(X[:, 1])
        fig, ax = plt.subplots(1, figsize=(9, 7), constrained_layout=True)
        ax.plot(X[:, 1], Y, 'bo', label='Ground-truth')
        ax.plot(X[:, 1], Y_hat, 'ro', label='Prediction')
        ax.plot([X[idx_min, 1], X[idx_max, 1]], [Y_hat[idx_min], Y_hat[idx_max]],
                'r-')
        ax.set_xlim([X[idx_min, 1] - 0.1, X[idx_max, 1] + 0.1])
        ax.set_ylim([Y[idx_min] - 0.1, Y[idx_max] + 0.1])
        ax.set_title("Iteration: {:d}".format(iter))
        plt.legend()
        plt.show(block=False)

        filename2save = "./linear_reg_grad_{:d}.png".format(iter)
        plt.savefig(filename2save)
        plt.close()


    def f(x):
        return x ** 2


    def difference(f, x, h=0.001):
        return (f(x + h) - f(x)) / h


    # STEP 3: DO GRADIENT DESCENT -------------------------------------------------------------------------------------#
    def get_gradient(theta, X, Y):
        # Write code here!
        get_mse = 0
        # mse 계산
        for x, y in zip(X, Y):
            theta_T_x = np.matmul(np.transpose(theta), x)
            y_theta = y - theta_T_x
            square = y_theta ** 2
            get_mse += square
        mse = get_mse / len(X)

        # gradient 계산
        gradient = difference(f, mse)

        return gradient, mse


    theta_hat = np.random.randn(2, 1)  # theta_hat 초기값을 random하게 정한다.
    alpha = 0.5
    tolerance = 1e-5

    # Perform Gradient Descent
    iter_cnt = 1  # Iteration count
    while True:
        gradient, loss = get_gradient(theta_hat, x_train,
                                      y_train)  # 매 iteration마다 grad와 loss계산
        theta_hat_new = theta_hat - alpha * gradient  # theta update

        # Stopping Condition
        if (np.sum(abs(theta_hat_new - theta_hat)) < tolerance) or (iter_cnt > 200):
            print("Converged.")
            break

        # Show iteration procedure
        if (iter_cnt % 20 == 0) or (iter_cnt < 10):
            print("Iteration: %d - Loss: %.4f" % (iter_cnt, loss))
            # Plot
            y_pred = np.matmul(x_test, theta_hat_new)
            plot_per_iter(x_test, y_test, y_pred, iter_cnt)

        iter_cnt += 1
        theta_hat = theta_hat_new

    print("theta =", theta_hat)
    print("Test Loss =", get_gradient(theta_hat, x_test, y_test)[1])
