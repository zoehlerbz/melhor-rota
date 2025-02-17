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

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/melhor-rota.git
```
2. Navegue até o diretório do projeto:

```bash
cd Caixeiro viajante
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
