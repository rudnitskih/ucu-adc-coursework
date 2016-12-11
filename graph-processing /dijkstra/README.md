## **Problem 1**: Dijkstra's Shortest-Path Algorithm
**Problem Introduction**: Suppose you are tasked to create the shortest distance table between the
cities of a country via the National motorway network. The information about the connections
between individual (adjacent) cities is available from the motorway map. The table is quite
useful for the transportation companies for different purposes: e.g. for calculating the process for
their deliveries between different cities.
Input Data: The input file contains the information about each vertex coordinates and edges
between them. The first n rows are in format «n x y». So, for example if the second row is «2
2600 3000» that means that the x-coordinate of the second vertex is 2600 and the y-coordinate is
3000. The following m rows are in format «i j» so they mark edges between vertex i and vertex j.
Your first task is to process data and find edge weights from the vertices coordinates.The real
data set is the *usa_route.txt2*. A synthetic dataset could be generated using a random value
generator – e.g. as suggested in Section 3.5.
Output: Output the table of shortest distances for the outbound cities `1 … i` – see also the tasks.
 
Constraint: 2 ≤ n ≤ 103
.
Tasks:
1. Implement Straightforward and Heap-based Dijkstra’s algorithms
2. Run both algorithm implementations on the input data set (specified in your variant) for
the first 1 … i outbound vertices (i is the i-th vertex represented by the i-th row in the
input dataset) to compute the shortest-path distances between i and every other vertex of
the graph. Experiment with i = 1 ... n using an appropriate increment to obtain 20-30
performance measurement points. Measure and compare performance of your
implementations as suggested in Section 3.
3. Document your accomplishments, findings, and well-reasoned conclusions in the report.
Provide all the code, executables, and data sets needed to reproduce your results appended
to your report.