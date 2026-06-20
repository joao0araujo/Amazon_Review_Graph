# 1. Clone o repositório
git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO
cd SEU_REPOSITORIO

# 2. (Opcional) Crie um ambiente virtual
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Abra o notebook
jupyter notebook analise_grafo.ipynb
Quer que eu escreva o README completo agora?Você disse: Escreva por favorEscreva por favor23:33Claude respondeu: ├── analise_grafo.Mobilizou recursos para documentação abrangenteMobilizou recursos para documentação abrangentemarkdown# Análise de Grafos — Amazon Video Games Reviews

Trabalho prático da disciplina de Grafos (MATA, UFBA).  
Análise estrutural do grafo de avaliações de jogos eletrônicos da Amazon,
modelado como grafo bipartito não-direcionado entre usuários e produtos.

## Descrição

O dataset utilizado é o **Video Games Reviews** da Amazon, disponível
publicamente. Cada avaliação gera uma aresta entre um usuário e um produto,
formando um grafo bipartito. Após tratamentos, o grafo final possui
**400.637 nós** e **466.498 arestas**.

A análise está dividida em três partes:

- **Parte I** — Métricas estruturais (grau, densidade, diâmetro, clusterização, etc.)
- **Parte II** — Algoritmos da disciplina (BFS, DFS, Dijkstra, Floyd-Warshall, Tarjan, MST, etc.)
- **Parte III** — Propriedades de redes complexas (small-world, lei de potência, robustez)

## Estrutura do Repositório
├── analise_grafo.ipynb        # Notebook principal com toda a análise

├── requirements.txt           # Dependências Python

├── data/

│   └── Video_Games.jsonl.gz   # Dataset original (ver instruções abaixo)

├── outputs/

│   ├── grafo_visualizacao.png

│   ├── teaser_figure.png

│   ├── distribuicao_graus.png

│   ├── power_law.png

│   └── robustez.png

└── README.md

## Requisitos

- Python 3.8 ou superior
- Jupyter Notebook (Extensão do VS Code) ou Google Collab
- Dataset

## Instalação e Execução

### Dataset

> **Atenção:** o arquivo do dataset não está incluído neste repositório
> devido à limitação de tamanho do GitHub (máximo 100MB por arquivo).

Faça o download manual do arquivo `Video_Games.jsonl.gz` em:  
[https://amazon-reviews-2023.github.io](https://mcauleylab.ucsd.edu/public_datasets/data/amazon_2023/raw/review_categories/Video_Games.jsonl.gz)

Após o download, coloque o arquivo dentro da pasta `data/`:

### 1. Clone o repositório

```bash
git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO
cd SEU_REPOSITORIO
```

### 2. Crie um ambiente virtual (recomendado)

```bash
# Linux / Mac
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Abra o notebook

```bash
jupyter notebook analise_grafo.ipynb
```

OBS: Caso queira rodar pelo Google Collab, não é necessaria a instalação dos requeriments, basta apenas importar o arquivo presente em ```Notebooks``` 

### 5. Execute as células em ordem

O notebook está organizado sequencialmente. Execute todas as células
de cima para baixo. As células mais pesadas (BFS em 500 nós, robustez)
podem levar alguns minutos.

## Aviso de Desempenho

Algumas células são computacionalmente intensas. Tempos estimados
em um computador comum:

| Célula | Operação | Tempo estimado |
|--------|----------|----------------|
| BFS/DFS (30x) | Grafo completo | ~30s |
| Dijkstra (30x) | Grafo completo | ~2min |
| Diâmetro (500 amostras) | BFS por amostragem | ~8min |
| Floyd-Warshall (10x) | Subgrafo 300 nós | ~20s |
| Tarjan (10x) | Grafo completo | ~2min |
| Robustez (30 repetições) | Remoção aleatória | ~5min |

## Autores

- João — Universidade Federal da Bahia (UFBA)

## Disciplina

MATA — Grafos  
Professor: George Lima  
UFBA, 2025
Só substituir o link do GitHub e conferir o nome do arquivo do dataset. Quer ajuda para organizar o repositório agora?