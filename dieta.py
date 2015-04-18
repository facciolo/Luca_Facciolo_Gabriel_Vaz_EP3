informação_pessoal = []
lista_alimentos = open("alimentos.csv","r+",encoding = "utf-8")
pessoa = open("usuário.csv","r+",encoding = "utf-8")
dieta = pessoa.read()
dados_alimentospessoa = dieta.split('\n', 3)[3]
dados_pessoa = dieta.split('\n', 10)[1]#comando que separa as informações pessoais do individuo
#informação_pessoal.append(dados_pessoa) por enquanto isso da na mesma do que o comando acima
'''nome = informação_pessoal[0]
idade = informação_pessoal[1]
peso = informação_pessoal[2]
sexo = informação_pessoal[3]
altura = informação_pessoal[4]
fator = informação_pessoal[5]
tentar separar o dados_pessoa em diferentes membros e inseri-lo na lista
para que possamos definir mais ou menos como está escrito acima '''
alimentos = lista_alimentos.read()
alimentos2 = alimentos.split('\n',1)[1]#comando que separa os alimentos em suas respectivas linhas
print(dados_pessoa)
print("TESTE")
print(dados_alimentospessoa)

#print(alimentos2)
TMB = 0
#idade,peso,sexo,altura = dados_pessoa

def FGBenedict(idade,peso,sexo,altura):#função que define a taxa metábolica
    if sexo == M:
        TMB = 88.36 + (13.4*peso) + (4.8*altura) - (5.7*idade)
    else:
        TMB = 447.6 + (9.2*peso) + (3.1*altura) - (4.3*idade)
    return TMB
TMB = FGBenedict
        

#OBS: peso em kilos , altura em cm e idade em anos

"""fator é o que está escrito na lista "usuário". A ideia é fazer o python ler e
nós colocamos ele aqui"""
def grau_atividade(TMB,fator):
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

    
    
    
    
    
        