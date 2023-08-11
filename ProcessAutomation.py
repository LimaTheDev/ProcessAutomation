import yfinance as yf 

dados = yf.Ticker("PETR4.SA").history("6mo")
print(dados)

fechamento = dados.Close

print(fechamento)