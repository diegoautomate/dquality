import streamlit as st



def main():
    
    st.set_page_config(page_title="Validação de CSV", page_icon=":bar_chart:", layout="wide")
    
    st.title("Validação de CSV - DataQuality")

    st.file_uploader("Selecione o arquivo CSV", type=['csv'])

if __name__ == '__main__':
    main()