import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# --- Montagem do grafo (Königsberg) ---
# Nós: L = left (margem/ilha), T = top (ilha), B = bottom (ilha), R = right (margem)
G = nx.MultiGraph()

nodes = ["L", "T", "B", "R"]
G.add_nodes_from(nodes)

# As 7 pontes (multiarestas)
# Configuração clássica que produz graus: L:5, T:3, B:3, R:3
edges = [
    ("L", "T"), ("L", "T"),  # 2 pontes L-T
    ("L", "B"), ("L", "B"),  # 2 pontes L-B
    ("L", "R"),              # 1 ponte L-R (linha horizontal)
    ("T", "R"),              # 1 ponte T-R
    ("B", "R"),              # 1 ponte B-R
]
for u, v in edges:
    G.add_edge(u, v)

# --- Checagens de Euler ---
# Graus
degrees = dict(G.degree())
odd_vertices = [n for n, d in degrees.items() if d % 2 == 1]

# Conectividade (desconsiderando vértices isolados)
non_isolated = [n for n, d in degrees.items() if d > 0]
connected = True
if non_isolated:
    connected = nx.is_connected(G.subgraph(non_isolated))

# Decisão
if not connected:
    verdict = "Grafo desconexo (desconsiderando isolados) — sem trilha Euleriana que percorra todas as arestas."
else:
    if len(odd_vertices) == 0:
        verdict = "Euleriano: existe circuito que percorre todas as arestas exatamente uma vez."
    elif len(odd_vertices) == 2:
        verdict = "Semi-Euleriano: existe caminho que percorre todas as arestas exatamente uma vez (mas não circuito)."
    else:
        verdict = "Não existe caminho nem circuito Euleriano (mais de 2 vértices de grau ímpar)."

# --- Desenho do grafo (arestas paralelas como arcos) ---
pos = {
    "L": (-1.0, 0.0),
    "T": (0.2,  0.8),
    "B": (0.2, -0.8),
    "R": (1.2,  0.0),
}

plt.figure(figsize=(8, 6))
# desenhar nós e rótulos
nx.draw_networkx_nodes(G, pos, node_color="green", node_size=700)
nx.draw_networkx_labels(G, pos, font_color="white", font_weight="bold")

# desenhar arestas paralelas manualmente
seen = set()
for u in G.nodes():
    for v in G[u]:
        if (v, u) in seen:
            continue
        seen.add((u, v))
        m = G.number_of_edges(u, v)
        # distribuir os raios (rad) das curvas
        if m == 1:
            rads = [0.0]
        else:
            # espaços simétricos em torno de 0
            rads = np.linspace(-0.5, 0.5, m)
        for rad in rads:
            nx.draw_networkx_edges(
                G, pos,
                edgelist=[(u, v)],
                connectionstyle=f"arc3,rad={rad}",
                width=3,
                edge_color="black"
            )

# mostrar graus ao lado dos nós
for n, (x, y) in pos.items():
    plt.text(x, y - 0.13, f"deg={degrees[n]}", horizontalalignment="center", fontsize=10)

plt.title("Problema das 7 Pontes de Königsberg", fontsize=14)
plt.axis("off")
plt.tight_layout()
plt.show()

# --- Saída textual ---
print("Graus dos vértices:", degrees)
print("Vértices de grau ímpar:", odd_vertices)
print("Conexo (desconsiderando isolados)?", connected)
print("Veredito:", verdict)
