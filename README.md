# Análise de Grafos - Amazon Video Games Reviews

Trabalho prático da disciplina de Teoria dos Grafos (UFBA, 2026).
Análise estrutural do grafo de avaliações de jogos eletrônicos da Amazon,
modelado como grafo bipartito não-direcionado entre usuários e produtos.

---

## Descrição

O dataset utilizado é o **Video Games Reviews** da Amazon (McAuley Lab, UCSD).
Cada avaliação gera uma aresta entre um usuário e um produto, formando um
grafo bipartito. Após tratamentos de filtragem temporal, remoção de duplicatas
e extração da maior componente conexa, o grafo final possui
**400.637 nós** e **466.498 arestas**.

A análise está dividida em três partes:

- **Parte I** - Métricas estruturais (grau, densidade, diâmetro, clusterização, etc.)
- **Parte II** - Algoritmos da disciplina (BFS, DFS, Dijkstra, Floyd-Warshall, Tarjan, MST, etc.)
- **Parte III** - Propriedades de redes complexas (small-world, lei de potência, robustez)

---

## Estrutura do Repositório

```
Amazon_Review_Graph/
├── Notebooks/
│   └── Códigos.ipynb          # Notebook principal com toda a análise
├── Dados/
│   └── Video_Games.jsonl.gz   # Dataset (baixar separadamente - ver abaixo)
├── Imagens/
│   ├── teaser_figure.png
│   ├── grafo_visualizacao.png
│   ├── distribuicao_graus.png
│   ├── power_law.png
│   └── robustez.png
├── requirements.txt
└── README.md
```

---

## Requisitos

- Python 3.8 ou superior
- Jupyter Notebook / JupyterLab / VS Code / Google Colab

---

## Instalação e Execução

### Dataset

> **Atenção:** o arquivo do dataset **não está incluído** neste repositório
> devido à limitação de tamanho de arquivos do GitHub (máx. 100MB).

Faça o download manual do arquivo `Video_Games.jsonl.gz` diretamente em:

[https://mcauleylab.ucsd.edu/public_datasets/data/amazon_2023/raw/review_categories/Video_Games.jsonl.gz](https://mcauleylab.ucsd.edu/public_datasets/data/amazon_2023/raw/review_categories/Video_Games.jsonl.gz)

Após o download, coloque o arquivo dentro da pasta `Dados/`:

```
Amazon_Review_Graph/
└── Dados/
    └── Video_Games.jsonl.gz   ← aqui
```


### Opção 1 - Localmente

**1. Clone o repositório**
```bash
git clone https://github.com/joao0araujo/Amazon_Review_Graph.git
cd Amazon_Review_Graph
```

**2. Crie um ambiente virtual (recomendado)**
```bash
# Linux / Mac
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

**3. Instale as dependências**
```bash
pip install -r requirements.txt
```

**4. Abra o notebook**
```bash
jupyter notebook Notebooks/Códigos.ipynb
```

### Opção 2 - Google Colab

Faça upload do arquivo `Notebooks/Códigos.ipynb` diretamente no
[Google Colab](https://colab.research.google.com). As dependências
já estão disponíveis no ambiente do Colab - não é necessário instalar
o `requirements.txt`. Lembre-se de fazer upload do dataset também.

---

## Execute as células em ordem

O notebook está organizado sequencialmente. Execute todas as células
de cima para baixo. Algumas células são computacionalmente intensas:

| Operação | Tempo estimado |
|----------|----------------|
| BFS / DFS (30×) | ~30s |
| Dijkstra (30×) | ~2min |
| Diâmetro - 500 amostras BFS | ~8min |
| Floyd-Warshall (10×) | ~20s |
| Tarjan (10×) | ~2min |
| Robustez - 30 repetições | ~5min |

---

## Autores

- João Araújo - Universidade Federal da Bahia (UFBA)

## Disciplina

Teoria dos Grafos  
Professor: Bruno
UFBA, 2026