# K-MEANS ALGORITHM
import os
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    MAX_ITER = 10000  # 최대 iteration 횟수
    PIC_ITER = 1  # iteration 그림 저장하는 주기

    dir_pic = "./pic"
    if not os.path.exists(dir_pic):
        os.makedirs(dir_pic)

    # STEP 1: LOAD DATA -----------------------------------------------------------------------------------------------#
    data_in = np.load("data_1.npy", allow_pickle=True)
    p = data_in[()]['p']
    num = data_in[()]['num']

    # STEP 2: RUN K-MEANS ---------------------------------------------------------------------------------------------#
    N = np.shape(p)[0]
    K = len(num)


    def euclidean_distance(dot1, dot2):
        x_diff = dot1[0] - dot2[0]
        y_diff = dot1[1] - dot2[1]
        times = x_diff ** 2 + y_diff ** 2
        return np.sqrt(times)


    def get_idx_cluster(p, p_cluster):
        # Write code here!
        idx_cluster = []
        for dot in p:
            distanceList = []
            for _cluster in p_cluster:
                distanceList.append(euclidean_distance(dot, _cluster))
            idx_cluster.append(distanceList.index(min(distanceList)))

        return idx_cluster


    def update_p_cluster(p, p_cluster, idx_cluster):
        # Write code here!
        # numOfCluster = len(p_cluster)
        # zeros = [0, 0]
        # new_p_cluster = []
        # for i in range(numOfCluster):
        #     new_p_cluster.append(zeros)
        #
        # for dot, cluster in zip(p, idx_cluster):
        #     new_p_cluster[cluster] = dot + new_p_cluster[cluster]
        #
        # out_cluster = []
        # newX = 0
        # newY = 0
        # for i in range(numOfCluster):
        #     idx = idx_cluster.count(i)
        #     if idx == 0:
        #         out_cluster.append([0, 0])
        #     else:
        #         avg = [new_p_cluster[i][0] / idx, new_p_cluster[i][1] / idx]
        #         out_cluster.append(avg)
        num_k = np.shape(p_cluster)[0]

        for i in range(num_k):
            idx_tmp = np.where(idx_cluster == i)
            idx_tmp = idx_tmp[0]

            if len(idx_tmp) > 0:
                p_sel = p[idx_tmp, :]
                p_cluster_new = np.mean(p_sel, axis=0)
                p_cluster[i, :] = p_cluster_new

        return p_cluster


    def plot_data(p, p_cluster, idx_cluster, dir_pic, iter):
        num_k = np.shape(p_cluster)[0]
        hcolor = ['r', 'g', 'b']

        fig1, ax1 = plt.subplots(1, figsize=(9, 7), constrained_layout=True)
        for i in range(num_k):
            idx_tmp = np.where(idx_cluster == i)
            idx_tmp = idx_tmp[0]

            if len(idx_tmp) > 0:
                p_sel = p[idx_tmp, :]
                ax1.plot(p_sel[:, 0], p_sel[:, 1], 'o', color=hcolor[i], markersize=3.0)
                ax1.plot(p_cluster[i, 0], p_cluster[i, 1], '^', color=hcolor[i], markersize=9.0)

        ax1.axis('equal')
        plt.show(block=False)

        if iter < 0:
            filename2save = "{:s}/kmeans_init.png".format(dir_pic)
        else:
            filename2save = "{:s}/kmeans_{:d}.png".format(dir_pic, iter)
        plt.savefig(filename2save)
        plt.pause(0.2)

        plt.close(fig1)


    # Run algorithm
    p_cluster = np.random.rand(K, 2)  # 초기 cluster 중심점
    idx_cluster = np.zeros(N)  # 초기 각 데이터별 cluster-index

    plot_data(p, p_cluster, idx_cluster, dir_pic, -1)  # 초기 결과
    for iter in range(MAX_ITER):
        print("{:d}".format(iter))

        # 이전 idx_cluster
        idx_cluster_old = np.copy(idx_cluster)

        # Centroid와 얼마나 가까운지를 기준으로 cluster를 구한다
        idx_cluster = get_idx_cluster(p, p_cluster)

        # 새로운 cluster의 중심값을 업데이트
        p_cluster = update_p_cluster(p, p_cluster, idx_cluster)

        # Plot
        if iter % PIC_ITER == 0:
            plot_data(p, p_cluster, idx_cluster, dir_pic, iter)  # 중간 결과 저장

        # idx_cluster의 변화가 없으면 iteration 종료
        diff_idx = np.abs(idx_cluster - idx_cluster_old)
        val_end = np.amax(diff_idx)
        if val_end == 0:
            is_success = True
            break

    print("END")
    quit()
