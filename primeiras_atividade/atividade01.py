valor_em_reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

valor_em_dolares = valor_em_reais / taxa_dolar
valor_em_euros = valor_em_reais / taxa_euro

print("Valor em Reais: R$", valor_em_reais)
print("Valor em Dólares: $", round(valor_em_dolares, 2))
print("Valor em Euros: €", round(valor_em_euros, 2))