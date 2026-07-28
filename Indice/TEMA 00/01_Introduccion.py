import streamlit as st
import utils

st.title("🎯 Introducción a las Bases de Datos")

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
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

st.header("¿Qué son las Bases de Datos?")
st.markdown("""<div class="justificar">
                    <p>⚠️ En construcción... </p>
                    </div>""", unsafe_allow_html=True)

def1, def2 = st.columns(2)
with def1:
    with st.container(border=True):
       st.markdown('''<div class="justificar">
                <h4 class="destacar"> 📌 Analíticamente... </h4>
                <p>⚠️ En construcción...</p>
                </div>''',  unsafe_allow_html=True)
with def2:
    with st.container(border=True):
        st.markdown('''<div class="justificar">
                <h4 class="destacar"> 📌 Conceptualmente... </h4>
                <p>⚠️ En construcción...</p>
                </div>''',  unsafe_allow_html=True)

st.header("¿Qué es un Sistema de Bases de Datos?")
st.markdown("""<div class="justificar">
                    <p>⚠️ En construcción... </p>
                    </div>""", unsafe_allow_html=True)

with st.expander(" 📍 **¿Por Qué Un Sistema de Bases de Datos?**"):
    sis1, sis2 = st.columns(2)
    with sis1:
       with st.container(border=True):
         st.markdown('''<b class="destacar">Espacio Físico</b><br>
                   ⚠️ En construcción...
                   ''',  unsafe_allow_html=True)
       with st.container(border=True):
                st.markdown('''<b class="destacar">Seguridad</b><br>
                          ⚠️ En construcción...
                          ''',  unsafe_allow_html=True)
    with sis2:
       with st.container(border=True):
         st.markdown('''<b class="destacar">Velocidad</b><br>
                   ⚠️ En construcción...
                   ''',  unsafe_allow_html=True)
       with st.container(border=True):
                st.markdown('''<b class="destacar">Capacidad</b><br>
                          ⚠️ En construcción...
                          ''',  unsafe_allow_html=True)


st.header("Tipos de Bases de Datos")
st.markdown("""<div class="justificar">
                    <p>⚠️ En construcción... </p>
                    </div>""", unsafe_allow_html=True)

bd1, bd2 = st.columns(2)
with bd1:
    with st.expander("🎯 :red[**Bases de Datos Relacionales**] 💫", expanded=True):
        st.markdown("""<div class="justificar">
                    <p>⚠️ En construcción... </p>
                    </div>""", unsafe_allow_html=True)
with bd2:
    with st.expander("🎯 :red[**Bases de Datos No Relacionales**] ✨", expanded=True):
        st.markdown("""<div class="justificar">
                    <p>⚠️ En construcción... </p>
                    </div>""", unsafe_allow_html=True)

st.header("Bases de Datos Relacionales")
st.markdown("""<div class="justificar">
                    <p>⚠️ En construcción... </p>
                    </div>""", unsafe_allow_html=True)

st.subheader("Elementos de una Base de Datos")

ele1, ele2 = st.columns(2)
with ele1:
       with st.container(border=True):
         st.markdown('''<b class="destacar">Filas</b><br>
                   ⚠️ En construcción...
                   ''',  unsafe_allow_html=True)
       with st.container(border=True):
                st.markdown('''<b class="destacar">Claves Primarias (PK)</b><br>
                          ⚠️ En construcción...
                          ''',  unsafe_allow_html=True)
with ele2:
       with st.container(border=True):
         st.markdown('''<b class="destacar">Columnas</b><br>
                   ⚠️ En construcción...
                   ''',  unsafe_allow_html=True)
       with st.container(border=True):
                st.markdown('''<b class="destacar">Claves Foraneas (FK)</b><br>
                          ⚠️ En construcción...
                          ''',  unsafe_allow_html=True)

