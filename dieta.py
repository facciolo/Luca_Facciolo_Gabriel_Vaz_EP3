from funçoesdieta import *

alimentos = open("alimentos.csv","r+",encoding = "utf-8")
ficha_pessoa = open("usuário.csv","r+",encoding = "utf-8")
ficha_pessoa = ficha_pessoa.read()
dieta = ficha_pessoa.split('\n', 3)[3]
lista_dias=dieta.split('\n')
dados_pessoa = ficha_pessoa.split('\n', 10)[1]#comando que separa as informações pessoais do individuo
dados_pessoa = dados_pessoa.split(",")
alimentos = alimentos.read()
alimentos = alimentos.split('\n',1)[1]#comando que separa os alimentos em suas respectivas linhas
alimentos = alimentos.split('\n')
catalogo = dict()



#lista dos dias
dia1 = []
dia2 = []
dia3 = []
dia4 = []
dia5 = []
dia6 = []
dia7 = []


#Definição dos parametros pessoais utilizados 
nome = dados_pessoa[0]
idade = int(dados_pessoa[1])
peso = float(dados_pessoa[2])
sexo = dados_pessoa[3]
altura = float(dados_pessoa[4])
fator = dados_pessoa[5]


'''TESTE
print(dados_pessoa)
print("TESTE")
print(dieta)
print(alimentos)
print(lista_dias)
print(TMB)
print(IMC)
'''



#atribuindo valores da taxa metabolica e IMC  
TMB = FGBenedict(sexo,peso,altura,idade)
TMB = grau_atividade(TMB,fator)
IMC = IMC(peso,altura)

#inserção de alimento nas listas dos dias 
for alimento in lista_dias:
    if alimento[0:5] == '06/04':
        dia1+=alimento + ','
    elif alimento[0:5] == '07/04':
        dia2+=alimento+ ','
    elif alimento[0:5] == '08/04':
        dia3+=alimento+ ','
    elif alimento[0:5] == '09/04':
        dia4+=alimento+ ','
    elif alimento[0:5] == '10/04':
        dia5+=alimento+ ','
    elif alimento[0:5] == '11/04':
        dia6+=alimento+ ','
    elif alimento[0:5] == '12/04':
        dia7+=alimento+ ','
    
    
dia1 = ('').join(dia1)
dia2 = ('').join(dia2)
dia3 = ('').join(dia3)
dia4 = ('').join(dia4)
dia5 = ('').join(dia5)
dia6 = ('').join(dia6)
dia7 = ('').join(dia7)


dia1 = dia1.split(',')

'''print(dia1)
print(dia1[1:13:3])
print(dia1[2:13:3])'''
    


#Cria um catalogo de todos alimentos 
catalogo_alimentos(catalogo,alimentos)

for i in range(1,13,3):#primeiro dia
    b = (float(catalogo[dia1[i]][1])*float((dia1[i+1]))/100)#separa apenas calorias
    #codigo que soma cada membro de b
    c = (float(catalogo[dia1[i]][2])*float((dia1[i+1]))/100)#separa apenas proteinas
    #codigo que soma cada membro de b
    d = (float(catalogo[dia1[i]][3])*float((dia1[i+1]))/100)#separa apenas carboidratos
    #codigo que soma cada membro de b
    e = (float(catalogo[dia1[i]][4])*float((dia1[i+1]))/100)#separa apenas gorduras
    


    
        