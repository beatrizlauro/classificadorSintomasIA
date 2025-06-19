import streamlit as st
import joblib
import os

# Definir caminhos corretos para modelo e vetorizador
vectorizer_path = os.path.join(os.path.dirname(__file__), "..", "models", "vectorizer.pkl")
modelo_path = os.path.join(os.path.dirname(__file__), "..", "models", "modelo_final.pkl")

# Carregar o modelo treinado e o vetorizador
vectorizer = joblib.load(vectorizer_path)
modelo = joblib.load(modelo_path)

# Configuração da interface
st.title("🩺 Classificador de Sintomas com IA")
st.write("Digite seus sintomas abaixo para obter uma previsão.")

# Entrada do usuário
sintomas_usuario = st.text_area("📝 Sintomas:", "")

# Predição
if st.button("🔍 Classificar"):
    if sintomas_usuario.strip():
        sintomas_vetorizados = vectorizer.transform([sintomas_usuario])
        
        # Obter as probabilidades de cada doença
        probabilidades = modelo.predict_proba(sintomas_vetorizados)[0]
        
        # Combinar classes e probabilidades
        doencas_com_prob = list(zip(modelo.classes_, probabilidades))
        
        # Ordenar por probabilidade decrescente
        doencas_ordenadas = sorted(doencas_com_prob, key=lambda x: x[1], reverse=True)
        
        # Montar texto com as top 5 doenças e porcentagens, formatado para exibir no st.success
        resultados_texto = "\n".join(
            f"{doenca.replace('_', ' ')};"
            for doenca, prob in doencas_ordenadas[:5]
        )
        
        st.success(f"Possíveis diagnósticos:\n{resultados_texto}")
    else:
        st.warning("⚠️ Por favor, insira sintomas antes de classificar.")
