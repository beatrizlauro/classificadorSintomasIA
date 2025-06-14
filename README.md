# 🧠 Classificador de Sintomas com IA

## 📌 Objetivo

O projeto **Classificador de Sintomas com IA** tem como principal objetivo auxiliar no diagnóstico preliminar de condições de saúde com base nos sintomas relatados pelo usuário. A ideia é criar uma ferramenta inteligente, acessível e fácil de usar, que possa ser utilizada por qualquer pessoa para obter uma sugestão de possível condição clínica antes de buscar atendimento médico profissional.

Este sistema visa:

- Reduzir o tempo de decisão entre perceber sintomas e procurar ajuda médica.
- Oferecer uma base educacional sobre possíveis condições relacionadas a certos sintomas.
- Demonstrar, na prática, a aplicação de conceitos de Inteligência Artificial no domínio da saúde.


## 🛠️ Tecnologias e Ferramentas Utilizadas



## ▶️ Instruções de Execução

### 1️⃣ Instalação
1️⃣ Instalação
Certifique-se de ter Python 3.6 ou superior instalado.

Clone este repositório:

bash
git clone https://github.com/beatrizlauro/classificadorSintomasIA.git
cd seu-repositorio
(Opcional) Ative um ambiente virtual:

Windows:

bash
python -m venv env
env\Scripts\activate
macOS / Linux:

bash
python3 -m venv env
source env/bin/activate
Instale as dependências:

bash
pip install -r requirements.txt
2️⃣ Estrutura do Projeto
bash
📂 interface/     # Interface com o usuário usando Streamlit
📂 models/        # Modelos treinados (.pkl)
  ├── modelo_final.pkl
  └── vectorizer.pkl
📂 data/          # Base de dados para treinamento
📂 scripts/       # Scripts para pré-processamento e treino
🚀 3. Executando a Interface
Após garantir que os arquivos do modelo modelo_final.pkl e vectorizer.pkl estão na pasta models/, execute:

bash
streamlit run interface/interface.py
Isso abrirá a aplicação no navegador, permitindo entrada de sintomas e previsão de doenças.

## 📊 Resultados Obtidos

O modelo foi avaliado utilizando Naive Bayes com vetorização de texto, apresentando os seguintes resultados:

- ✅ **Acurácia:** 85% (exemplo, preencher com o valor real)
- ✅ **Precisão, Recall e F1-score:** Conforme relatório gerado.

### 🔹 Matriz de Confusão:
![Matriz de Confusão](results/matriz_confusao.png)

### 🔹 Distribuição de Doenças no Dataset:
![Distribuição de Doenças](results/distribuicao_doencas.png)

### 🔹 Exemplo de Uso:
- 🔍 Entrada: `febre dor de cabeça cansaço`
- ✅ Saída: `Dengue` (Exemplo)

> O modelo funciona tanto via interface Streamlit quanto via script ou notebook.


## 👥 Créditos

Projeto desenvolvido por:

- Beatriz da Costa Lauro  
- Brenda Bonaita de Oliveira  
- José Rodrigues de França  
- Julia Alves de Brito  

Como parte da disciplina de **Inteligência Artificial** – Curso de **Sistemas de Informação**, 5º período – 2025.
