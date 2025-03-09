import streamlit as st
from PIL import Image
import inteligencia

st.set_page_config(layout='wide')
chave = st.secrets["GEMINI_CHAVE"]


head1, head2, head3 = st.columns ([2, 2, 10], vertical_alignment="bottom")
with head1:
     st.image("arquivos/ARROZ.jpg", width=255)
with head2:
        st.image("arquivos/CHOCOLATE.jpg", width=122)
with head3:
    st.title(":violet[RECEITA BOT]")
    st.subheader("O seu assistente virtual pra criar receitas!")

col1, col2 = st.columns ([2, 2])

with col1:
    st.header("Faça o upload de uma foto com os ingredientes.")
    arquivo_foto = st.file_uploader("", type=["jpg", "jpeg", "png"])
    if arquivo_foto is not None:
        imagem = Image.open(arquivo_foto)
        st.image(imagem)
        with st.spinner("O Receita Bot está dando uma olhada..."):
            if st.button("Detectar Possiveis Receitas "):
                st.session_state.ingredientes = inteligencia.detectar_ingredientes(chave, imagem)
                st.session_state.receitas = inteligencia.possiveis_receitas(chave,st.session_state.ingredientes)

    if 'ingredientes' in st.session_state:
        st.write(f":violet[Ingredientes Detectados]: {st.session_state.ingredientes}")
        st.write(":violet[Possiveis Receitas]")
        for id, receita in enumerate(st.session_state.receitas, start=1):
            st.write(f"{id}. {receita}")

with col2:
    if 'receitas' in st.session_state:
        st.header("Escolha uma Receita")
        receita_selecionada = st.selectbox("", st.session_state.receitas)
        with st.spinner("O Receita Bot está criando a receita..."):
            if st.button ("Ver Receita"):
                st.session_state.receita_completa = inteligencia.receita_completa(chave,
                                                                                  st.session_state.ingredientes,
                                                                                  receita_selecionada)
                st.write(st.session_state.receita_completa)