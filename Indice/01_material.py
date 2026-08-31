import streamlit as st
import utils

st.markdown("""
    <style>
    .justificar {
        text-align: justify;
    }
    .destacar {
        color: #FF4B4B !important;
        font-weight: bold;
    }
    .contenedor {
        background-color: #1E2023;
        padding: 15px;
        border-radius: 5px;
        border-left: 5px solid #FF4B4B;
        border-bottom: 5px solid #FF4B4B;
        margin-bottom: 10px;
    }
    .contenedor-lista {
        background-color: #1E2023;
        padding: 15px;
        border-radius: 5px;
        border-left: 5px solid #FF4B4B;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Material de Apoyo")

st.divider()
st.header(":red[Cursos Gratuitos:]")
st.markdown("""<div class="justificar">
            ⚠️🔨 En Construcción...
            <br><br></div>""", unsafe_allow_html=True)

cur1, cur2, cur3 = st.columns(3, border=True)
with cur1:
  st.subheader("TEMA 00: Diseño de BBDD")
  st.markdown("""<div class="justificar">
            ⚠️🔨 En Construcción...
            <br><br></div>""", unsafe_allow_html=True)
  st.link_button("Curso en GitHub", url="https://github.com/DiscoDurodeRoer/curso-disenio-base-de-datos/tree/master")
with cur2:
  st.subheader("TEMA 03: SQL")
  st.markdown("""<div class="justificar">
            ⚠️🔨 En Construcción...
            <br><br></div>""", unsafe_allow_html=True)
  st.link_button("Curso en GitHub", url="https://github.com/DiscoDurodeRoer/curso-disenio-base-de-datos/tree/master")
with cur3:
  st.subheader("TEMA 04: Power BI")
  st.markdown("""<div class="justificar">
            ⚠️🔨 En Construcción...
            <br><br></div>""", unsafe_allow_html=True)
  st.link_button("Curso en GitHub", url="https://github.com/DiscoDurodeRoer/curso-disenio-base-de-datos/tree/master")

st.divider()

st.header(":red[Vídeos:]")
st.markdown("""<div class="justificar">
            ⚠️🔨 En Construcción...
            <br><br></div>""", unsafe_allow_html=True)

vid1, vid2, vid3, vid4 = st.columns(4, border=True)
with vid1:
  st.subheader("Conceptos Básicos")
  st.markdown("""<div class="justificar">
            ⚠️🔨 En Construcción...
            <br><br></div>""", unsafe_allow_html=True)
  st.link_button("Curso en GitHub", url="https://github.com/DiscoDurodeRoer/curso-disenio-base-de-datos/tree/master")
with vid2:
  st.subheader("TEMA 03: SQL")
  st.markdown("""<div class="justificar">
            ⚠️🔨 En Construcción...
            <br><br></div>""", unsafe_allow_html=True)
  st.link_button("Curso en GitHub", url="https://github.com/DiscoDurodeRoer/curso-disenio-base-de-datos/tree/master")
with vid3:
  st.subheader("EXTRA 01: Python")
  st.markdown("""<div class="justificar">
            ⚠️🔨 En Construcción...
            <br><br></div>""", unsafe_allow_html=True)
  st.link_button("Curso en GitHub", url="https://github.com/DiscoDurodeRoer/curso-disenio-base-de-datos/tree/master")
with vid4:
  st.subheader("EXTRA 04: Git")
  st.markdown("""<div class="justificar">
            ⚠️🔨 En Construcción...
            <br><br></div>""", unsafe_allow_html=True)
  st.link_button("Curso en GitHub", url="https://github.com/DiscoDurodeRoer/curso-disenio-base-de-datos/tree/master")

st.divider()

st.header(":red[Guías y Ejercicios Resueltos:]")
st.markdown("""<div class="justificar">
            ⚠️🔨 En Construcción...
            <br><br></div>""", unsafe_allow_html=True)

guia1, guia2 = st.columns(2)
with guia1:
    with st.container(border=True):
      st.subheader("TEMA 01: Normalización")
      st.markdown("""<div class="justificar">
            ⚠️🔨 En Construcción...
            <br><br></div>""", unsafe_allow_html=True)
      st.link_button("Curso en GitHub", url="https://github.com/DiscoDurodeRoer/curso-disenio-base-de-datos/tree/master")
    with st.container(border=True):
      st.subheader("TEMA 01: Denormalización")
      st.markdown("""<div class="justificar">
            ⚠️🔨 En Construcción...
            <br><br></div>""", unsafe_allow_html=True)
      st.link_button("Curso en GitHub", url="https://github.com/DiscoDurodeRoer/curso-disenio-base-de-datos/tree/master")

with guia2:
    with st.container(border=True):
     st.subheader("TEMA 02: DER")
     st.markdown("""<div class="justificar">
            ⚠️🔨 En Construcción...
            <br><br></div>""", unsafe_allow_html=True)
     st.link_button("Curso en GitHub", url="https://github.com/DiscoDurodeRoer/curso-disenio-base-de-datos/tree/master")
    with st.container(border=True):
     st.subheader("TEMA 03: SQL")
     st.markdown("""<div class="justificar">
            ⚠️🔨 En Construcción...
            <br><br></div>""", unsafe_allow_html=True)
     st.link_button("Curso en GitHub", url="https://github.com/DiscoDurodeRoer/curso-disenio-base-de-datos/tree/master")

st.divider()

st.header(":red[Guías de Ejercicios:]")
st.markdown("""<div class="justificar">
            ⚠️🔨 En Construcción...
            <br><br></div>""", unsafe_allow_html=True)

eje1, eje2 = st.columns(2)
with eje1:
    with st.container(border=True):
      st.subheader("TEMA 01: Normalización")
      st.markdown("""<div class="justificar">
            ⚠️🔨 En Construcción...
            <br><br></div>""", unsafe_allow_html=True)
      st.link_button("Curso en GitHub", url="https://github.com/DiscoDurodeRoer/curso-disenio-base-de-datos/tree/master")
    with st.container(border=True):
      st.subheader("TEMA 01: Denormalización")
      st.markdown("""<div class="justificar">
            ⚠️🔨 En Construcción...
            <br><br></div>""", unsafe_allow_html=True)
      st.link_button("Curso en GitHub", url="https://github.com/DiscoDurodeRoer/curso-disenio-base-de-datos/tree/master")

with eje2:
    with st.container(border=True):
     st.subheader("TEMA 02: DER")
     st.markdown("""<div class="justificar">
            ⚠️🔨 En Construcción...
            <br><br></div>""", unsafe_allow_html=True)
     st.link_button("Curso en GitHub", url="https://github.com/DiscoDurodeRoer/curso-disenio-base-de-datos/tree/master")
    with st.container(border=True):
     st.subheader("TEMA 03: SQL")
     st.markdown("""<div class="justificar">
            ⚠️🔨 En Construcción...
            <br><br></div>""", unsafe_allow_html=True)
     st.link_button("Curso en GitHub", url="https://github.com/DiscoDurodeRoer/curso-disenio-base-de-datos/tree/master")

utils.cambio_pag(ant="Indice/00_inicio.py", sig="Indice/TEMA 00/00_ConceptosBasicos.py")