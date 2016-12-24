# Negative weight cycle detection
## Algorithms description
Shortest path problem solution with Dijkstra's algorithm is fast but also vunerable to graphs with negative cycles. Because of Dijkstra's greedy approach to minimizing path weight, it can stay in infinite negative cycle.

Thus arises new problem of negative cycle detection. And for solution could be used side effect of another shortest path algorithms. Bellman-Ford and Floyd-Warshall algorithms are slower than Dijkstra's but their approach is more stable and allow to detect a prescence of negative cycle in a target graph.
### Bellman-Ford algorithm for negative cycle detection
This algorithm uses similar principle of vertex relaxation, in which approximation ot the correct distance is gradually replaced by more accurate values until eventually reaching the optimum solution. Approximation always is an overestimate of a true distance between a vertex and a source, and it is replaced with a new found path if it is shorter. But instead of greedily select next vertex for the path from the queue of closest not processed vertices as Dijkstra's does, Bellman-Ford consequently relaxes all edges for `|V|-1` times, where `|V|` is a number of vertices in the graph.
1. **Initialize**. At the beginning algorithm initializes two collections of size `V` to store distance and predecessor for every vertes in the path. Predecessor of a source vertex is empty and distance is equal to zero.
2. **Relaxation**. On every relaxation iteration algorithm consequently check for every edge `e(v,u)` a condition: `distance[u]` is less than `distance[v] + e.weight`. If It is true, than from shorter path from source vertex to `u` with predecessor `v` exists. Then `distance[u]` is set to `distance[v] + e.weight`, and `predecessor[u]` is set to `v`. It is proven by induction that it is enough to do `n` steps to find all shortest path with length `n` in a graph. Thus relaxation step is repeated `|V|-1` to find all possible shortest pathes in a graph with `|V|` vertices which contains no negative loops.
3. **Negative cycle check**. In the end algorithms repeats relaxation step one more time. If any edge `e(v,u)` detected where `distance[u] > distance[v] + e.weight` is true, then graph contains negative loop. Explanation is simple: path with length `|V|` definitely contain a loop. And it is a negative loop, because any positive loop can not be included in path because shortest path can not contain non-negative loops.

This algorithms uses at most `O(|V|*|E|)` operations in the main loop for the worst case. In the best case, if all egdes are sorted in order of distance from source vertex, it will use `O(|E|)` operations.
For example, consider graph with 4 edges and 5 vertices `(d,e, 1),(c,d, 3),(b,c, 2),(a,b,3)` with source vertex `a`.
Distance:
| a | b   | c   | d   | e   |
|---|-----|-----|-----|-----|
| 0 | inf | inf | inf | inf |
| 0 | 3   | inf | inf | inf |
| 0 | 3   | 5   | inf | inf |
| 0 | 3   | 5   | 8   | inf |
| 0 | 3   | 5   | 8   | 9   |
Predecessors:
| a    | b    | c    | d    | e    |
|------|------|------|------|------|
| None | None | None | None | None |
| None | a    | None | None | None |
| None | a    | b    | None | None |
| None | a    | b    | c    | None |
| None | a    | b    | c    | d    |
### Floyd-Warshall algorithm for negative cycle detection
Floyd-Warshall algorithm also introduces the inductive approach to the shortest path problem solution. On every step it looks for possible shortest path between all pairs of vertices in a graph, which uses one selected node as intermediate pitstop. It operates with a matrix `|V|` by `|V|`, where each element contains shortest path distance between `i`th and `j`th vertex of a graph on current step.
1. **Initialization**. On a step 0 adjacency matrix is copied to distance matrix. Predecessor matrix contains elements `predecessor_ij` where `predecessor_ij` - vertex `j` if there edge from `j` to `i`.
2. **Main loop**. On each iteration algorithm consequently select one vertice `p` to be used as a pitstop. Then it checks each pair of vertices (each element of a distance matrix) if a path from vertex `i` to vertex `j` (respective to the matrix row and column) which uses vertex `p` shorter than current distance between `i` and `j`. If yes, distance between `i` and `j` updated with vertex `p` set a predecessor. In terms of exact computational operations, algorithm just checks if `distance[i][p] + distance[p][j] < distance[i][j]`.
3. **Negative cycle check**. Initially `distance[i,i]` for `i=1..|V|` is equal to zero, because it is distance from vertex `i` to itself. During the main loop, algorithm consequently revises distances between all vertices, and if vertex `i` is a part of a negative cycle, distance from `i` to `i` itself becames less then zero. Thus algorithm could just check all diagonal entries of the distance matrix to find negative cycle in the graph.



# Credits
- https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm
- https://www.youtube.com/watch?v=KQ9zlKZ5Rzc&t=215s "Floyd Warshall Algorithm: All-pairs Shortest-paths" by Joe James
- http://algo.epfl.ch/_media/en/courses/2011-2012/algorithmique-cycles-2011a.pdf Textbook for Algorithmique Course of Ecole Polytechnique
- https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm