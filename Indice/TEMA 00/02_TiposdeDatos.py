import streamlit as st
import utils

st.title("Tipos de Datos")

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

st.header("Estructuración de los Datos")
st.markdown("""""",unsafe_allow_html=True)

est1, est2, est3 = st.columns(3)
with est1:
    with st.container(border=True):
        st.markdown("""""", unsafe_allow_html=True)
with est2:
    with st.container(border=True):
        st.markdown("""""", unsafe_allow_html=True)
with est3:
    with st.container(border=True):
        st.markdown("""""", unsafe_allow_html=True)

st.header("Tipos de Datos")

st.subheader("Datos Númericos:")
st.markdown("""""", unsafe_allow_html=True)

num1, num2 = st.columns(2)
with num1:
    with st.expander("Números Enteros"):
        st.markdown("""""", unsafe_allow_html=True)
with num2:
    with st.expander("Números Decimalos"):
        st.markdown("""""", unsafe_allow_html=True)

st.subheader("Datos de Texto:")
st.markdown("""""", unsafe_allow_html=True)

tex1, tex2 = st.columns(2)
with tex1:
    st.markdown("""""", unsafe_allow_html=True)
    st.markdown("""""", unsafe_allow_html=True)
with tex2:
    st.markdown("""""", unsafe_allow_html=True)
    st.markdown("""""", unsafe_allow_html=True)
    
with st.expander("¿Cuando Utilizar Cada Uno?"):
    st.markdown("""""", unsafe_allow_html=True)

st.subheader("Datos de Fecha:")
st.markdown("""""", unsafe_allow_html=True)

fech1, fech2 = st.columns(2)
with fech1:
    st.markdown("""""", unsafe_allow_html=True)
    st.markdown("""""", unsafe_allow_html=True)
with fech2:
    st.markdown("""""", unsafe_allow_html=True)
    st.markdown("""""", unsafe_allow_html=True)
    
utils.cambio_pag(ant="Indice/TEMA 00/01_Introduccion.py", sig="Indice/TEMA 01/00_Normalizacion.py")