import streamlit as st
import utils

st.title("Introducción a las Bases de Datos")

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

st.header("¿Qué son las Bases de Datos?")
st.markdown('''''',  unsafe_allow_html=True)

def1, def2 = st.columns(2)
with def1:
    st.markdown('''''',  unsafe_allow_html=True)
with def1:
    st.markdown('''''',  unsafe_allow_html=True) 

st.subheader("Qué es un Sistema de Bases de Datos")
st.markdown('''''',  unsafe_allow_html=True)

st.header("Tipos de Bases de Datos")

bd1, bd2 = st.columns(2)
with bd1:
    st.subheader("Bases de Datos Relacionales")
    st.markdown('''''',  unsafe_allow_html=True)
with bd2:
    st.subheader("Bases de Datos No Relacionales")
    st.markdown('''''',  unsafe_allow_html=True)

st.header("Bases de Datos Relacionales")
st.markdown('''''',  unsafe_allow_html=True)

st.subheader("Elementos de una Base de Datos")

ele1, ele2 = st.columns(2)
with ele1:
    st.markdown('''''',  unsafe_allow_html=True)
    st.markdown('''''',  unsafe_allow_html=True)
with ele2:
    st.markdown('''''',  unsafe_allow_html=True)
    st.markdown('''''',  unsafe_allow_html=True)

st.subheader("Operaciones Princpales en Una Base de Datos")
st.markdown('''''',  unsafe_allow_html=True)

st.header("Claves Primarias y Foraneas:")
st.markdown('''''',  unsafe_allow_html=True)

pk, fk = st.columns(2)
with pk:
    st.subheader("Reglas de las Llaves Primarias")
    st.markdown('''''',  unsafe_allow_html=True)
with fk:
    st.subheader("Reglas de las Llaves Primarias")
    st.markdown('''''',  unsafe_allow_html=True)

st.subheader("Tipos de Llaves Primarias")

utils.cambio_pag(ant="Indice/GENERAL/00_inicio.py", sig="Indice/TEMA 01/00_Normalizacion.py")