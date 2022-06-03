print("---saiba o aumento do seu salário---")

salario = float(input("Digite o seu salário: ").replace(',','.'))
salarioN = float(input("Digite a porcentagem que você ganhou: "))

salarioN = salarioN / 100
salarios = salario * salarioN + salario

print("O seu novo salário é de = R$%.2f"%salarios)