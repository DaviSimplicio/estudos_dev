#Fase 1 - Avaliação Davi Simplicio
#Regras: Mês entre 1 a 13 (usar for range 1:13)
# - temperatura entre -60 a +50 (usar float para coleta do dados limitando if temperatura entre x e y)
#Objetivos:
#1. Informar termparatura maxima em Celsius
#2. Calcular temperatura media anual (usar repetição total = total + temp com for range)
#3. Contador de escaldante if temp > 33 (cont = cont + 1)
#4. Filtro de menor valor, if valor > temp (valor = temp)
#5. Filtro maior valor , if valor < tempo (valor = temp)
#observações: usar break para bloquear novas tentativas do for cas ocorra algum erro
# ------------------------------------------------------------------------------------------------------#
#coletar dados de temperatura para cada mês 1 a 12 : temp 1 a 12
menor = 51 
maior = -61
escaldante = 0 
soma = 0

for mes in range(1,13):
   
    for tentativa in range(100):
     temperatura = float(input(f"Qual a temperatura do mês {mes}: "))
        
     if temperatura >= -60 and temperatura <= 50 : 
      break

     else: 
      print(f"Temperatura {temperatura} do mês {mes} fora do limite [-60] a [50]")
 
    soma = soma + temperatura  

    if temperatura > 33: 
        escaldante = escaldante + 1 
    
    if temperatura > maior:
        maior = temperatura
        mes_maior = mes 
    
    if temperatura < menor : 
        menor = temperatura
        mes_menor = mes   

for numero_mes in range(1, 13):

    if numero_mes == 1:
        nome_mes = "janeiro"

    if numero_mes == 2:
        nome_mes = "fevereiro"

    if numero_mes == 3:
        nome_mes = "março"

    if numero_mes == 4:
        nome_mes = "abril"

    if numero_mes == 5:
        nome_mes = "maio"

    if numero_mes == 6:
        nome_mes = "junho"

    if numero_mes == 7:
        nome_mes = "julho"

    if numero_mes == 8:
        nome_mes = "agosto"

    if numero_mes == 9:
        nome_mes = "setembro"

    if numero_mes == 10:
        nome_mes = "outubro"

    if numero_mes == 11:
        nome_mes = "novembro"

    if numero_mes == 12:
        nome_mes = "dezembro"

    if numero_mes == mes_maior:
        nome_mes_maior = nome_mes

    if numero_mes == mes_menor:
        nome_mes_menor = nome_mes

media = soma/12
print(f"Temperatura média máxima anual: {media}")
print(f"Quantidade de meses escaldantes: {escaldante}")
print(f"Mês mais escaldante: {nome_mes_maior}")
print(f"Mês menos quente: {nome_mes_menor}")

