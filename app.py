import streamlit as st

st.set_page_config(page_title="Computación II", page_icon="💻", layout="wide")

pg_00 = st.Page("capitulos/00_inicio.py", title="Inicio")
pg_01 = st.Page("capitulos/01_Introduccion.py", title="Introducción")
pg_02 = st.Page("capitulos/02_Normalizacion.py", title="Normalizacion")
pg_03 = st.Page("capitulos/03_Denormalizacion.py", title="Denormalización")
pg_04 = st.Page("capitulos/04_DER.py", title="Introducción a DER")
pg_05 = st.Page("capitulos/05_SQL.py", title="Introducción a SQL")

pg = st.navigation({
    "**General**": [pg_00, pg_01],
    "**Tema 01: Normalización y Denormalización**": [pg_02, pg_03],
    "**Tema 02: Diagrama Entidad Relación**": [pg_04],
    "**Tema 03: SQL**": [pg_05]
})

pg.run()