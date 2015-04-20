import funçoesdieta
def alimentodia(alimento):#função que insere os alimentos em seus respectivos dias
    global dia1,dia2,dia3,dia4,dia5,dia6,dia7
    if alimento[0:5] == '06/04':
        dia1+=alimento+'\n'
    elif alimento[0:5] == '07/04':
        dia2+=alimento+'\n'
    elif alimento[0:5] == '08/04':
        dia3+=alimento+'\n'
    elif alimento[0:5] == '09/04':
        dia4+=alimento+'\n'
    elif alimento[0:5] == '10/04':
        dia5+=alimento+'\n'
    elif alimento[0:5] == '11/04':
        dia6+=alimento+'\n'
    elif alimento[0:5] == '12/04':
        dia7+=alimento+'\n'
        
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
alimento_5=lista_dias[4]
alimento_6=lista_dias[5]
alimento_7=lista_dias[6]
alimento_8=lista_dias[7]


dia1 = []
dia2 = []
dia3 = []
dia4 = []
dia5 = []
dia6 = []
dia7 = []
alimentodia(alimento_1)
alimentodia(alimento_2)
alimentodia(alimento_3)
alimentodia(alimento_4)
alimentodia(alimento_5)
alimentodia(alimento_6)
alimentodia(alimento_7)
alimentodia(alimento_8)

print(''.join(dia1))
print(''.join(dia2))
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



    
TMB = funçoesdieta.FGBenedict(sexo,peso,altura,idade)
TMB = funçoesdieta.grau_atividade(TMB,fator)
print(TMB)