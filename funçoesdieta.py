
def FGBenedict(sexo,peso,altura,idade):#função que define a taxa metábolica
#OBS: peso em kilos , altura em cm e idade em anos
    if sexo == "M":
        TMB = 88.36 + (13.4*peso) + (4.8*altura) - (5.7*idade)
    else:
        TMB = 447.6 + (9.2*peso) + (3.1*altura) - (4.3*idade)
    return TMB

def grau_atividade(TMB,fator):#função que define a taxa metábolica de acordo com a atividade fisica
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
    
def IMC(peso,altura):
    return (1.3*peso)/(altura**2.5)

def catalogo_alimentos(catalogo,alimentos):#cria um dicionario com todos elementos do arquivo alimentos
    for termo in alimentos:
        valores = []
        linha = []
        linha = termo.split(',')
        for numero in linha[1:]:
            valores.append(float(numero))
        catalogo[linha[0]] = valores
    return catalogo
