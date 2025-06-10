
import pandas as pd
import unidecode

# Funções auxiliares
def padronizar_texto(texto):
    if pd.isnull(texto):
        return ''
    texto = str(texto).strip().lower()
    texto = unidecode.unidecode(texto).replace('ç', 'c')
    texto = ' '.join(texto.split())
    texto = texto.replace(' ', '_')
    return texto

def normalizar_sintomas(sintomas_str, mapa_sintomas):
    sintomas = sintomas_str.split(',')
    sintomas_norm = [mapa_sintomas.get(s.strip().lower(), s.strip().lower()) for s in sintomas]
    return ', '.join(sorted(set(sintomas_norm)))

# Dicionário de normalização de sintomas (exemplo inicial)
mapa_sintomas = {
    "cefaleia": "dor de cabeca",
    "dor na cabeca": "dor de cabeca",
    "febril": "febre",
    "cansaco extremo": "fadiga",
}

# Carregar datasets com os novos nomes
baseDeDados = pd.read_csv('baseDeDados.csv')
sintomas_Descricao = pd.read_csv('sintomas_Descricao.csv')
sintomas_Gravidade = pd.read_csv('sintomas_Gravidade.csv')
sintomas_Precaucao_Tratamento = pd.read_csv('sintomas_Precaucao_Tratamento.csv')

# Padronizar e limpar colunas relevantes
for df in [baseDeDados, sintomas_Descricao, sintomas_Gravidade, sintomas_Precaucao_Tratamento]:
    for col in df.columns:
        df[col] = df[col].apply(padronizar_texto)

# Aplicar normalização de sintomas em colunas de sintomas do baseDeDados
if 'sintomas' in baseDeDados.columns:
    baseDeDados['sintomas'] = baseDeDados['sintomas'].apply(lambda x: normalizar_sintomas(x, mapa_sintomas))
    baseDeDados['sintomas_lista'] = baseDeDados['sintomas'].apply(lambda x: [s.strip() for s in x.split(',') if s.strip()])

# Salvar datasets limpos com os mesmos nomes adicionando sufixo '_limpo'
baseDeDados.to_csv('baseDeDados_limpo.csv', index=False)
sintomas_Descricao.to_csv('sintomas_Descricao_limpo.csv', index=False)
sintomas_Gravidade.to_csv('sintomas_Gravidade_limpo.csv', index=False)
sintomas_Precaucao_Tratamento.to_csv('sintomas_Precaucao_Tratamento_limpo.csv', index=False)

print("Limpeza concluída. Arquivos salvos com sufixo '_limpo'.")
