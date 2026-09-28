# Projeto Fase 2

Projeto da disciplina de Lógica e Programação de Computadores.

O programa lê um arquivo CSV com dados meteorológicos de Porto Alegre e usa esses dados para fazer consultas, cálculos e gerar um gráfico.

## O que o programa faz

- lê o arquivo `dados.csv`
- guarda os dados em uma lista de dicionários
- permite escolher um período por mês e ano
- mostra todos os dados ou somente precipitação, temperatura, umidade e vento
- mostra o mês mais chuvoso do arquivo
- calcula a média da temperatura mínima de um mês entre 2006 e 2016
- gera um gráfico com essas médias
- calcula a média geral da temperatura mínima

## Arquivos

- `AvaliacaoFase2.py`
- `dados.csv`

## Como executar

Deixe o `dados.csv` na mesma pasta do arquivo Python.

Caso não tenha o Matplotlib instalado:

```bash
pip install matplotlib
```

Depois execute:

```bash
python AvaliacaoFase2.py
```

## Observação

O arquivo usado no projeto possui dados até junho de 2016.
