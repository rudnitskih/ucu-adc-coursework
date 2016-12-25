import matplotlib.pyplot as plt
import utils as u
from pylab import rcParams
rcParams['figure.figsize'] = 12, 12

plt.style.use('ggplot')

c = [0.01, 0.2, 0.4, 0.6, 0.8]
for connectivity in c:
    bf_r = u.read_test_result("results/bellman-ford-%.2f.txt" % connectivity)

    f, ax = plt.subplots()
    ax.set_title('Bellman-Ford on graph with connectivity %.2f' % connectivity, fontsize=24)
    ax.plot(bf_r[0], bf_r[2], color="darkblue", label='Real operations estimate', marker="o", linewidth=4.)
    ax.plot(bf_r[0], bf_r[3], color="darkred", label='Theoretical estimate', marker="^", linewidth=4.)
    ax.set_ylabel('No of operations', fontsize=18)
    ax.set_xlabel('No of vertices', fontsize=18)
    ax.legend(loc='upper left', shadow=True)

    plt.savefig('images/bf_%.2f.png'%connectivity, dpi=300)

    fw_r = u.read_test_result("results/floyd-warshall-%.2f.txt"%connectivity)

    f, ax = plt.subplots()
    ax.set_title('Floyd-Warshall on graph with connectivity %.2f'%connectivity, fontsize=24)
    ax.plot(fw_r[0], fw_r[2], color="darkblue", label='Real operations estimate', marker="o", linewidth=4.)
    ax.plot(fw_r[0], fw_r[2], color="darkred", label='Theoretical estimate', marker="^", linewidth=4.)
    ax.set_ylabel('No of operations', fontsize=18)
    ax.set_xlabel('No of vertices', fontsize=18)
    ax.legend(loc='upper left', shadow=True)

    plt.savefig('images/fw_%.2f.png'%connectivity, dpi=300)

    f, ax = plt.subplots()
    ax.plot(bf_r[0], bf_r[1], color="darkblue", label='Bellman-Ford', linewidth=2.)
    ax.plot(fw_r[0], fw_r[1], color="darkred", label='Floyd-Warshall', linewidth=2.)
    ax.set_ylabel('Time (sec)', fontsize=18)
    ax.set_title('Both algorithms on graph with connectivity %.2f' % connectivity, fontsize=24)
    ax.legend(loc='upper left', shadow=True)

    plt.savefig('images/bf_fw_%.2f.png'%connectivity, dpi=300)


