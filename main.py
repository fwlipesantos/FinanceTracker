import time
import pandas as pd
from consulta import Acao 

acoes = [
    'PETR4.SA', 'ITUB4.SA', 'BBDC4.SA', 'VALE3.SA', 'ABEV3.SA',
    'MGLU3.SA', 'BBAS3.SA', 'AMER3.SA', 'ITSA4.SA', 'ELET6.SA',
    'PETR3.SA', 'SUZB3.SA', 'GGBR3.SA', 'AMER3.SA', 'XPBR31.SA',
    'RADL3.SA', 'VIVT3.SA', 'HYPE3.SA'
]

def atualizar_dados():
    excel = []

    for ticket in acoes:
        acao = Acao(ticket)  
        excel.append({
            'Ação': ticket,
            'Abertura': f"R$ {acao.open():.2f}".replace('.', ','),
            'Baixa': f"R$ {acao.low():.2f}".replace('.', ','),
            'Alta': f"R$ {acao.high():.2f}".replace('.', ','),
            'Fechamento': f"R$ {acao.close():.2f}".replace('.', ',')
        })

    df = pd.DataFrame(excel)
    df.to_excel('dados.xlsx', index=False)  
    print("Dados atualizados")

while True:
    atualizar_dados()
    time.sleep(300) 
    

