import json

def analisa_faturamento(faturamento_diario):
    if not faturamento_diario:
        return None, None, 0

    
    faturamento_validos = [item['valor'] for item in faturamento_diario if item['valor'] > 0] # Tratando os dados

    if not faturamento_validos:
        return None, None, 0

    
    menor_faturamento = min(faturamento_validos) 
    maior_faturamento = max(faturamento_validos)
    media_mensal = sum(faturamento_validos) / len(faturamento_validos)

    
    dias_acima_da_media = sum(1 for valor in faturamento_validos if valor > media_mensal) # <- Contando os Dias a acima da media 

    return menor_faturamento, maior_faturamento, dias_acima_da_media, media_mensal


with open('dados.json', 'r') as arquivo: # <- Lendo o arquivo JSON
    dados = json.load(arquivo)

menor, maior, dias_acima_media, media = analisa_faturamento(dados) # Chamando a função e exibindo os resultados
print("--Relatório do faturamento--")
print(f"Menor valor -> {menor}")
print(f"Maior valor -> {maior}")
print(f"Número de dias com faturamento superior à média mensal -> {dias_acima_media}")
print(f"media total: {media}")