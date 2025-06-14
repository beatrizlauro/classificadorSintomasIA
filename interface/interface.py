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
        previsao = modelo.predict(sintomas_vetorizados)
        st.success(f"**Possível diagnóstico:** {previsao[0]}")
    else:
        st.warning("⚠️ Por favor, insira sintomas antes de classificar.")
