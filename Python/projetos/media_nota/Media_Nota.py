#Aprovação de a aluno por nota e frequência
#Aluno realiza 3 provas com mesmo peso
#Grau 1 é calculado média aritmética das provas
#Precisa estar presentem em 75% das aulas, caso contrário reprovado por faltas
# if G1 => 7, o ALUNO ESTARÁ APROVADO EM g1
# if G1 < 4, o aluno está reprovado
# if G1 <7 and G1 > 4 , deve realizar exame G2 
# Se a média entre G1 e a nota do G2 for => a 5 o aluno está aprovado em grau 2 
# Se a média for inferior a 5 o aluno estará reprovado em grau 2 
#Objetivo: Criar um sistema que funcione respeitando as regras acima 
#----------------------------------------------------------------------------------------------------#
nome = (str(input("Insira o Nome do aluno: ")))
prova1 = (float(input("Qual a nota da primeira Prova: ")))
prova2 = (float(input("Qual a nota da segunda Prova: ")))
prova3 = (float(input("Qual a nota da terceira Prova: ")))
aulas = (int(input("Quantas aulas válidas teve o Semestre: ")))
presenca = (int(input("Quantas presenças o aluno teve: ")))
#Validação de presença
aprovacao = (presenca/aulas)*100
if aprovacao <= 75 :
    print(f"Aluno(a) {nome}, Reprovado por falta")
    print(f"Frequência: {aprovacao}% ") 

else: 
    #Definindo regra da faixa das prova 0 a 10
    if prova1 <0 or prova1 > 10 : 
        print("Faixa da nota: [0] a [10]")
        print(f"Primeira prova de nota {prova1} fora das especificações")   

    else:
        if prova2 <0 or prova1 > 10 : 
            print("Faixa da nota: [0] a [10]")
            print(f"Segunda prova de nota {prova2} fora das especificações") 
        
        else: 
            if prova3 <0 or prova1 > 10 : 
                print("Faixa da nota: [0] a [10]")
                print(f"Terceira prova de nota {prova3} fora das especificações") 
               
            else: 
                #Depois de definido a regra da prova, só tirar a media 
                g1 = (prova1 + prova2 + prova3)/3
                if g1 >= 7 :
                    print(f"Aluno(a) {nome} Aprovado!")
                    print(f"Média: {g1}")
                    print(f"Frequência: {aprovacao}%")

                else: 
                    if g1 < 7 and g1 >= 4 : 
                        print(f"Aluno(a) {nome} de Recuperação!")
                        print(f"Nota: {g1}")
                        g2 = float(input("Qual a nota da recuperação: "))
                        if g2 > 10 or g2 < 0 : 
                            print("Faixa da nota: [0] a [10]")
                            print(f"Primeira prova de nota {prova1} fora das especificações") 

                        else: 
                            media = (g1+g2)/2 
                            if media >= 5 :
                                print(f"Aluno(a) {nome} Aprovado na recuperação!")
                                print(f"Media: {media}")
                                print(f"Frequência: {aprovacao}%")
                            
                            else:
                                print(f"Aluno(a) {nome} Reprovado na recuperação!")
                                print(f"Media: {media}")
                                print(f"Frequência: {aprovacao}%")
                         
                    else:
                        print(f"Aluno(a) {nome} Reprovado!")
                        print(f"Média: {g1}")
                        print(f"Frequência: {aprovacao}%")
                        
