TMB = 0
lista_alimentos = open("alimentos.csv","r+",encoding = "utf-8")
pessoa = open("usuário.csv","r+",encoding = "utf-8")
dieta = pessoa.read()
dados_alimentospessoa = dieta.split('\n', 3)[3]
dados_pessoa = dieta.split('\n', 10)[1]#comando que separa as informações pessoais do individuo
lista=dados_pessoa.split(",")

lista_dias=dados_alimentospessoa.split('\n')

alimento_1=lista_dias[0]
alimento_2=lista_dias[1]
alimento_3=lista_dias[2]
alimento_4=lista_dias[3]

print(alimento_1[0:5])
#(linhas 10-15) Definição dos parametros pessoais utilizados 
nome = lista[0]
idade = int(lista[1])
peso = float(lista[2])
sexo = lista[3]
altura = float(lista[4])
fator = lista[5]

alimentos = lista_alimentos.read()
alimentos2 = alimentos.split('\n',1)[1]#comando que separa os alimentos em suas respectivas linhas
print(dados_pessoa)
print("TESTE")
print(dados_alimentospessoa)
#print(alimentos2)


def FGBenedict():#função que define a taxa metábolica
#OBS: peso em kilos , altura em cm e idade em anos
    if sexo == "M":
        TMB = 88.36 + (13.4*peso) + (4.8*altura) - (5.7*idade)
    else:
        TMB = 447.6 + (9.2*peso) + (3.1*altura) - (4.3*idade)
    return TMB
    
TMB = FGBenedict()
        
def grau_atividade():
    global TMB
    if fator == "mínimo":
        TMB = TMB*1.2
    elif fator == "baixo":
        TMB = TMB*1.375
    elif fator == "médio":
        TMB = TMB*1.55
    elif fator == "alto":
        TMB = TMB*1.725
    elif fator == "muito alto":
        TMB = TMB*1.9
    return TMB
grau_atividade()
print(TMB)


    
    
    
    
    
        