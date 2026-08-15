#Precisa conter
#NOME
#IDADE
#ALTURA
#IDADE MINIMA (16 ANOS)
#SEXO definir peso minimo para mulehr e homem 
#DIA DE NASCIMENTO
#MES DE NASCIMENTO
#ANO DE NASCIMENTO
#PRINT COM TODOS OS DADOS DO CLIENTE 
print("Bem Vindo a doação de Sangue HEMOSC \n "
f"Por favor nos informe seus dados abaixo:")

nome = input("Nome:")
idade = int(input("Idade: "))
altura = float(input("Altura: "))

sexo = int(input(
     "Sexo:\n"
     "Informe [1] para Feminino\n" 
     "Informe [2] para Masculino:\n"
))

dianasc = int(input("Dia de Nascimento: "))
mesnasc = int(input("Mês de Nascimento : "))
anonasc =int(input("Ano de Nascimento: "))

peso = float(input("Qual seu peso (Kg): "))


if idade < 16:
    print("Não Autorizado para Doação")


else : 
    if sexo <1 or sexo>2 :
        print("Sexo Inválido:\n"
        "[1] Feminino \n"
        "[2] Masculino")
        
    else :
        if altura <= 0 or altura > 3:
            print("Altura Inválida")

        else: 
            if peso <=0: 
                print("Peso Inválido")

            else:
                if dianasc <1 or dianasc > 31:
                     print("Dia de Nascimento Inválido")

                else:
                    if mesnasc < 1 or mesnasc >12 :
                        print("Mês Inválido")

                    else: 
                        if sexo ==1:
                            cadastro = "Feminino"
                        if sexo ==2:
                            cadastro = "Masculino"
                        if sexo == 1 and peso < 51 :
                             print("Mulher abaixo do Peso para Doação")

                        else:
                            if sexo == 2 and peso <50 :
                                    print("Homem abaixo do Peso para Doação")

                            else:
                                #calculo do IMC  
                                imc = peso/(altura*altura)
                                if imc < 18.5 : 
                                    gordura = "Abaixo do Peso"
                                if imc >=18.5 and imc <25 :
                                    gordura = "Peso Normal"
                                if imc >= 25 and imc <30 :
                                    gordura = "Sobrepeso"
                                if imc >=30 and imc <35 :
                                    gordura = "Obesidade Grau I"
                                if imc >=35 and imc <40 :
                                    gordura = "Obesidade Grau II"
                                if imc >=40 :
                                    gordura = "Obesidade Grau III"
                                print ("Cadastro Finalizado:\n"
                                        "Aprovado para Doação!")
                                print(f"Nome:{nome}\n"
                                        f"Idade: {idade} anos\n"
                                        f"Altura: {altura} m \n"
                                        f"Sexo: {cadastro} \n"
                                        f"Nascimento: {dianasc}/{mesnasc}/{anonasc}\n"
                                        f"Peso: {peso} \n"
                                        f"IMC:{gordura}\n"
                                        f"Valor IMC: {imc:.2f}")