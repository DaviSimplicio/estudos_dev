#Fase 2 - Ler arquivo CSV e Avaliar os dadis do usuário e mostrar dados do período, emitir grafico e dia mais chuvoso
import matplotlib.pyplot as plt

def mesMaisChuvoso(lista):
    chuva = {}

    for registro in lista:
        chave = str(registro["mes"]) + "/" + str(registro["ano"])

        if chave in chuva:
            chuva[chave] += registro["precipitacao"]
        else:
            chuva[chave] = registro["precipitacao"]

    maior = 0
    mesAno = ""

    for chave in chuva:
        if chuva[chave] > maior:
            maior = chuva[chave]
            mesAno = chave

    print(f"\nMês mais chuvoso: {mesAno} - {maior:.2f} mm")

def mediaMinima(lista, mes):
    medias = {}

    for ano in range(2006, 2017):
        soma = 0
        cont = 0

        for registro in lista:
            if registro["mes"] == mes and registro ["ano"] == ano:
                soma += registro ["minima"]
                cont += 1
        #O arquivo possui dados até junho de 2016
        if cont > 0:
            medias[str(mes) + "/" + str(ano)] = soma / cont
        else:
            print(f"Não existem dados para {mes}/{ano}")

    return medias

#Leitura do CSV
arquivo = open("dados.csv", "r")

arquivo.readline() #ignora cabeçaho do arquivo
lista = []

for linha in arquivo:
    linha = linha.strip()
    dados = linha.split(",")
    dataSeparada = dados[0].split("/")

   #Armazenando cada dado em sua variável correspondente
    registro = {
        "data": dados[0],
        "dia": int(dataSeparada[0]),
        "mes": int(dataSeparada[1]),
        "ano": int(dataSeparada[2]),
        "precipitacao": float(dados[1]),
        "maxima": float(dados[2]),
        "minima": float(dados[3]),
        "horasInsol": float(dados[4]),
        "tempMedia": float(dados[5]),
        "umidRelativa": float(dados[6]),
        "velocidadeVento": float(dados[7]),
    }
    lista.append(registro)

arquivo.close()

mesInicial = int(input("Qual o mês inicial: "))
anoInicial = int(input("Qual o ano inicial: "))
mesFinal = int(input("Qual o mes final: "))
anoFinal = int(input("Qual o ano final: "))

#Valida se o período inicial está dentro do intervalo existente no arquivo
while (anoInicial < 1961 or anoInicial > 2016 or mesInicial < 1 or mesInicial > 12 or (anoInicial == 2016 and mesInicial > 6)):
    print("Período inicial incorreto!")
    print(f"Mês Final: {mesFinal}")
    print(f"Ano Final: {anoFinal}")

    mesInicial = int(input("Qual o mês inicial: "))
    anoInicial = int(input("Qual o ano inicial: "))

#Valida se o período final existe no arquivo e se não é menor que o período inicial
while (anoFinal < 1961 or anoFinal > 2016 or mesFinal < 1 or mesFinal > 12 or (anoFinal == 2016 and mesFinal > 6) or
       anoFinal < anoInicial or (anoFinal == anoInicial and mesFinal < mesInicial)):
    print("Período final incorreto!")
    print(f"Mês inicial: {mesInicial}")
    print(f"Ano inicial: {anoInicial}")

    mesFinal = int(input("Qual o mês final: "))
    anoFinal = int(input("Qual o ano final: "))

print("---------------------------------------")
print("O que deseja visualizar?\n"
      "[1] Todos os dados \n"
      "[2] Precipitação \n"
      "[3] Temperatura \n"
      "[4] umidade e vento \n"
      "Selecione", end="")

selecao = int(input(": "))

while selecao < 1 or selecao > 4:
    print("Opção Invalida!")
    selecao = int(input("Selecione: "))

dataInicial = anoInicial * 100 + mesInicial
dataFinal = anoFinal * 100 + mesFinal

if selecao == 1:
    print("Data / Precipitação / Máxima / Mínima / Horas Insol / Média / Umidade / Vento")
elif selecao == 2:
    print("Data / Precipitação")
elif selecao == 3:
    print("Data / Máxima / Mínima / Média")
else:
    print("Data / Umidade / Vento")

for registro in lista:
    dataRegistro = registro ["ano"] * 100 + registro["mes"]

    if dataInicial <= dataRegistro <= dataFinal:

        if selecao == 1:
            print(registro["data"],
                  "/ Precipitação:", registro["precipitacao"],
                  "/ Máxima:", registro["maxima"],
                  "/ Mínima:", registro["minima"],
                  "/ Horas Insol:", registro["horasInsol"],
                  "/ Média:", registro["tempMedia"],
                  "/ Umidade:", registro["umidRelativa"],
                  "/ Vento:", registro["velocidadeVento"])
            print()
        elif selecao == 2:
            print(registro["data"], "/ Precipitação: ", registro["precipitacao"])
            print()
        elif selecao == 3:
            print(registro["data"],
                  "/ Máxima:", registro["maxima"],
                  "/ Mínima:", registro["minima"],
                  "/ Média:", registro["tempMedia"])
            print()

        else:
            print(registro["data"],
                  "/ Umidade:", registro["umidRelativa"],
                  "/ Vento:", registro["velocidadeVento"])
            print()

mesMaisChuvoso(lista)

mesEscolhido = int(input("Digite um mês para calcular a média de temperatura mínima: "))

while mesEscolhido < 1 or mesEscolhido > 12:
    print("Mês invalido!")
    mesEscolhido = int(input("Digite um mês: "))

medias = mediaMinima(lista,mesEscolhido)

for chave in medias:
    print(chave, "-", round(medias[chave], 2 ), "ºC")

anos = []
temperatura = []

for chave in medias:
    data = chave.split("/")
    anos.append(data[1])
    temperatura.append(medias[chave])

plt.bar(anos, temperatura, label="Temperatura mínima")
plt.xlabel("Ano")
plt.ylabel("Temperatura mínima média °C")
plt.title("Média da temperatura mínima")
plt.legend()
plt.show()

soma = 0
for chave in medias:
    soma+= medias[chave]

mediaGeral = soma / len(medias)

print(f"Média geral: {mediaGeral:.2f} ºC")



