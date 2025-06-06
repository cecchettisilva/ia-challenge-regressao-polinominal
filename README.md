# Desafio de Regressão Linear Múltipla

## Objetivo

O objetivo deste exercício é: 
Você é um analista de dados em uma empresa de vendas e deseja prever a receita de vendas de um vendedor com base no seu tempo de experiência na empresa, o número de vendas que ele realiza, e um fator sazonal que pode afetar os resultados (por exemplo, meses de alta e baixa demanda).

## Tarefa:

1. **Carregamento de Dados**: Carregar o dataset no Python usando o Pandas.
2. **Exploração dos Dados**: Realizar uma análise exploratória dos dados, visualizando correlações entre as variáveis.
3. **Divisão dos Dados**: Separar os dados em conjuntos de treinamento e teste.
4. **Modelo de Regressão Linear**:
    - Treinar um modelo de regressão linear para prever a receita com base no tempo de experiência e no número de vendas.
    - Avaliar o desempenho do modelo usando métricas como o MSE (Mean Squared Error) e o R².
5. **Modelo de Regressão Polinomial**:
    - Treinar um modelo de regressão polinomial, incluindo o fator sazonal como uma variável adicional.
    - Avaliar se o modelo polinomial oferece um desempenho superior ao modelo linear simples.
6. **Comparação dos Modelos**: Comparar os resultados e decidir qual modelo é mais adequado para prever a receita com base nas variáveis fornecidas.

## Estrutura do Projeto

- __sales_data.csv__: Arquivo contendo os dados de entrada para análise.
- **receita_vendas.ipynb**: Notebook principal com o código e análises realizadas.
- __api_receita_vendas.py__: API para calcular as predições.
- __app_streamlit_receita_vendas.py__: Frontend para realizar e demonstrar os cálculos de predições.
- __modelo_receita_vendas.pkl__: Arquivo base usado, contendo a lógica para predições.
- **Pipfile** e **Pipfile.lock**: Arquivos para gerenciamento de dependências do projeto.

## Instalação

1. Certifique-se de ter o Python 3.8 ou superior instalado.

2. Instale o gerenciador de pacotes `pipenv` com o comando:

```bash
pip install pipenv

```

3. Navegue até o diretório do projeto e instale as dependências com:

```bash
pipenv install <nome_da_biblioteca>

```

4. Ative o ambiente virtual:

```bash
pipenv shell

```

## Executar API

- Execute o comando abaixo em um terminal:

```bash
uvicorn api_receita_vendas:app --reload
```

## Executar Frontend:

- Execute o comando abaixo em um terminal:

```bash
streamlit run app_streamlit_receita_vendas.py
```