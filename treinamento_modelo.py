import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import classification_report, confusion_matrix
import joblib

# Carrega o dataset
df = pd.read_csv('data/limpos/Português/baseDeDados_limpo.csv')

# Corrige nomes das colunas (remove espaços e coloca em minúsculas)
df.columns = df.columns.str.strip().str.lower()

# Corrige erro: encontra colunas que **começam com 'sintoma'**
sintomas_colunas = [col for col in df.columns if col.startswith('sintoma')]

# 🔁 Junta os sintomas em uma única string por linha
df['sintomas_texto'] = df[sintomas_colunas].fillna('').astype(str).agg(' '.join, axis=1)

# Input (X) e saída (y)
X = df['sintomas_texto']
y = df['doenca']

# Vetorização
vectorizer = CountVectorizer()
X_vect = vectorizer.fit_transform(X)

# Treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X_vect, y, test_size=0.2, random_state=42)
modelo = MultinomialNB()
modelo.fit(X_train, y_train)

# Avaliação
y_pred = modelo.predict(X_test)
print("Matriz de Confusão:")
print(confusion_matrix(y_test, y_pred))
print("\nRelatório de Classificação:")
print(classification_report(y_test, y_pred))

# Salva o modelo e o vetorizador
joblib.dump(modelo, 'models/modelo_final.pkl')
joblib.dump(vectorizer, 'models/vectorizer.pkl')
