# Arquivo feito para testar o modelo. INSTRUÇÕES:
# 1. Inserir sintomas na variável *entrada*
# 2. Rodar o comando python teste_modelo.py
import joblib

# Carrega o modelo e o vetor
modelo = joblib.load('models/modelo_final.pkl')
vectorizer = joblib.load('models/vectorizer.pkl')

# Exemplo de entrada do usuário
entrada = "tremendo calafrios"

entrada_vect = vectorizer.transform([entrada])
predicao = modelo.predict(entrada_vect)

print("Doença prevista:", predicao[0])
