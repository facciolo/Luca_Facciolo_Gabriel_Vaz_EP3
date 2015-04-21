from funçoesdieta import *

def alimentodia(alimento):#função que insere os alimentos em seus respectivos dias
    global dia1,dia2,dia3,dia4,dia5,dia6,dia7
    if alimento[0:5] == '06/04':
        dia1+=alimento+ '\n'
    elif alimento[0:5] == '07/04':
        dia2+=alimento+ '\n'
    elif alimento[0:5] == '08/04':
        dia3+=alimento+ '\n'
    elif alimento[0:5] == '09/04':
        dia4+=alimento+ '\n'
    elif alimento[0:5] == '10/04':
        dia5+=alimento+ '\n'
    elif alimento[0:5] == '11/04':
        dia6+=alimento+ '\n'
    elif alimento[0:5] == '12/04':
        dia7+=alimento+ '\n'
    return dia1,dia2,dia3,dia4,dia5,dia6,dia7
        
alimentos = open("alimentos.csv","r+",encoding = "utf-8")
ficha_pessoa = open("usuário.csv","r+",encoding = "utf-8")
ficha_pessoa = ficha_pessoa.read()
dieta = ficha_pessoa.split('\n', 3)[3]
dados_pessoa = ficha_pessoa.split('\n', 10)[1]#comando que separa as informações pessoais do individuo
dados_pessoa = dados_pessoa.split(",")
alimentos = alimentos.read()
alimentos = alimentos.split('\n',1)[1]#comando que separa os alimentos em suas respectivas linhas
lista_dias=dieta.split('\n')

#lista dos dias
dia1 = []
dia2 = []
dia3 = []
dia4 = []
dia5 = []
dia6 = []
dia7 = []


#inserção de alimento nas listas dos dias 
for alimento in lista_dias:
    alimentodia(alimento)
print(''.join(dia1))
print(''.join(dia2))


#Definição dos parametros pessoais utilizados 
nome = dados_pessoa[0]
idade = int(dados_pessoa[1])
peso = float(dados_pessoa[2])
sexo = dados_pessoa[3]
altura = float(dados_pessoa[4])
fator = dados_pessoa[5]


print(dados_pessoa)
print("TESTE")
print(dieta)
#print(alimentos)



    
TMB = FGBenedict(sexo,peso,altura,idade)
TMB = grau_atividade(TMB,fator)

print(TMB)