st.subheader("Principales Operaciones en Una Base de Datos")
st.markdown("""<div class="justificar">
                    <p>⚠️ En construcción... </p>
                    </div>""", unsafe_allow_html=True)

op1, op2, op3 = st.columns(3)
with op1:
    st.markdown("""<div class="contenedor">
                    <b class="destacar"> Agregar Archivos </b><br>
                    ⚠️ En construcción... 
                    </div>""", unsafe_allow_html=True)
    st.markdown("""<div class="contenedor">
                        <b class="destacar"> Insertar Datos </b><br>
                        ⚠️ En construcción... 
                        </div>""", unsafe_allow_html=True)
with op2:
    st.markdown("""<div class="contenedor">
                    <b class="destacar"> Repuperar Datos </b><br>
                    ⚠️ En construcción... 
                    </div>""", unsafe_allow_html=True)
    st.markdown("""<div class="contenedor">
                        <b class="destacar"> Modificar Datos </b><br>
                        ⚠️ En construcción... 
                        </div>""", unsafe_allow_html=True)
with op3:
    st.markdown("""<div class="contenedor">
                    <b class="destacar"> Eliminar Datos </b><br>
                    ⚠️ En construcción... 
                    </div>""", unsafe_allow_html=True)
    st.markdown("""<div class="contenedor">
                        <b class="destacar"> Eliminar Archivos </b><br>
                        ⚠️ En construcción... 
                        </div>""", unsafe_allow_html=True)
    
st.header("Claves Primarias y Foraneas:")
st.markdown("""<div class="justificar">
                    <p>⚠️ En construcción... </p>
                    </div>""", unsafe_allow_html=True)

pk, fk = st.columns(2)
with pk:
    with st.expander(":red[**Reglas de las Claves Primarias**]"):
        st.markdown("""<div class="justificar">
                    <spam class="destacar"> Regla #1:</spam>
                    <p>⚠️ En construcción...  </p>
                    <spam class="destacar"> Regla #2:</spam>
                    <p>⚠️ En construcción...  </p>
                    <spam class="destacar"> Regla #3:</spam>
                    <p>⚠️ En construcción...  </p>
                    <spam class="destacar"> Regla #4:</spam>
                    <p>⚠️ En construcción...  </p>
                    <spam class="destacar"> Regla #5:</spam>
                    <p>⚠️ En construcción...  </p>
                    </div>""", unsafe_allow_html=True)
with fk:
    with st.expander(":red[**Reglas de las Llaves Foraneas**]"):
        st.markdown("""<div class="justificar">
                            <spam class="destacar"> Regla #1: </spam>
                            <p>⚠️ En construcción...  </p>
                            <spam class="destacar"> Regla #2: </spam>
                            <p>⚠️ En construcción...  </p>
                            <spam class="destacar"> Regla #3: </spam>
                            <p>⚠️ En construcción...  </p>
                            <spam class="destacar"> Regla #4: </spam>
                            <p>⚠️ En construcción...  </p>
                            <spam class="destacar"> Regla #5: </spam>
                            <p>⚠️ En construcción...  </p>
                            </div>""", unsafe_allow_html=True)

st.subheader("Tipos de Claves Primarias")
st.markdown("""<div class="justificar">
                    <p>⚠️ En construcción... </p>
                    </div>""", unsafe_allow_html=True)

tip1, tip2 = st.columns(2)
with tip1:
    st.markdown("""<div class="contenedor">
                        <b class="destacar"> PKs Simples </b><br>
                        ⚠️ En construcción... 
                        </div>""", unsafe_allow_html=True)
with tip2:
    st.markdown("""<div class="contenedor">
                        <b class="destacar"> PKs Compuestas </b><br>
                        ⚠️ En construcción... 
                        </div>""", unsafe_allow_html=True)

utils.cambio_pag(ant="Indice/TEMA 00/00_ConceptosBasicos.py", sig="Indice/TEMA 00/02_TiposdeDatos.py")