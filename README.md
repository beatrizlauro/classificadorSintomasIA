# Classificador de Sintomas com IA

Este projeto implementa um classificador de doenças a partir de descrições de sintomas em texto, utilizando técnicas de processamento de linguagem natural (NLP) e modelos de aprendizado de máquina.

---

## 📂 Estrutura do Projeto

```
classificadorSintomasIA/
├── data/
│   ├── brutos/               # Dados originais em inglês e português
│   └── limpos/               # Dados pré-processados e limpos
│       ├── Português/
│       │   └── baseDeDados_limpo.csv
│       └── Inglês/
├── models/
│   ├── modelo_final.pkl      # Modelo treinado serializado
│   └── vectorizer.pkl        # Vetorizador de texto (TF-IDF)
├── interface/
│   └── interface.py          # Aplicação Streamlit para interação
├── testes/
│   ├── teste.py              # Script de testes manuais de previsão
│   └── resultados.py         # Geração de matriz de confusão e relatório
├── notebook/
│   └── criacaodapasta.txt    # Scripts auxiliares de organização
├── results/                  # Diretório de saída com gráficos e relatórios
└── README.md
```

---

## 🛠 Requisitos

- Python 3.8 ou superior
- Bibliotecas Python:
  - pandas
  - scikit-learn
  - joblib
  - matplotlib
  - seaborn
  - streamlit

Você pode instalar todas as dependências com:

```bash
pip install -r requirements.txt
```

---

## 🚀 Instalação

### 1. Clone este repositório:
   ```bash
   git clone https://github.com/beatrizlauro/classificadorSintomasIA.git 
   cd classificadorSintomasIA
   ```

### 2. Crie o ambiente virtual
   ```bash
   python -m venv venv
   ```

### 3. Ative o ambiente virtual (Linux ou MacOS)

Linux:
   ```bash
   source venv/bin/activate
   ```
Windows:
   ```bash
   venv\Scripts\activate
   ```

### 4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🎯 Uso

### 1. Executar a interface web

Inicie a aplicação Streamlit para inserir sintomas via interface gráfica:
```bash
streamlit run interface/interface.py
````

### 2. Testes manuais via script

Para executar testes de previsão de doenças a partir de exemplos de sintomas:

```bash
python testes/teste.py
```

---

## 📊 Avaliação do Modelo

O modelo foi avaliado usando 80% dos dados para treino e 20% para teste (random\_state=42). As principais métricas de desempenho obtidas foram:

| Métrica                  | Valor |
| ------------------------ | ----- |
| **Acurácia**             | 100%  |
| **Precisão (Macro Avg)** | 100%  |
| **Recall (Macro Avg)**   | 100%  |
| **F1-score (Macro Avg)** | 100%  |

## 📊 Métricas de Desempenho do Modelo

| Classe                                 | Precision | Recall | F1-score | Support |
|----------------------------------------|-----------|--------|----------|---------|
| (vertigem)_vertigem_posicional_paromsal| 1.00      | 1.00   | 1.00     | 18      |
| acne                                   | 1.00      | 1.00   | 1.00     | 24      |
| aids                                   | 1.00      | 1.00   | 1.00     | 30      |
| ...                                    | ...       | ...    | ...      | ...     |

### ✅ Totais

- **Total de amostras:** 984  
- **Acurácia:** 1.00  

| Métrica       | Precision | Recall | F1-score | Support |
|---------------|-----------|--------|----------|---------|
| Macro média   | 1.00      | 1.00   | 1.00     | 984     |
| Média ponderada | 1.00    | 1.00   | 1.00     | 984     |

## 👥 Créditos

Projeto desenvolvido por:

- Beatriz da Costa Lauro  
- Brenda Bonaita de Oliveira  
- José Rodrigues de França  
- Julia Alves de Brito  

Como parte da disciplina de **Inteligência Artificial** – Curso de **Sistemas de Informação**, 5º período – 2025.

