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
    </style>
    """, unsafe_allow_html=True)

st.title("Denormalización")

st.header("¿Qué es la denormalización en las bases de datos?")
st.markdown("""<div class="justificar">
                <p>⚠️ En Construcción... </p>
                </div>""", unsafe_allow_html=True)

st.subheader("Por qué y cuándo denormalizar")
st.markdown("""<div class="justificar">
                <p>⚠️ En Construcción... </p>
                </div>""", unsafe_allow_html=True)

ra1, ra2 = st.columns(2)
with ra1:
    with st.container(border=True):
        st.markdown('''<b class="destacar">Razón 1</b><br>
                   ⚠️ En Construcción...
                   ''',  unsafe_allow_html=True)    
    with st.container(border=True):
        st.markdown('''<b class="destacar">Razón 3</b><br>
                   ⚠️ En Construcción...
                   ''',  unsafe_allow_html=True)
with ra2:
    with st.container(border=True):
        st.markdown('''<b class="destacar">Razón 2</b><br>
                   ⚠️ En Construcción...
                   ''',  unsafe_allow_html=True)    
    with st.container(border=True):
        st.markdown('''<b class="destacar">Razón 4</b><br>
                   ⚠️ En Construcción...
                   ''',  unsafe_allow_html=True)

st.subheader("Ventajas y desventajas de la Denormalización")
st.markdown("""<div class="justificar">
                <p>⚠️ En Construcción... </p>
                </div>""", unsafe_allow_html=True)

ven1, des2 = st.columns(2)
with ven1:
    with st.expander("**VENTAJAS**", expanded=True):
                st.markdown("""<div class="justificar">
                        <spam class="destacar">Ventaja 1:</spam>
                        <p>⚠️ En Construcción...  </p>
                        <spam class="destacar">Ventaja 2:</spam>
                        <p>⚠️ En Construcción...  </p>
                        <spam class="destacar">Ventaja 3:</spam>
                        <p>⚠️ En Construcción...  </p>
                        </div>""", unsafe_allow_html=True)
with des2:
    with st.expander("**DESVENTAJAS**", expanded=True):
                st.markdown("""<div class="justificar">
                        <spam class="destacar">Ventaja 1:</spam>
                        <p>⚠️ En Construcción...  </p>
                        <spam class="destacar">Ventaja 2:</spam>
                        <p>⚠️ En Construcción...  </p>
                        <spam class="destacar">Ventaja 3:</spam>
                        <p>⚠️ En Construcción...  </p>
                        </div>""", unsafe_allow_html=True)
                
st.header("4 pasos de Kimball")
st.markdown("""<div class="justificar">
                <p>⚠️ En Construcción... </p>
                </div>""", unsafe_allow_html=True)

pas1, pas2, pas3, pas4 = st.columns(4)
with pas1:
        st.markdown("""<div class="contenedor">
                <h4 class="destacar">Paso 1: Proceso Organizacional</h4>
                <p class="justificar">⚠️ En Construcción... </p>
                </div>""", unsafe_allow_html=True)
with pas2:
        st.markdown("""<div class="contenedor">
                <h4 class="destacar">Paso 2: Declarar Granularidad</h4>
                <p class="justificar">⚠️ En Construcción... </p>
                </div>""", unsafe_allow_html=True)
with pas3:
        st.markdown("""<div class="contenedor">
                <h4 class="destacar">Paso 3: Identificar Dimensiones</h4>
                <p class="justificar">⚠️ En Construcción... </p>
                </div>""", unsafe_allow_html=True)
with pas4:
        st.markdown("""<div class="contenedor">
                <h4 class="destacar">Paso 4: Identificar Hechos</h4>
                <p class="justificar">⚠️ En Construcción... </p>
                </div>""", unsafe_allow_html=True)

st.markdown("""<div class="justificar">
                <p>⚠️ En Construcción... </p>
                </div>""", unsafe_allow_html=True)

st.header("Técnicas de Denormalización")
st.markdown("""<div class="justificar">
                <p>⚠️ En Construcción... </p>
                </div>""", unsafe_allow_html=True)

tec1, tec2, tec3 = st.tabs(["**COLUMNAS**", "**TABLAS**", "**VISTAS**"])
with tec1:
    mo1, mo2 = st.columns(2)
with mo1:
    st.subheader("atributos derivados:")
    st.markdown("""<div class="justificar">
                    <p>⚠️ En Construcción... </p>
                    </div>""", unsafe_allow_html=True)
    with st.expander("**¿Cuando Usar?**"):
        st.markdown("""<div class="justificar">
                                <spam class="destacar">Ventaja 1:</spam>
                                <p>⚠️ En Construcción...  </p>
                                <spam class="destacar">Ventaja 2:</spam>
                                <p>⚠️ En Construcción...  </p>
                                <spam class="destacar">Ventaja 3:</spam>
                                <p>⚠️ En Construcción...  </p>
                                </div>""", unsafe_allow_html=True)  
with mo2:
    st.subheader("duplicación de columnas:")
    st.markdown("""<div class="justificar">
                    <p>⚠️ En Construcción... </p>
                    </div>""", unsafe_allow_html=True)
    with st.expander("**¿Cuando Usar?**"):
        st.markdown("""<div class="justificar">
                                <spam class="destacar">Ventaja 1:</spam>
                                <p>⚠️ En Construcción...  </p>
                                <spam class="destacar">Ventaja 2:</spam>
                                <p>⚠️ En Construcción...  </p>
                                <spam class="destacar">Ventaja 3:</spam>
                                <p>⚠️ En Construcción...  </p>
                                </div>""", unsafe_allow_html=True)   
with tec2:
    mo3, mo4 = st.columns(2)
with mo3:
    st.subheader("tablas preunidas:")
    st.markdown("""<div class="justificar">
                    <p>⚠️ En Construcción... </p>
                    </div>""", unsafe_allow_html=True)
    with st.expander("**¿Cuando Usar?**"):
        st.markdown("""<div class="justificar">
                                <spam class="destacar">Ventaja 1:</spam>
                                <p>⚠️ En Construcción...  </p>
                                <spam class="destacar">Ventaja 2:</spam>
                                <p>⚠️ En Construcción...  </p>
                                <spam class="destacar">Ventaja 3:</spam>
                                <p>⚠️ En Construcción...  </p>
                                </div>""", unsafe_allow_html=True)  
with mo4:
    st.subheader("tablas de resumen:")
    st.markdown("""<div class="justificar">
                    <p>⚠️ En Construcción... </p>
                    </div>""", unsafe_allow_html=True)
    with st.expander("**¿Cuando Usar?**"):
        st.markdown("""<div class="justificar">
                                <spam class="destacar">Ventaja 1:</spam>
                                <p>⚠️ En Construcción...  </p>
                                <spam class="destacar">Ventaja 2:</spam>
                                <p>⚠️ En Construcción...  </p>
                                <spam class="destacar">Ventaja 3:</spam>
                                <p>⚠️ En Construcción...  </p>
                                </div>""", unsafe_allow_html=True) 
with tec3:
    st.subheader("vistas materializadas:")
    st.markdown("""<div class="justificar">
                    <p>⚠️ En Construcción... </p>
                    </div>""", unsafe_allow_html=True)
    with st.expander("**¿Cuando Usar?**"):
        st.markdown("""<div class="justificar">
                                <spam class="destacar">Ventaja 1:</spam>
                                <p>⚠️ En Construcción...  </p>
                                <spam class="destacar">Ventaja 2:</spam>
                                <p>⚠️ En Construcción...  </p>
                                <spam class="destacar">Ventaja 3:</spam>
                                <p>⚠️ En Construcción...  </p>
                                </div>""", unsafe_allow_html=True) 

utils.cambio_pag(ant="Indice/TEMA 01/01_Arquitectura.py", sig="Indice/TEMA 02/00_DER.py")