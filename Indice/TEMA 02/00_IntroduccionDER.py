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

st.title("Introducción a DER")

st.header("¿Qué son los Diagramas de Entidad Relación?")
st.markdown("""<div class="justificar">
            ⚠️🔨 En Construcción...
            </div>""", unsafe_allow_html=True)

st.subheader("Importancia de DER:")
st.markdown("""<div class="justificar">
            ⚠️🔨 En Construcción...<br><br>
            <b class="destacar">Titulo:</b> ⚠️🔨 En Construcción...<br>
            <b class="destacar">Titulo:</b> ⚠️🔨 En Construcción...<br>
            <b class="destacar">Titulo:</b> ⚠️🔨 En Construcción...<br>
            <b class="destacar">Titulo:</b> ⚠️🔨 En Construcción...
            </div>""", unsafe_allow_html=True)
 
st.header("Componentes de DER")
st.markdown("""<div class="justificar">
            ⚠️🔨 En Construcción...
            <br><br></div>""", unsafe_allow_html=True)
co1, co2, co3, co4 = st.columns(4)
with co1:
    st.markdown("""<div class="contenedor">
                <h4 class="destacar">Entidad:</h4>
                <p>⚠️🔨 En Construcción...</p>
                </div>""", unsafe_allow_html=True)
with co2:    
    st.markdown("""<div class="contenedor">
                    <h4 class="destacar">Atributos:</h4>
                    <p>⚠️🔨 En Construcción...</p>
                    </div>""", unsafe_allow_html=True)    
with co3:
    st.markdown("""<div class="contenedor">
                    <h4 class="destacar">Interrelaciones:</h4>
                    <p>⚠️🔨 En Construcción...</p>
                    </div>""", unsafe_allow_html=True)
with co4:    
    st.markdown("""<div class="contenedor">
                    <h4 class="destacar">Jerarquías:</h4>
                    <p>⚠️🔨 En Construcción...</p>
                    </div>""", unsafe_allow_html=True)
st.write(" ")
with st.expander("**Leyenda**"):
    st.markdown("")

st.header("Entidades y Atributos")
st.markdown("""<div class="justificar">
            ⚠️🔨 En Construcción...
            </div>""", unsafe_allow_html=True)

st.subheader("Entidades:")
st.markdown("""<div class="justificar">
            ⚠️🔨 En Construcción...
            </div>""", unsafe_allow_html=True)
ent1, ent2 = st.columns(2)
with ent1:
    st.subheader("Entidades Fuertes")
    st.markdown("""<div class="justificar">
            ⚠️🔨 En Construcción...
            <br><br></div>""", unsafe_allow_html=True)
    with st.expander("**Forma**"):
      st.markdown("")      
with ent2:
    st.subheader("Entidades Débiles")
    st.markdown("""<div class="justificar">
            ⚠️🔨 En Construcción...
            <br><br></div>""", unsafe_allow_html=True)
    with st.expander("**Forma**"):
          st.markdown("") 

st.subheader("Atributos:")
st.markdown("""<div class="justificar">
            ⚠️🔨 En Construcción...
            <br><br></div>""", unsafe_allow_html=True)
atri1, atri2, atri3 = st.columns(3)
with atri1:
    with st.container(border=True):
      st.markdown("""<div class="justificar">
                <h4>Simples</h4>
                ⚠️🔨 En Construcción...
                <h5 class="destacar">Por Ejemplo:</h5>
                ⚠️🔨 En Construcción...
               </p></div>""", unsafe_allow_html=True) 
    with st.expander("**Forma**"):
      st.markdown("")      
with atri2:
    with st.container(border=True):
          st.markdown("""<div class="justificar">
                    <h4>Identificatorios</h4>
                    ⚠️🔨 En Construcción...
                    <h5 class="destacar">Por Ejemplo:</h5>
                    ⚠️🔨 En Construcción...
                   </p></div>""", unsafe_allow_html=True)
    with st.expander("**Forma**"):
          st.markdown("") 
with atri3:
    with st.container(border=True):
          st.markdown("""<div class="justificar">
                    <h4>Compuestos</h4>
                    ⚠️🔨 En Construcción...
                    <h5 class="destacar">Por Ejemplo:</h5>
                    ⚠️🔨 En Construcción...
                   </p></div>""", unsafe_allow_html=True)
    with st.expander("**Forma**"):
          st.markdown("") 
          
st.header("Tipos de Interrelaciones")
st.markdown("""<div class="justificar">
            ⚠️🔨 En Construcción...
            </div>""", unsafe_allow_html=True)

int1, int2 = st.columns(2)
with int1:
    st.subheader("Interrelación Común:")
    st.markdown("""<div class="justificar">
                    <p>⚠️🔨 En Construcción...<br>
                    <h5 class="destacar">Por Ejemplo:</h5>
                    ⚠️🔨 En Construcción....</p>
                    </div>""", unsafe_allow_html=True)
    with st.expander("**Forma**"):
              st.markdown("")
with int2:
    st.subheader("Interrelación Identificatoria:")
    st.markdown("""<div class="justificar">
                    <p>⚠️🔨 En Construcción...<br>
                    <h5 class="destacar">Por Ejemplo:</h5>
                    ⚠️🔨 En Construcción....</p>
                    </div>""", unsafe_allow_html=True)
    with st.expander("**Forma**"):
              st.markdown("")
              
st.subheader("Según el Grado de la Interrelación:")
gra1, gra2, gra3 = st.columns(3)
with gra1:
    st.markdown("""<div class="contenedor-lista">
                    <h4 class="destacar">Unaria:</h4>
                    <p>⚠️🔨 En Construcción...</p>
                    </div>""", unsafe_allow_html=True)
    st.write(" ")
    with st.expander("**Forma**"):
                  st.markdown("")
with gra2:
    st.markdown("""<div class="contenedor-lista">
                    <h4 class="destacar">Binaria:</h4>
                    <p>⚠️🔨 En Construcción...</p>
                    </div>""", unsafe_allow_html=True)
    st.write(" ")
    with st.expander("**Forma**"):
                  st.markdown("")
with gra3:
    st.markdown("""<div class="contenedor-lista">
                    <h4 class="destacar">Ternaria:</h4>
                    <p>⚠️🔨 En Construcción...</p>
                    </div>""", unsafe_allow_html=True)
    st.write(" ")
    with st.expander("**Forma**"):
                  st.markdown("")

utils.cambio_pag(ant="Indice/TEMA 01/02_Denormalizacion.py", sig="Indice/TEMA 02/01_NotacionDER.py")