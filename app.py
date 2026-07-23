import streamlit as st

st.set_page_config(page_title="Computación II", page_icon="⌨️", layout="wide")

pg_00 = st.Page("Indice/GENERAL/00_inicio.py", title="Inicio")
pg_01 = st.Page("Indice/GENERAL/01_Introduccion.py", title="Introducción a las BBDD")

pg_02 = st.Page("Indice/TEMA 01/00_Normalizacion.py", title="Normalizacion")
pg_03 = st.Page("Indice/TEMA 01/01_Denormalizacion.py", title="Denormalización")
pg_04 = st.Page("Indice/TEMA 01/02_EjerciciosTema1.py", title="Ejecicios Resueltos")

pg_05 = st.Page("Indice/TEMA 02/00_DER.py", title="Introducción a DER")
pg_06 = st.Page("Indice/TEMA 02/01_NotacionDER.py", title="Notación de DER")
pg_07 = st.Page("Indice/TEMA 02/02_EjerciciosTema2.py", title="Ejercicios Resueltos")

pg_08 = st.Page("Indice/TEMA 03/00_SQL.py", title="Introducción a SQL")

pg = st.navigation({
    "**🏠 HOME**": [pg_00, pg_01],
    "**📕 TEMA 01 : Normalización en BBDD**": [pg_02, pg_03, pg_04],
    "**📗 TEMA 02 : Diagrama Entidad Relación**": [pg_05, pg_06, pg_07],
    "**📘 TEMA 03 : SQL**": [pg_08]
})

with st.sidebar:
    st.markdown("# Apuntes - Computación II✨")
    st.markdown("Material de estudio hecho para la materia Computación II de la Escuela de Estadística y Ciencias Actuariales 🎲")
    st.caption("Creado por: ✨🎲 Aymara Andersen 🎲✨")
  
pg.run()