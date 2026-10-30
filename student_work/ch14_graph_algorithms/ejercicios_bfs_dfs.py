from goodrich.ch14.graph import Graph

def vecinos(g, v):
    return [e.opposite(v).element() for e in g.incident_edges(v)]

def dfs(g, v, d):
    for e in g.incident_edges(v):
        w = e.opposite(v)
        if w not in d:
            d[w] = e
            dfs(g, w, d)

def bfs(g, v):
    forest = {v: None}
    level = [v]

    while len(level) > 0:
        next_level = []
        for u in level:
            for e in g.incident_edges(u):
                w = e.opposite(u)
                if w not in forest:
                    forest[w] = e
                    next_level.append(w)
        level = next_level

    return forest

def alcanzables(g, v):
    d = bfs(g, v)
    return [vertex.element() for vertex in d.keys()]

if __name__ == "__main__":
    # tus pruebas (opcional)
    pass
