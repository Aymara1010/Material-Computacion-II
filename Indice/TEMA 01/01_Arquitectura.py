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

st.title("Arquitecturas y Modelado en las BBDD")

st.header("Introducción a los Data Wherehouse y Sus Componentes")
st.markdown("""<div class="justificar">
                    <p>⚠️ En Construcción... </p>
                    </div>""", unsafe_allow_html=True)
with st.expander("**IMPORTANTE**"):
    st.markdown("""<div class="justificar">
                    <p>⚠️ En Construcción... </p>
                    </div>""", unsafe_allow_html=True)

st.subheader("Componentes de una arquitectura de almacén de datos")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""<div class="contenedor-lista">
                    <b class="destacar">1. Fuentes de Datos</b><br>
                    ⚠️ En Construcción...
                    </div>""", unsafe_allow_html=True)
    st.markdown("""<div class="contenedor-lista">
                    <b class="destacar">4. Almacenamiento de Datos</b><br>
                    ⚠️ En Construcción...
                    </div>""", unsafe_allow_html=True)
with col2:
    st.markdown("""<div class="contenedor-lista">
                    <b class="destacar">2. ETL</b><br>
                    ⚠️ En Construcción...
                    </div>""", unsafe_allow_html=True)
    st.markdown("""<div class="contenedor-lista">
                    <b class="destacar">5. Metadatos</b><br>
                    ⚠️ En Construcción...
                    </div>""", unsafe_allow_html=True)
with col3:
    st.markdown("""<div class="contenedor-lista">
                    <b class="destacar">3. Área de Preparación</b><br>
                    ⚠️ En Construcción...
                    </div>""", unsafe_allow_html=True)
    st.markdown("""<div class="contenedor-lista">
                    <b class="destacar">6. Acceso y Análisis de Datos</b><br>
                    ⚠️ En Construcción...
                    </div>""", unsafe_allow_html=True)

st.header("Arquitecturas de Inmon y Kimball")
st.markdown("""<div class="justificar">
                    <p>⚠️ En Construcción... </p>
                    </div>""", unsafe_allow_html=True)

arq1, arq2 = st.columns(2)
with arq1:
    st.subheader("Arquitectura de Inmon")
    with st.container(border=True):
         st.markdown('''<b class="destacar">ENFOQUE</b><br>
                   ⚠️ En Construcción...
                   ''',  unsafe_allow_html=True)
    st.subheader("Ventajas / Desventajas",text_alignment="center")
    Inmon1, Inmon2 = st.columns(2, border=True)
    with Inmon1:
        st.markdown("""<div class="justificar">
                        <spam class="destacar">Ventaja 1:</spam>
                        <p>⚠️ En Construcción...  </p>
                        <spam class="destacar">Ventaja 2:</spam>
                        <p>⚠️ En Construcción...  </p>
                        <spam class="destacar">Ventaja 3:</spam>
                        <p>⚠️ En Construcción...  </p>
                        </div>""", unsafe_allow_html=True)
    with Inmon2:
            st.markdown("""<div class="justificar">
                        <spam class="destacar">Ventaja 1:</spam>
                        <p>⚠️ En Construcción...  </p>
                        <spam class="destacar">Ventaja 2:</spam>
                        <p>⚠️ En Construcción...  </p>
                        <spam class="destacar">Ventaja 3:</spam>
                        <p>⚠️ En Construcción...  </p>
                        </div>""", unsafe_allow_html=True)
    with st.expander("**¿Cuando Usar?**"):
        st.markdown("""<div class="justificar">
                    <p>⚠️ En Construcción... </p>
                    </div>""", unsafe_allow_html=True)
        
with arq2:
    st.subheader("Arquitectura de Kimball")
    with st.container(border=True):
         st.markdown('''<b class="destacar">ENFOQUE</b><br>
                   ⚠️ En Construcción...
                   ''',  unsafe_allow_html=True)
    st.subheader("Ventajas / Desventajas",text_alignment="center")
    kim1, kim2 = st.columns(2, border=True)
    with kim1:
        st.markdown("""<div class="justificar">
                        <spam class="destacar">Ventaja 1:</spam>
                        <p>⚠️ En Construcción...  </p>
                        <spam class="destacar">Ventaja 2:</spam>
                        <p>⚠️ En Construcción...  </p>
                        <spam class="destacar">Ventaja 3:</spam>
                        <p>⚠️ En Construcción...  </p>
                        </div>""", unsafe_allow_html=True)
    with kim2:
            st.markdown("""<div class="justificar">
                        <spam class="destacar">Ventaja 1:</spam>
                        <p>⚠️ En Construcción...  </p>
                        <spam class="destacar">Ventaja 2:</spam>
                        <p>⚠️ En Construcción...  </p>
                        <spam class="destacar">Ventaja 3:</spam>
                        <p>⚠️ En Construcción...  </p>
                        </div>""", unsafe_allow_html=True)
    with st.expander("**¿Cuando Usar?**"):
        st.markdown("""<div class="justificar">
                    <p>⚠️ En Construcción... </p>
                    </div>""", unsafe_allow_html=True)

st.header("Modelado Dimensional de Kimball")
st.markdown("""<div class="justificar">
                    <p>⚠️ En Construcción... </p>
                    </div>""", unsafe_allow_html=True)

mo1, mo2 = st.columns(2)
with mo1:
    st.subheader("Tabla de Dimensiones")
    st.markdown("""<div class="justificar">
                    <p>⚠️ En Construcción... </p>
                    </div>""", unsafe_allow_html=True)
    with st.expander("**Características**"):
        st.markdown("""<div class="justificar">
                                <spam class="destacar">Ventaja 1:</spam>
                                <p>⚠️ En Construcción...  </p>
                                <spam class="destacar">Ventaja 2:</spam>
                                <p>⚠️ En Construcción...  </p>
                                <spam class="destacar">Ventaja 3:</spam>
                                <p>⚠️ En Construcción...  </p>
                                </div>""", unsafe_allow_html=True)  
with mo2:
    st.subheader("Tabla de Hechos")
    st.markdown("""<div class="justificar">
                    <p>⚠️ En Construcción... </p>
                    </div>""", unsafe_allow_html=True)
    with st.expander("**Características**"):
        st.markdown("""<div class="justificar">
                                <spam class="destacar">Ventaja 1:</spam>
                                <p>⚠️ En Construcción...  </p>
                                <spam class="destacar">Ventaja 2:</spam>
                                <p>⚠️ En Construcción...  </p>
                                <spam class="destacar">Ventaja 3:</spam>
                                <p>⚠️ En Construcción...  </p>
                                </div>""", unsafe_allow_html=True)   

st.subheader("Ventajas del modelo dimensional")

ven1, ven2, ven3 = st.columns(3)
with ven1:
    st.markdown("""<div class="contenedor-lista">
                    <b class="destacar">Ventaja</b><br>
                    ⚠️ En Construcción...
                    </div>""", unsafe_allow_html=True)
with ven2:
    st.markdown("""<div class="contenedor-lista">
                    <b class="destacar">Ventaja</b><br>
                    ⚠️ En Construcción...
                    </div>""", unsafe_allow_html=True)
with ven3:
    st.markdown("""<div class="contenedor-lista">
                    <b class="destacar">Ventaja</b><br>
                    ⚠️ En Construcción...
                    </div>""", unsafe_allow_html=True)

st.subheader("Esquemas del Modelo Dimensional")
st.markdown("""<div class="justificar">
                    <p>⚠️ En Construcción... </p>
                    </div>""", unsafe_allow_html=True)

mod1, mod2 = st.columns(2)
with mod1:
    st.subheader("**Esquema Estrella**")
    st.markdown("""<div class="justificar">
                    <p>⚠️ En Construcción... </p>
                    </div>""", unsafe_allow_html=True)
    with st.expander("**Características**"):
                    st.markdown("""<div class="justificar">
                                <spam class="destacar">Ventaja 1:</spam>
                                <p>⚠️ En Construcción...  </p>
                                <spam class="destacar">Ventaja 2:</spam>
                                <p>⚠️ En Construcción...  </p>
                                <spam class="destacar">Ventaja 3:</spam>
                                <p>⚠️ En Construcción...  </p>
                                </div>""", unsafe_allow_html=True)  
    with st.expander("**Ventajas**"):
                    st.markdown("""<div class="justificar">
                                <spam class="destacar">Ventaja 1:</spam>
                                <p>⚠️ En Construcción...  </p>
                                <spam class="destacar">Ventaja 2:</spam>
                                <p>⚠️ En Construcción...  </p>
                                <spam class="destacar">Ventaja 3:</spam>
                                <p>⚠️ En Construcción...  </p>
                                </div>""", unsafe_allow_html=True)  
    with st.expander("**Cuando Usar**"):
                    st.markdown("""<div class="justificar">
                            <p>⚠️ En Construcción... </p>
                            </div>""", unsafe_allow_html=True)
with mod2:
    st.subheader("**Esquema Copo de Nieve**")
    st.markdown("""<div class="justificar">
                            <p>⚠️ En Construcción... </p>
                            </div>""", unsafe_allow_html=True)
    with st.expander("**Características**"):
                    st.markdown("""<div class="justificar">
                                <spam class="destacar">Ventaja 1:</spam>
                                <p>⚠️ En Construcción...  </p>
                                <spam class="destacar">Ventaja 2:</spam>
                                <p>⚠️ En Construcción...  </p>
                                <spam class="destacar">Ventaja 3:</spam>
                                <p>⚠️ En Construcción...  </p>
                                </div>""", unsafe_allow_html=True)  
    with st.expander("**Ventajas**"):
                    st.markdown("""<div class="justificar">
                                <spam class="destacar">Ventaja 1:</spam>
                                <p>⚠️ En Construcción...  </p>
                                <spam class="destacar">Ventaja 2:</spam>
                                <p>⚠️ En Construcción...  </p>
                                <spam class="destacar">Ventaja 3:</spam>
                                <p>⚠️ En Construcción...  </p>
                                </div>""", unsafe_allow_html=True)  
    with st.expander("**Cuando Usar**"):
                    st.markdown("""<div class="justificar">
                            <p>⚠️ En Construcción... </p>
                            </div>""", unsafe_allow_html=True)


utils.cambio_pag(ant="Indice/TEMA 01/00_Normalizacion.py", sig="Indice/TEMA 01/02_Denormalizacion.py")