import joblib

# Carrega o modelo e o vetorizador
modelo = joblib.load('models/modelo_final.pkl')
vectorizer = joblib.load('models/vectorizer.pkl')

# Função de previsão
def testar_sintomas(sintomas):
    if not sintomas.strip():
        return " Entrada vazia. Insira pelo menos um sintoma."
    sintomas_transformados = vectorizer.transform([sintomas])
    predicao = modelo.predict(sintomas_transformados)
    return predicao[0]

#  Lista de testes simulados
testes = [
    "febre dor de cabeça cansaço",
    "dor no peito falta de ar tontura",
    "tosse dor de garganta nariz entupido",
    "coceira vermelhidão inchaço na pele",
    "dor nas articulações febre cansaço",
    "",  # Entrada vazia
    "palavra inexistente inventada"  # Sintomas estranhos para testar robustez
]

# Executa os testes
print("=== Testes do Classificador de Sintomas ===")
for idx, sintomas in enumerate(testes):
    resultado = testar_sintomas(sintomas)
    print(f"\nTeste {idx+1}:")
    print(f"→ Sintomas informados: '{sintomas}'")
    print(f"→ Resultado da previsão: {resultado}")
