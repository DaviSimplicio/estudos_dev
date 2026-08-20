#PROJECT - CALCULLING TRIP VALI
#Precisa calcular:
#Litros Necessários
#Custo do Combustível
#Custo total da viagem
#Custo por pessoa
#Quanto sobra ou falta do orçamento 
#Pedágios
#Observações: Print final deve considerar viagem aprovada ou orçamento insuficiente.
#Objetivo: receber distancia de viagem em km, consumo do carro em km/L, preço do combustível, valor total do pedágio, quantidade de 
#passageiros e orçamento disponível
#Objetivo pessoal de melhoria: Tentar aplicar a 2 ou mais abastecimentos. 
#saida: distancia, combustivel necessário, combustível gasto R$, pedágio, Total, Por pessoa, Orçamento disponível, Saldo Restante, dividir para cada um proporcionalmente. status 
#=======================================================================================================================================#
#Inputs dos Objetivos 
distancia = float(input("Qual a distância ao Destino final em (Km): "))
consumocarro = float(input("Qual o consumo do seu veículo (Km/L) "))
precocombustivel = float(input("Valor do Combustível: "))
pedagio =  float(input("Valor gasto no Pedágio: "))
passageiros = int(input("Quantos passageiros no veículo?: "))
orcamento = float(input("Orçamento da viagem: "))
validacao = int(input("Será necessário outro abastecimento? \n 1 Para [Sim]\n 2 Para [Não]\n R: "))
#Objetivo pessoal é considerar mais de um tanque

if distancia <= 0 or consumocarro <=0 or precocombustivel <= 0 or pedagio < 0 or passageiros <= 0 or orcamento < 0 :
    print("Dados inválidos, inserido alguma variável Negativa") 
else:  
    

 if validacao != 1 and validacao != 2 : 
             print("Validação inserida errada, digite 1 para[Sim] ou 2 para [Não]")

 else: 
            if validacao == 1 :
             abastecimento = float(input("Quantos Litros foram abastecidos na primeira vez?: "))
             precocombustivel2 = float(input("Qual o valor do segundo abastecimento:"))
             consumocarro2 = float(input("Qual o consumo do seu veículo para esse segundo abastecimento (Km/L): "))
             if abastecimento <=0 or precocombustivel2 <=0 or consumocarro2 <=0 : 
                 print("Dados inválidos, inserido alguma variável Negativa")
             
             else:
                 if validacao == 1 and distancia - (consumocarro*abastecimento) <= 0 :
                     print("Não precisa de um Segundo abastecimento")
                 
                 else:
                     #Km rodado primeiro tanque
                     kmrodados1 = abastecimento*consumocarro
                     combustivelgasto1 = (abastecimento*precocombustivel)
                     #Km rodado segundo tanque considerando diferença e distância total
                     kmrodados2 = distancia - kmrodados1
                     combustivelgasto2 = (kmrodados2/consumocarro2)*precocombustivel2
                     #total gasto combustivel
                     combustivelgasto = combustivelgasto1 + combustivelgasto2
                 
                     #Calculo para definir a quantidade gasta considerando 2 abastecimento 1 consumo total e 2 total/parcial ou faltante
                     combustivel = (abastecimento) + ((distancia - kmrodados1)/consumocarro2)
                     #Definido todas as variáveis podemos seguir para o print final

                     total = combustivelgasto + pedagio
                     resto = orcamento - total
                     if total <= orcamento : 
                         print("========Resumo da Viagem======== \n"
                               f"Distância: {distancia:.2f} Km \n"
                               f"Combustível Necessário: {combustivel:.2f} L \n"
                               f"Combustível: R${combustivelgasto:.2f} reais \n"
                               f"Pedágios: R${pedagio:.2f} reais \n"
                                "\n"
                               f"Total: R${total:.2f} reais \n"
                               f"Por Pessoa: R${total/passageiros:.2f} reais \n"
                                "\n"
                               f"Orçamento da Viagem: R${orcamento:.2f} reais \n"
                               f"Saldo: R${resto:.2f} reais \n"
                                "=======VIAGEM APROVADA=========")

                     else: 

                      print("========Resumo da Viagem======== \n"
                           f"Distância: {distancia:.2f} Km \n"
                           f"Combustível Necessário: {combustivel:.2f} L \n"
                           f"Combustível: R${combustivelgasto:.2f} reais \n"
                           f"Pedágios: R${pedagio:.2f} reais \n"
                            "\n"
                           f"Total: R${total:.2f} reais \n"
                           f"Por Pessoa: R${total/passageiros:.2f} reais \n"
                            "\n"
                           f"Orçamento da Viagem: R${orcamento:.2f} reais \n"
                            "\n"
                           f"Ficaram faltando R${-resto:.2f} reais \n"
                            "=======VIAGEM REPROVADA=========")
            else: 
                    
                if validacao == 2 :
                 #Combustível em L do total da viagem
                 combustivel = distancia/consumocarro
                 #Custo do combustivel
                 combustivelgasto = combustivel*precocombustivel
                 #Total da viagem
                 total = combustivelgasto + pedagio
                 #Resto
                 resto = orcamento - total 
                 if total <= orcamento : 
                    print("========Resumo da Viagem======== \n"
                       f"Distância: {distancia:.2f} Km \n"
                       f"Combustível Necessário: {combustivel:.2f} L \n"
                       f"Combustível: R${combustivelgasto:.2f} reais \n"
                       f"Pedágios: R${pedagio:.2f} reais \n"
                        "\n"
                       f"Total: R${total:.2f} reais \n"
                       f"Por Pessoa: R${total/passageiros:.2f} reais \n"
                        "\n"
                       f"Orçamento da Viagem: R${orcamento:.2f} reais \n"
                       f"Saldo: R${resto:.2f} reais \n"
                        "=======VIAGEM APROVADA=========")


                 else: 
                    print("========Resumo da Viagem======== \n"
                       f"Distância: {distancia:.2f} Km \n"
                       f"Combustível Necessário: {combustivel:.2f} L \n"
                       f"Combustível: R${combustivelgasto:.2f} reais \n"
                       f"Pedágios: R${pedagio:.2f} reais \n"
                        "\n"
                       f"Total: R${total:.2f} reais \n"
                       f"Por Pessoa: R${total/passageiros:.2f} reais \n"
                        "\n"
                       f"Orçamento da Viagem: R${orcamento:.2f} reais \n"
                        "\n"
                       f"Ficaram faltando R${-resto:.2f} reais \n"
                        "=======VIAGEM REPROVADA=========")

         

