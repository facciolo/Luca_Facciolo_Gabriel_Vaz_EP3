dia1 = []
dia2 = []
dia3 = []
dia4 = []
dia5 = []
dia6 = []
dia7 = []
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
    return dia1,dia2,dia3,dia4,dia5,dia6,dia7
def compara_alimento(lista_dias,alimentos):
    for alimento in lista_dias:
        None
    for alimento2 in alimentos:
        None
    if alimento[0:5] == alimento2[0:5]:
        return alimento2

def IMC(peso,altura):
    return (1.3*peso)/(altura**2.5)

def catalogo_alimentos(catalogo,alimentos):
    for termo in alimentos:
        valores = []
        linha = []
        linha = termo.split(',')
        for numero in linha[1:]:
            valores.append(float(numero))
        catalogo[linha[0]] = valores
    return catalogo
    
    