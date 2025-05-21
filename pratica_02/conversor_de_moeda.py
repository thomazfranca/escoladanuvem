# Conversor de Moeda 
# Crie um programa que converte um valor em reais para dólares e euros. 
# Use os seguintes dados:- Valor em reais: R$ 100.00- Taxa do dólar: R$ 5.70- Taxa do euro: R$ 6.40O 
# programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.# Conversor de Moeda

# Conversor de Moeda

# Dados
valor_em_reais = 100.00
taxa_dolar = 5.70
taxa_euro = 6.40

# Conversão
valor_em_dolar = valor_em_reais / taxa_dolar
valor_em_euro = valor_em_reais / taxa_euro

# Exibição dos resultados com vírgula como separador decimal
print(f"Valor em reais: R$ {valor_em_reais:.2f}".replace('.', ','))
print(f"Valor convertido em dólares: US$ {valor_em_dolar:.2f}".replace('.', ','))
print(f"Valor convertido em euros: € {valor_em_euro:.2f}".replace('.', ','))

