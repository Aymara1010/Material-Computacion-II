import streamlit as st

st.set_page_config(page_title="Computación II", page_icon="⌨️", layout="wide", initial_sidebar_state="collapsed")

pg_00 = st.Page("Indice/00_inicio.py", title="Inicio")

pg_01 = st.Page("Indice/TEMA 00/00_ConceptosBasicos.py", title="Conceptos Básicos")
pg_02 = st.Page("Indice/TEMA 00/01_Introduccion.py", title="Bases de Datos")
pg_03 = st.Page("Indice/TEMA 00/02_TiposdeDatos.py", title="Tipos de Datos")

pg_04 = st.Page("Indice/TEMA 01/00_Normalizacion.py", title="Normalizacion")
pg_05 = st.Page("Indice/TEMA 01/01_Arquitectura.py", title="Arquitectura y Modelado")
pg_06 = st.Page("Indice/TEMA 01/02_Denormalizacion.py", title="Denormalización")

pg_07 = st.Page("Indice/TEMA 02/00_DER.py", title="Introducción a DER")
pg_08 = st.Page("Indice/TEMA 02/01_NotacionDER.py", title="Notación de DER")
pg_09 = st.Page("Indice/TEMA 02/02_EjerciciosTema2.py", title="Ejercicios Resueltos")

pg_10 = st.Page("Indice/TEMA 03/00_SQL.py", title="Introducción a SQL")

pg = st.navigation({
    "**🏠 HOME**": [pg_00],
    "**📙 TEMA 00: Introducción a las BBDD**": [pg_01, pg_02, pg_03],
    "**📕 TEMA 01 : Normalización en BBDD**": [pg_04, pg_05, pg_06],
    "**📗 TEMA 02 : Diagrama Entidad Relación**": [pg_07, pg_08, pg_09],
    "**📘 TEMA 03 : SQL**": [pg_10]
})

with st.sidebar:
    st.markdown("# Apuntes - Computación II✨")
    st.markdown("Este proyecto fue hecho usando 🎲 Python y Streamlit 🎲, puedes acceder al repositorio de la app en Github [aquí](https://github.com/Aymara1010/Material-Computacion-II)")
    st.caption("Creado por: ✨🎲 Aymara Andersen 🎲✨")
  
pg.run()