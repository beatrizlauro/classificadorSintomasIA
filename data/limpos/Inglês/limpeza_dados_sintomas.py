import pandas as pd
import unidecode

# Funções auxiliares
def padronizar_texto(texto):
    if pd.isnull(texto):
        return ''
    texto = str(texto).strip().lower()
    texto = unidecode.unidecode(texto)
    texto = ' '.join(texto.split())
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

# Carregar datasets
dataset = pd.read_csv('dataset.csv')
symptom_description = pd.read_csv('symptom_Description.csv')
symptom_precaution = pd.read_csv('symptom_Precaution.csv')
symptom_severity = pd.read_csv('symptom_Severity.csv')

# Padronizar e limpar colunas relevantes
for df in [dataset, symptom_description, symptom_precaution, symptom_severity]:
    for col in df.columns:
        df[col] = df[col].apply(padronizar_texto)

# Aplicar normalização de sintomas em colunas de sintomas do dataset
# Ajuste conforme o nome correto da coluna no seu dataset
if 'sintomas' in dataset.columns:
    dataset['sintomas'] = dataset['sintomas'].apply(lambda x: normalizar_sintomas(x, mapa_sintomas))
    dataset['sintomas_lista'] = dataset['sintomas'].apply(lambda x: [s.strip() for s in x.split(',') if s.strip()])

# Salvar datasets limpos
dataset.to_csv('dataset_limpo.csv', index=False)
symptom_description.to_csv('symptom_Description_limpo.csv', index=False)
symptom_precaution.to_csv('symptom_Precaution_limpo.csv', index=False)
symptom_severity.to_csv('symptom_Severity_limpo.csv', index=False)

print("Limpeza concluída. Arquivos salvos com sufixo '_limpo'.")
