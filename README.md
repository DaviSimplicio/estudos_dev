# estudos_dev

Repositório de estudos, projetos e cursos desenvolvidos ao longo da graduação com exercícios da faculdade e anotações próprias.

Curso Análise e Desenvolvimento de Sistemas na PUCRS. Aqui ficam os exercícios que faço nas disciplinas e o que vou estudando por fora.

## Organização

```
JAVA/          estudos de Java
Python/
  Provas/      avaliações das disciplinas
  ...          exercícios e práticas das aulas
```

## Avaliação Fase 2, dados meteorológicos de Porto Alegre

Arquivo `Python/Provas/AvaliacaoFase2.py`

Trabalho individual da disciplina de programação em Python da PUCRS. A proposta era ler um arquivo CSV com dados climáticos diários de Porto Alegre entre 1961 e 2016, com cerca de 18 mil registros vindos do INMET, e fazer análises e um gráfico a partir deles.

### O que a avaliação pedia

1. **Leitura do arquivo.** Carregar o CSV para a memória em listas ou dicionários, sem alterar o arquivo original e usando caminho relativo.
2. **Visualização por período.** O usuário informa mês e ano inicial e final e escolhe se quer ver todos os dados, só precipitação, só temperatura ou só umidade e vento. As entradas precisam ser validadas.
3. **Mês mais chuvoso.** Encontrar o mês e ano com maior precipitação considerando todo o arquivo, usando dicionário e pelo menos uma função.
4. **Média da temperatura mínima.** Para um mês escolhido pelo usuário, calcular ano a ano a média da temperatura mínima entre 2006 e 2016, guardando o resultado em um dicionário.
5. **Gráfico de barras.** Mostrar essas médias em um gráfico com eixos rotulados e legenda.
6. **Média geral.** Percorrer o dicionário do item anterior e mostrar a média geral do período.

### Como resolvi

Cada linha do CSV vira um dicionário com data, dia, mês, ano e as medições, e todos ficam guardados numa lista. Separei a data com `split` para conseguir filtrar por mês e ano.

Para o filtro de período transformei mês e ano em um número só (ano x 100 + mês), assim a comparação entre datas fica simples. As entradas do usuário são validadas considerando que o arquivo vai de 1961 até junho de 2016.

O mês mais chuvoso usa um dicionário com a chave "mês/ano" somando a precipitação de todos os dias. A média da temperatura mínima segue a mesma ideia e depois alimenta o gráfico feito com matplotlib e o cálculo da média geral.

### Como rodar

O arquivo `dados.csv` já está na mesma pasta do programa. Basta entrar em `Python/Provas` e executar

```
python AvaliacaoFase2.py
```

É preciso ter o matplotlib instalado (`pip install matplotlib`).
