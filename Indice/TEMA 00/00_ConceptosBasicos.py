import streamlit as st
import utils

st.title("🧩 Conceptos Básicos")

st.markdown("""
    <style>
    .justificar {
        text-align: justify;
    }
    .destacar {
        color: #FF4B4B;
        font-weight: bold;
    }
    .contenedor {
        background-color: #1E2023;
        padding: 15px;
        border-radius: 5px;
        border-left: 5px solid #FF4B4B;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

st.subheader("☁️ Base de Datos")
st.markdown("""<div class="justificar">
                    <p>⚠️ En construcción... </p>
                    </div>""", unsafe_allow_html=True)

bd1, bd2 = st.columns(2)
with bd1:
       with st.container(border=True):
         st.markdown('''<b class="destacar">🎯 Relacionales</b><br>
                   ⚠️ En construcción...
                   ''',  unsafe_allow_html=True)
with bd2:
       with st.container(border=True):
         st.markdown('''<b class="destacar">🎯 No Relacionales</b><br>
                   ⚠️ En construcción...
                   ''',  unsafe_allow_html=True)

st.subheader("💡 Entidades")
st.markdown("""<div class="justificar">
                    <p>⚠️ En construcción... </p>
                    </div>""", unsafe_allow_html=True)

ent1, ent2 = st.columns(2)
with ent1:
    with st.expander("⚡️ :red[**Entidades Fuertes**]", expanded=True):
        st.markdown("""<div class="justificar">
                    <p>⚠️ En construcción... </p>
                    </div>""", unsafe_allow_html=True)
with ent2:
    with st.expander("⚡️ :red[**Entidades Debiles**]", expanded=True):
        st.markdown("""<div class="justificar">
                    <p>⚠️ En construcción... </p>
                    </div>""", unsafe_allow_html=True)

st.subheader("🌱 Campos y  Atributos")
st.markdown("""<div class="justificar">
                    <p>⚠️ En construcción... </p>
                    </div>""", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown("""<div class="contenedor">
                    <b class="destacar">🌼 Campo </b><br>
                    ⚠️ En construcción... 
                    </div>""", unsafe_allow_html=True)
with col2:
    st.markdown("""<div class="contenedor">
                    <b class="destacar">🌻 Atributos </b><br>
                    ⚠️ En construcción... 
                    </div>""", unsafe_allow_html=True)
        
st.subheader("📌 Registros")
st.markdown("""<div class="justificar">
                    <p>⚠️ En construcción... </p>
                    </div>""", unsafe_allow_html=True)

st.subheader("📌 Archivos")
st.markdown("""<div class="justificar">
                    <p>⚠️ En construcción... </p>
                    </div>""", unsafe_allow_html=True)

st.subheader("📌 Relación")
st.markdown("""<div class="justificar">
                    <p>⚠️ En construcción... </p>
                    </div>""", unsafe_allow_html=True)

st.subheader("📌 Cardinalidad")
st.markdown("""<div class="justificar">
                    <p>⚠️ En construcción... </p>
                    </div>""", unsafe_allow_html=True)

st.subheader("🔑 Clave Primaria PK")
st.markdown("""<div class="justificar">
                    <p>⚠️ En construcción... </p>
                    </div>""", unsafe_allow_html=True)

pk1, pk2 = st.columns(2)
with pk1:
    with st.expander("📂 :red[**Simples**] ✨", expanded=True):
        st.markdown("""<div class="justificar">
                    <p>⚠️ En construcción... </p>
                    </div>""", unsafe_allow_html=True)
with pk2:
    with st.expander("📂 :red[**Compuestas**] ✨", expanded=True):
        st.markdown("""<div class="justificar">
                    <p>⚠️ En construcción... </p>
                    </div>""", unsafe_allow_html=True)

st.subheader("🔑 Clave Fóranea FK")
st.markdown("""<div class="justificar">
                    <p>⚠️ En construcción... </p>
                    </div>""", unsafe_allow_html=True)

utils.cambio_pag(ant="Indice/00_inicio.py", sig="Indice/TEMA 00/01_Introduccion.py")