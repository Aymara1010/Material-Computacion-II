import streamlit as st
import utils

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

st.title("Normalización")

st.header("¿Qué es la Normalización?")
st.markdown("""<div class="justificar">
                    <p>⚠️ En Construcción... </p>
                    </div>""", unsafe_allow_html=True)

st.subheader("¿Por Qué Normalizar?")
nor1, nor2 = st.columns(2)
with nor1:
    st.markdown("""<div class="contenedor-lista">
                <b class="destacar">Redundancia</b><br>
                ⚠️ En Construcción...
                </div>""", unsafe_allow_html=True)
    st.markdown("""<div class="contenedor-lista">
                <b class="destacar">Integridad</b><br>
                ⚠️ En Construcción...
                </div>""", unsafe_allow_html=True)
with nor2: 
    st.markdown("""<div class="contenedor-lista">
                <b class="destacar">Rendimiento y escalabilidad </b><br>
                ⚠️ En Construcción...
                </div>""", unsafe_allow_html=True)
    st.markdown("""<div class="contenedor-lista">
                <b class="destacar">Seguridad</b><br>
                ⚠️ En Construcción...
                </div>""", unsafe_allow_html=True)
    
st.subheader("Ventajas y desventajas de la normalización")
st.markdown("""<div class="justificar">
                    <p>⚠️ En Construcción... </p>
                    </div>""", unsafe_allow_html=True)

ven1, des2 = st.columns(2)
with ven1:
    with st.expander("Ventajas",expanded=True):
            st.markdown("""<div class="justificar">
                        <spam class="destacar">Ventaja 1:</spam>
                        <p>⚠️ En Construcción...  </p>
                        <spam class="destacar">Ventaja 2:</spam>
                        <p>⚠️ En Construcción...  </p>
                        <spam class="destacar">Ventaja 3:</spam>
                        <p>⚠️ En Construcción...  </p>
                        </div>""", unsafe_allow_html=True)
with des2:
    with st.expander("Desventajas",expanded=True):
            st.markdown("""<div class="justificar">
                        <spam class="destacar">Ventaja 1:</spam>
                        <p>⚠️ En Construcción...  </p>
                        <spam class="destacar">Ventaja 2:</spam>
                        <p>⚠️ En Construcción...  </p>
                        <spam class="destacar">Ventaja 3:</spam>
                        <p>⚠️ En Construcción...  </p>
                        </div>""", unsafe_allow_html=True)

st.header("Formas Normales")
st.markdown("""<div class="justificar">
                <p>⚠️ En Construcción... </p>
                </div>""", unsafe_allow_html=True)

fn1, fn2, fn3 = st.columns(3)
with fn1:
    st.markdown("""<div class="contenedor">
                <h4 class="destacar"> Primera Forma Normal</h4>
                <p class="justificar">⚠️ En Construcción...</p>
                </div>""", unsafe_allow_html=True)
with fn2:
    st.markdown("""<div class="contenedor">
                <h4 class="destacar"> Segunda Forma Normal</h4>
                <p class="justificar">⚠️ En Construcción...</p>
                </div>""", unsafe_allow_html=True)
with fn3:
    st.markdown("""<div class="contenedor">
                <h4 class="destacar"> Tercera Forma Normal</h4>
                <p class="justificar">⚠️ En Construcción...</p>
                </div>""", unsafe_allow_html=True)

st.header("Conceptos Clave Para la Normalización")
st.markdown("""<div class="justificar">
                <p>⚠️ En Construcción... </p>
                </div>""", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["CLAVES", "DEPENDENCIAS", "RELACIONES"])

with tab1:
    st.subheader("Claves")
    st.markdown("""<div class="justificar">
                <p>⚠️ En Construcción... </p>
                </div>""", unsafe_allow_html=True)
    clav1, clav2 = st.columns(2)
    with clav1:
       with st.container(border=True):
         st.markdown('''<b class="destacar">SIMPLE</b><br>
                   ⚠️ En Construcción...
                   ''',  unsafe_allow_html=True)
    with clav2:
       with st.container(border=True):
         st.markdown('''<b class="destacar">COMPUESTA</b><br>
                   ⚠️ En Construcción...
                   ''',  unsafe_allow_html=True)
with tab2:
   st.subheader("Dependencias")
   st.markdown("""<div class="justificar">
                <p>⚠️ En Construcción... </p>
                </div>""", unsafe_allow_html=True)
   dep1, dep2 = st.columns(2)
   with dep1:
      with st.container(border=True):
         st.markdown('''<b class="destacar">FUNCIONAL</b><br>
                   ⚠️ En Construcción...
                   ''',  unsafe_allow_html=True)
   with dep2:
      with st.container(border=True):
         st.markdown('''<b class="destacar">TRANSITIVA</b><br>
                   ⚠️ En Construcción...
                   ''',  unsafe_allow_html=True)
with tab3:
   st.subheader("Relaciones")
   st.markdown("""<div class="justificar">
                <p>⚠️ En Construcción... </p>
                </div>""", unsafe_allow_html=True)
   re1, re2, re3 = st.columns(3)
   with re1:
      with st.container(border=True):
         st.markdown('''<b class="destacar">UNO A UNO</b><br>
                   ⚠️ En Construcción...
                   ''',  unsafe_allow_html=True)
   with re2:
      with st.container(border=True):
         st.markdown('''<b class="destacar">UNO A MUCHOS</b><br>
                   ⚠️ En Construcción...
                   ''',  unsafe_allow_html=True)
   with re3:
      with st.container(border=True):
         st.markdown('''<b class="destacar">MUCHOS A MUCHOS</b><br>
                   ⚠️ En Construcción...
                   ''',  unsafe_allow_html=True)

st.header("¿Por Qué es Importante la Normalización?")
st.markdown("""<div class="justificar">
                <p>⚠️ En Construcción... </p>
                </div>""", unsafe_allow_html=True)


st.subheader("¿Qué anomalías de datos corrige la normalización?")
st.markdown("""<div class="justificar">
                <p>⚠️ En Construcción... </p>
                </div>""", unsafe_allow_html=True)

with st.expander("Inserción"):
                st.markdown("""<div class="justificar">
                <p>⚠️ En Construcción... </p>
                </div>""", unsafe_allow_html=True)

with st.expander("Eliminación"):
                st.markdown("""<div class="justificar">
                <p>⚠️ En Construcción... </p>
                </div>""", unsafe_allow_html=True)

with st.expander("Actualización"):
                st.markdown("""<div class="justificar">
                <p>⚠️ En Construcción... </p>
                </div>""", unsafe_allow_html=True)                   

utils.cambio_pag(ant="Indice/TEMA 00/02_TiposdeDatos.py", sig="Indice/TEMA 01/01_Arquitectura.py")