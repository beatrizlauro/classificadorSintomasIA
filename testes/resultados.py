import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split

# Carregar o dataset
df = pd.read_csv('data/limpos/Português/baseDeDados_limpo.csv')
df.columns = df.columns.str.strip().str.lower()

# Preparar os dados
sintomas_colunas = [col for col in df.columns if col.startswith('sintoma')]
df['sintomas_texto'] = df[sintomas_colunas].fillna('').astype(str).agg(' '.join, axis=1)

X = df['sintomas_texto']
y = df['doenca']

# Carregar o modelo e o vetorizador
vectorizer = joblib.load('models/vectorizer.pkl')
modelo = joblib.load('models/modelo_final.pkl')

# Transformar os dados
X_vect = vectorizer.transform(X)

# Dividir dados (igual ao treino)
X_train, X_test, y_train, y_test = train_test_split(X_vect, y, test_size=0.2, random_state=42)

# Fazer previsões
y_pred = modelo.predict(X_test)

#  Matriz de Confusão
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8,6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title(' Matriz de Confusão')
plt.xlabel('Predito')
plt.ylabel('Verdadeiro')
plt.tight_layout()
plt.savefig('results/matriz_confusao.png')  # Salva como imagem
plt.show()

# 🔹 Relatório de Classificação
print("\n=== Relatório de Classificação ===")
print(classification_report(y_test, y_pred))

#  Salva também o relatório em arquivo texto
with open('results/relatorio_classificacao.txt', 'w') as f:
    f.write(classification_report(y_test, y_pred))

print("\n✅ Matriz de confusão salva em 'results/matriz_confusao.png'")
print("✅ Relatório salvo em 'results/relatorio_classificacao.txt'")
