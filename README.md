# Problema das 7 Pontes de Königsberg

Repositório que implementa a visualização e análise do **Problema das 7 Pontes de Königsberg** utilizando Python e a biblioteca `networkx`.

Link do repositório: [https://github.com/vitor-souza-ime/7pontes](https://github.com/vitor-souza-ime/7pontes)

---

## Descrição

O Problema das 7 Pontes de Königsberg é um clássico problema de teoria dos grafos que originou o estudo dos **caminhos e circuitos Eulerianos**. O objetivo é determinar se é possível atravessar todas as pontes exatamente uma vez, começando e terminando em um mesmo ponto (circuito Euleriano) ou apenas atravessando todas as pontes uma vez (caminho Euleriano).

Este projeto:

- Constrói o grafo representando as margens e ilhas de Königsberg.
- Adiciona as 7 pontes como **multiarestas**.
- Calcula os graus dos vértices e identifica quais são ímpares.
- Verifica se o grafo é **conexo** (desconsiderando vértices isolados).
- Determina se o grafo é Euleriano, semi-Euleriano ou se não possui caminho Euleriano.
- Plota o grafo com arestas paralelas (representando múltiplas pontes) e mostra o grau de cada vértice.

---

## Tecnologias

- Python 3.x
- [NetworkX](https://networkx.org/) — Para construção e análise de grafos.
- [Matplotlib](https://matplotlib.org/) — Para visualização do grafo.
- NumPy — Para cálculos auxiliares na distribuição das curvas das arestas.

---

## Como executar

1. Clone o repositório:

```bash
git clone https://github.com/vitor-souza-ime/7pontes.git
cd 7pontes
````

2. Instale as dependências (recomendado criar um ambiente virtual):

```bash
pip install networkx matplotlib numpy
```

3. Execute o script:

```bash
python main.py
```

Você verá:

* Um **gráfico do grafo** com os nós e arestas representando as pontes.
* O **grau de cada vértice**.
* O **veredito Euleriano** no terminal.

---

## Estrutura do repositório

```
7pontes/
├── main.py        # Script principal
└── README.md      # Este arquivo
```

---

## Saída esperada

Exemplo de saída no terminal:

```
Graus dos vértices: {'L': 5, 'T': 3, 'B': 3, 'R': 3}
Vértices de grau ímpar: ['L', 'T', 'B', 'R']
Conexo (desconsiderando isolados)? True
Veredito: Não existe caminho nem circuito Euleriano (mais de 2 vértices de grau ímpar).
```

O gráfico exibido mostra as 4 regiões (L, T, B, R) e as 7 pontes conectando-as.

---

## Referências

* [Problema das 7 Pontes de Königsberg – Wikipedia](https://pt.wikipedia.org/wiki/Problema_das_sete_pontes_de_K%C3%B6nigsberg)
* Leonhard Euler, 1736. *Solutio problematis ad geometriam situs pertinentis*.


