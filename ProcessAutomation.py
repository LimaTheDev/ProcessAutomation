import yfinance as yf 

ticker = input("Digite o código da ação: ")
dados = yf.Ticker(ticker).history("6mo")
print(dados)

fechamento = dados.Close

print(fechamento)