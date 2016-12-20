import utils as u


def convert_currencies_to_graph(file_path):
    with open(file_path, "r") as f:
        n = int(f.readline());
        vertices = []
        edges = {}
        for line in f:
            parts = filter(None, line.split(' '))
            if len(parts) == 6:
                vertice = parts[0]
                vertices.append(vertice)
                v1 = len(vertices)-1
                for v2 in range(n):
                    if v1 != v2:
                        exchange = parts[v2 + 1]
                        key = u.gr_key(v1, v2)
                        edges[key] = (v1,v2, float(exchange))
        return vertices, edges

edges, vertices = convert_currencies_to_graph("rates.txt")
u.save_graph_to_file(edges, vertices, "rates.graph")