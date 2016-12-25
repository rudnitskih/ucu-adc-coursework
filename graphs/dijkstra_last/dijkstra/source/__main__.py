import Graph
from Dijkstra import shortest_path, dijkstra, dijkstra_with_heap, dijkstra_with_heap_base
from collections import defaultdict
from make_data_in_graph import make_data_in_graph
from last_imp_dijstra import lst_dijkstra, lst_dijkstra_with_heap
from make_data_vertex import make_data_vertex
from timeit import default_timer as timer
from numpy import mean, log

if __name__ == '__main__':
    print 'Pleas, choose which variant of dijkstra algorithm you need:'
    print '1 - Straightforward'
    print '2 - Heap-Based\n'
    choise = raw_input('Choise - ')

    if int(choise) == 1 :

        print "OK let`s start our expirement!"
        print '--------------------------------------'
        print '\n'
        print 'And first will be Straightforward dijkstra Algorithm'

        for exp in range(33 ,1000, 33):
            print str(exp) + ' - ' + 'Vertices'
            result = []
            counter1 = []
            counter2 = []
            graph = make_data_vertex('../../usa_route.txt', exp)
            nodes = graph.nodes
            for i in range(5):
                print str(i) + ' - ' + 'epoch'
                start = timer()
                for node in nodes:
                    tmp = dijkstra(graph, node)
                    counter1.append(tmp[2])
                    counter2.append(tmp[3])

                end = timer()
                result.append(end - start)

            print '\n '
            print '--------------------------------------'
            print '\n'
            print mean(result), mean(counter1), mean(counter2), mean(counter1) +  mean(counter2), len(graph.edges) + len(graph.nodes)**2
            print '--------------------------------------'
            print len(graph.edges)
            with open('straightforward.txt', 'a') as f:
                f.write(str(mean(result)) + ',' + str(mean(counter1)) + ',' + str(mean(counter2)) +',' + str(len(graph.edges) + len(graph.nodes)**2) +'\n')

    elif int(choise) == 2:
        print 'OK let`s start our expirement!'
        print '--------------------------------------'
        print ''
        print ''
        print 'And first will be Straightforward dijkstra Algorithm'

        for exp in range(33, 1000, 33):
            print str(exp) + ' - ' + 'Vertices'
            result = []
            counters = []
            graph = make_data_vertex('../../usa_route.txt', exp)
            nodes = graph.nodes
            for i in range(5):
                print str(i) + ' - ' + 'epoch'
                start = timer()
                counter1 = []
                counter2 = []
                for node in nodes:
                    tmp = lst_dijkstra_with_heap(graph, node)
                    counter1.append(tmp[2])
                    counter2.append(tmp[3])

                end = timer()
                result.append(end - start)
            print '\n '
            '--------------------------------------'
            print mean(result), mean(counter1), mean(counter2), mean(counter1) + mean(counter2), (len(graph.edges) + len(graph.nodes))*log(len(graph.nodes))
            print '--------------------------------------'

            with open('Heap-Based.txt', 'a') as f:
                f.write(str(mean(result)) + ',' + str(mean(counter1)) + ',' + str(mean(counter2)) + ',' + str((len(graph.edges) + len(graph.nodes))*log(len(graph.nodes))) + '\n')

    else:
        print 'Oops'














































