import matplotlib.pyplot as plt
import utils as u
from pylab import rcParams
rcParams['figure.figsize'] = 15, 15

plt.style.use('ggplot')

c = [0.1, 0.25, 0.5, 0.75, 1.0]
for connectivity in c:
    bf_r = u.read_test_result("results/bellman-ford-%.2f.txt"%connectivity)

    f, axarr = plt.subplots(2, sharex=True)
    axarr[0].plot(bf_r[0], bf_r[1], color="blue")
    axarr[0].set_ylabel('Duration', fontsize=18)
    axarr[0].set_title('Bellman-Ford on graph with connectivity %.2f'%connectivity)
    axarr[1].plot(bf_r[0], bf_r[2], color="blue")
    axarr[1].set_ylabel('No of operations', fontsize=18)
    axarr[1].set_xlabel('No of vertices', fontsize=18)

    plt.savefig('images/bf_%.2f.png'%connectivity, dpi=300)

    fw_r = u.read_test_result("results/floyd-warshall-%.2f.txt"%connectivity)

    f, axarr = plt.subplots(2, sharex=True)
    axarr[0].plot(fw_r[0], fw_r[1], color="green")
    axarr[0].set_ylabel('Duration', fontsize=18)
    axarr[0].set_title('Floyd-Warshall on graph with connectivity %.2f'%connectivity)
    axarr[1].plot(fw_r[0], fw_r[2], color="green")
    axarr[1].set_ylabel('No of operations', fontsize=18)
    axarr[1].set_xlabel('No of vertices', fontsize=18)

    plt.savefig('images/fw_%.2f.png'%connectivity, dpi=300)


    f, axarr = plt.subplots(2, sharex=True)
    axarr[0].plot(bf_r[0], bf_r[1], color="blue")
    axarr[0].plot(fw_r[0], fw_r[1], color="green")
    axarr[0].set_ylabel('Duration', fontsize=18)
    axarr[0].set_title('Both algorithms on graph with connectivity %.2f'%connectivity)
    axarr[1].plot(bf_r[0], bf_r[2], color="blue")
    axarr[1].plot(fw_r[0], fw_r[2], color="green")
    axarr[1].set_ylabel('No of operations', fontsize=18)
    axarr[1].set_xlabel('No of vertices', fontsize=18)

    plt.savefig('images/bf_fw_%.2f.png'%connectivity, dpi=300)


