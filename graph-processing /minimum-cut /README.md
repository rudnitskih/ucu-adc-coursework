Problem 5: Graph Minimum Cut
Problem Introduction: Suppose you have the data from a mobile operator about all calls in the
country. The government asks you to check if the country’s territorial system should be changed.
For this you construct the following graph: vertices c1, c2, ..., cn are people (mobile operator
customers) and the edges between them represent calls (in the case of a weighted graph the edge
weight rij is number of calls between ci and cj). Therefore, finding a minimum cut of such a
graph would allow us to cluster people into groups where connection is strong inside the group
and weak outside it.
Input Data: The file contains the edges of a directed graph. Vertices are labeled as positive
integers from 1 to n. Every row indicates an edge, the vertex label in the first column is the tail
and the vertex label in second column is the head (recall the graph is directed, and the edges are
directed from the first column vertex to the second column vertex). So for example, a row may
look like "2 31", which means that there is an edge from vertex 2 to vertex 31. The real data set
for this problem is kargerMinCut.txt4. A synthetic dataset could be generated using a
random value generator – e.g. as suggested in Section 3.5.
Constraint: 1 ≤ n ≤ 103
.
Output: Output the sizes of the graphs created by the discovered minimum cut.
Tasks:
1. Implement Karger’s Random Contraction and Stoer-Wagner algorithms for
Computing a Minimum Cut.
2. Run Karger’s algorithm implementation on the input data set of vertex dimension k (n =
k). For that ensure that the numbers of vertices in the input graph are in the range [1, k];
the rest should be removed. After experimenting with the Karger’s algorithm, assign
random weights to the input graph, run Stoer-Wagner algorithm. Compare the results.
Experiment with k = 100 ... 1000 using an appropriate increment to obtain 20-30
performance measurement points. Measure and compare performance of your
implementations as suggested in Section 3.
3. Document your accomplishments, findings, and well-reasoned conclusions in the report.
Provide all the code, executables, and data sets needed to reproduce your results appended
to your report. 