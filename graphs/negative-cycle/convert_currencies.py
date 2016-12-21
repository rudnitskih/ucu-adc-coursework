import utils as u


def convert_currencies_to_graph(file_path):
    with open(file_path, "r") as f:
        n = int(f.readline());
        vertices = []
        adj_list = {}
        for line in f:
            parts = filter(None, line.split(' '))
            if len(parts) == 6:
                vertice = parts[0]
                vertices.append(vertice)
        f.seek(0)
        f.readline()
        v1 = 0
        for line in f:
            parts = filter(None, line.split(' '))
            if len(parts) == 6:
                for v2 in range(1, len(parts)):
                    u.set_connection(adj_list, vertices[v1], vertices[v2-1], float(parts[v2]))
            v1 += 1

        return vertices, adj_list

edges, vertices = convert_currencies_to_graph("rates.txt")
u.save_graph_to_file(edges, vertices, "rates.graph")