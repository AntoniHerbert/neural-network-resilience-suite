import csv

def cortar_csv(arquivo_entrada, arquivo_saida, ate_linha):
    with open(arquivo_entrada, 'r', newline='', encoding='utf-8') as infile:
        reader = list(csv.reader(infile))
    
    header = reader[0]
    dados = reader[1:ate_linha + 1]
    
    with open(arquivo_saida, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(header)
        writer.writerows(dados)

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

entrada = os.path.join(BASE_DIR, "mlbfa_output.csv")
saida = os.path.join(BASE_DIR, "mlbfa_output_capado.csv")

cortar_csv(entrada, saida, 439)