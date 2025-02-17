# Problema do Bernardo Viajante: *Uma Variação do Problema do Caixeiro Viajante*

Bernardo (este que vos fala), sua esposa e seus cachorros são nômades digitais e planejam suas hospedagens para o ano. Como meio de transporte, utilizam sempre o mesmo carro. O desafio é otimizar a rota para minimizar as distâncias percorridas.

## Objetivo

Dado um conjunto de cidades, o objetivo é encontrar a viagem de ida e volta mais curta possível, passando por todas as cidades exatamente uma vez e retornando ao ponto de partida: Curitiba.

## Definição do Problema

O problema a ser resolvido é uma variação do *Travelling Salesman Problem (TSP)*, onde buscamos determinar a melhor rota de viagem que atenda aos seguintes critérios:

1. Partir de Curitiba;

2. Visitar todas as cidades da lista uma única vez;

3. Retornar a Curitiba ao final do percurso;

4. Minimizar a distância percorrida.

***

# ⚠️ OBSERVAÇÃO

O algoritmo de força bruta utilizado para encontrar a melhor rota verifica **todas as permutações possíveis** das cidades, garantindo a solução ótima, mas com um custo computacional extremamente alto. O número de possibilidades cresce de forma fatorial com o número de cidades, tornando inviável a resolução para conjuntos muito grandes.

| Cidades | Fatorial  | Comparações  |
|---------|-----------|-----------|
| 2       | 2!        | 2         |
| 5       | 5!        | 120       |
| 10      | 10!       | 3.628.800 |
| 20      | 20!       | 2.432.902.008.176.640.000 |

### Recomenda-se utilizar este método apenas para conjuntos pequenos (**≤10 cidades**).

***

## 📌 Fórmula de Haversine para cálculo da distância entre dois pontos no globo

A fórmula de Haversine é usada para calcular a distância entre dois pontos na superfície da Terra, levando em conta sua curvatura. A equação é:

\[
a = \sin^2\left(\frac{\Delta\phi}{2}\right) + \cos(\phi_1) \cdot \cos(\phi_2) \cdot \sin^2\left(\frac{\Delta\lambda}{2}\right)
\]

\[
c = 2 \cdot \text{atan2}\left(\sqrt{a}, \sqrt{1-a}\right)
\]

\[
d = R \cdot c
\]

Onde:

- \( \phi_1, \lambda_1 \) são a latitude e longitude do primeiro ponto (em radianos).
- \( \phi_2, \lambda_2 \) são a latitude e longitude do segundo ponto (em radianos).
- \( \Delta\phi = \phi_2 - \phi_1 \) e \( \Delta\lambda = \lambda_2 - \lambda_1 \) são as diferenças entre as latitudes e longitudes.
- \( R \) é o raio médio da Terra, aproximadamente **6371 km**.
- \( d \) é a distância entre os pontos ao longo da superfície da Terra.

***

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/melhor-rota.git
```
2. Navegue até o diretório do projeto:

```bash
cd BirdLens
```
3. Instale as dependências:

```bash
pip install -r requirements.txt
```

## Como usar

**Para usar dados próprios:** 
    
Prepare seu arquivo .csv, formatado com:

- Coluna 1: cidade  **# Obrigatoriamente deve ser nomeada 'cidade'**
- Coluna 2: lat
- Coluna 3: long

Coloque-o na pasta 'caixeiro_viajante/data/'. No arquivo run.py, defina o caminho para o vídeo:

```python
PATH = os.path.join(BASEDIR, 'caixeiro_viajante', 'data', 'seu_arquivo.csv')
```

1. Execute o script:

```bash
python run.py
```
