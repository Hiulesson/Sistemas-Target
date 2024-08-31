import json

def analisa_faturamento(faturamento_diario):
    if not faturamento_diario:
        return None, None, 0

    # Tratando os dados
    faturamento_validos = [item['valor'] for item in faturamento_diario if item['valor'] > 0]

    if not faturamento_validos:
        return None, None, 0

    # Calcula o menor e o maior valor de faturamento
    menor_faturamento = min(faturamento_validos)
    maior_faturamento = max(faturamento_validos)

    # Calculo da média mensal
    media_mensal = sum(faturamento_validos) / len(faturamento_validos)

    # Contando os Dias a acima da media 
    dias_acima_da_media = sum(1 for valor in faturamento_validos if valor > media_mensal)

    return menor_faturamento, maior_faturamento, dias_acima_da_media, media_mensal

# Lendo o arquivo JSON
with open('faturamento_agosto.json', 'r') as arquivo:
    dados = json.load(arquivo)

faturamento_diario = dados['faturamento_diario']

# Chamando a função e exibindo os resultados
menor, maior, dias_acima_media, media = analisa_faturamento(faturamento_diario)

print(f"Menor valor de faturamento: {menor}")
print(f"Maior valor de faturamento: {maior}")
print(f"Número de dias com faturamento superior à média mensal: {dias_acima_media}")
print(f"media total{media}")