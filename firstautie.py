# Restante do seu código Streamlit...
streamlit run app.py
# Inicie um repositório Git no diretório do seu projeto
git init
# app.py
print(app.py)
# Adicione o arquivo ao controle de versão do Git
git add app.py
# Confirme as alterações no repositório Git
git commit -m "Iniciar o projeto"
# Instale o Streamlit usando o pip
pip install streamlit
# streamlit_app.py
import streamlit as st

def main():
    st.write("Olá, mundo no Streamlit!")

if __name__ == "__main__":
    main()
# Execute o aplicativo Streamlit
streamlit run streamlit_app.py
