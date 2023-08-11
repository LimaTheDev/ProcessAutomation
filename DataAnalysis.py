import yfinance as yf 

dados = yf.Ticker("PETR4.SA").history("6mo")
print(dados)

fechamento = dados.Close

print(fechamento)

maxima = round(fechamento.max(), 2)
minima = round(fechamento.min(), 2)
atual = round(fechamento[-1], 2) 

print(f"A cotação maxima é: R${maxima}")
print(f"A cotação minima é: R${minima}")
print(f"A cotação atual é: R${atual}")
