import yfinance as yf

acoes = [
    'PETR4.SA', 'ITUB4.SA', 'BBDC4.SA', 'VALE3.SA', 'ABEV3.SA', 'MGLU3.SA', 
    'BBAS3.SA', 'AMER3.SA', 'ITSA4.SA', 'ELET6.SA', 'PETR3.SA', 'SUZB3.SA', 
    'GGBR3.SA', 'AMER3.SA', 'XPBR31.SA', 'RADL3.SA', 'VIVT3.SA', 'HYPE3.SA'
]

class Acao:
    def __init__(self, ticketApi):
        self.ticketApi = ticketApi

    def open(self):
        ticket_open = yf.Ticker(self.ticketApi)
        output = ticket_open.history(period='1d')
        return output['Open'].iloc[0]
    
    def low(self):
        ticket_low = yf.Ticker(self.ticketApi)
        output = ticket_low.history(period='1d')
        return output['Low'].iloc[0]
    
    def high(self):
        ticket_high = yf.Ticker(self.ticketApi)
        output = ticket_high.history(period='1d')
        return output['High'].iloc[0]
    
    def close(self):
        ticket_closed = yf.Ticker(self.ticketApi)
        output = ticket_closed.history(period='1d')
        return output['Close'].iloc[0]

def consultar_acoes():
    excel = []  
    
    for ticket in acoes:
        acao = Acao(ticket) 

       
        excel.append({
            'Ação': ticket,
            'Abertura': f"R$ {acao.open():.2f}".replace('.',','),
            'Baixa': f"R$ {acao.low():.2f}".replace('.',','),
            'Alta': f"R$ {acao.high():.2f}".replace('.',','),
            'Fechamento': f"R$ {acao.close():.2f}".replace('.',',')
        })

    return excel  
