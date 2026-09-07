#Exercicio 3 - Cálculo de salário líquido

Nome = str(input("Insira seu nome: "))
salario = float(input("Insira seu salario: "))
dependentes = int(input("Quantidade de Dependentes: "))

valorDependente = 189.59
if salario > 0 :
    if salario > 8475.55 : inss = 988.10
    elif salario > 4354.27: inss = (((salario - 4354.27)*0.14)+411.12)
    elif salario > 2902.84: inss = (((salario - 2902.84)*0.12)+236.95)
    elif salario > 1621: inss = (((salario - 1621.00)*0.09)+121.58)
    elif salario <= 1621 : inss = salario*0.075
    #Calculo considerando a quantidade de dependente
    if dependentes < 0 :
        print("Quantidade de dependentes incorreto")

    else:
        descontoSimplificado = 607.20
        deducaoLegal = inss + (valorDependente * dependentes)

        if deducaoLegal > descontoSimplificado:
            salarioImposto = salario - deducaoLegal
        else:
            salarioImposto = salario - descontoSimplificado

        if salarioImposto > 4664.68: imposto = (((salarioImposto - 4664.68) * 0.275) + 374.07)
        elif salarioImposto > 3751.05: imposto = (((salarioImposto - 3751.05) * 0.225) + 168.5)
        elif salarioImposto > 2826.65: imposto = (((salarioImposto - 2826.65) * 0.15) + 29.84)
        elif salarioImposto > 2428.80: imposto = ((salarioImposto - 2428.80) * 0.075)
        else:
            imposto = 0

        #Calculo considerando zero dependente para considerar a reestituição
        deducaoLegalSemDependente = inss

        if deducaoLegalSemDependente > descontoSimplificado:
            salarioReestituicao = salario - deducaoLegalSemDependente
        else:
            salarioReestituicao = salario - descontoSimplificado

        if salarioReestituicao > 4664.68: impostoR = (((salarioReestituicao - 4664.68) * 0.275) + 374.07)
        elif salarioReestituicao > 3751.05: impostoR = (((salarioReestituicao - 3751.05) * 0.225) + 168.5)
        elif salarioReestituicao > 2826.65: impostoR = (((salarioReestituicao - 2826.65) * 0.15) + 29.84)
        elif salarioReestituicao > 2428.80: impostoR = ((salarioReestituicao - 2428.80) * 0.075)
        else:
            impostoR = 0

        if salario <= 5000:
            irrf_final = 0
            irrf_finalR = 0

        elif salario <= 7350:
            reducao = 978.62 - (0.133145 * salario)

            irrf_final = imposto - reducao
            irrf_finalR = impostoR - reducao
            if irrf_final < 0:
                irrf_final = 0

            if irrf_finalR < 0:
                irrf_finalR = 0

        else:
            irrf_final = imposto
            irrf_finalR = impostoR

        fgts = salario*0.08

        salarioLiquido = salario - inss - irrf_final

        if dependentes > 0:
            reestituicao = (irrf_finalR - irrf_final) / dependentes
        else:
            reestituicao = 0

        print(f"Holerite!\n"
              f"Nome: {Nome}\n"
              f"Salário Bruto: R${salario:.2f}\n"
              f"Dependentes: {dependentes}\n"
              f"INSS: R${inss:.2f}\n"
              f"IRRF Final: R${irrf_final:.2f}\n"
              f"Salário Líquido: R${salarioLiquido:.2f}\n"
              f"FGTS: R${fgts:.2f}, A receber da empresa!\n")

        if dependentes > 0:
            print(f"IR sem dependentes: R${irrf_finalR:.2f}")
            print(f"IR com dependentes: R${irrf_final:.2f}")
            print(f"Economia média por dependente: R${reestituicao:.2f}")
            print(f"Economia média por dependente: R${reestituicao:.2f}")
        else:
            print("Sem dependentes declarados.")

else:
    print(f"Salário inválido: R${salario}, não é permitido!")