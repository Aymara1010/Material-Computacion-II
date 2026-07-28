import streamlit as st
import utils

st.title("💫 Tipos de Datos")

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

st.header("Estructuración de los Datos")
st.markdown("""<div class="justificar">
                    <p>⚠️ En construcción... </p>
                    </div>""", unsafe_allow_html=True)

est1, est2, est3 = st.columns(3)
with est1:
        st.markdown("""<div class="contenedor">
                    <h4 class="destacar"> 💫 Datos Estructurados</h4>
                    <p class="justificar">⚠️ En construcción...</p>
                    </div>""", unsafe_allow_html=True)
with est2:
        st.markdown("""<div class="contenedor">
                    <h4 class="destacar"> 🌟 Datos Semi-Estructurados</h4>
                    <p class="justificar">⚠️ En construcción...</p>
                    </div>""", unsafe_allow_html=True)
with est3:
        st.markdown("""<div class="contenedor">
                    <h4 class="destacar"> ✨ Datos No Estructurados</h4>
                    <p class="justificar">⚠️ En construcción...</p>
                    </div>""", unsafe_allow_html=True)

st.header("Tipos de Datos")
st.markdown("""<div class="justificar">
                    <p>⚠️ En construcción... </p>
                    </div>""", unsafe_allow_html=True)

st.subheader("🎲 Datos Númericos:")
st.markdown("""<div class="justificar">
                    <p>⚠️ En construcción... </p>
                    </div>""", unsafe_allow_html=True)

num1, num2 = st.columns(2)
with num1:
    with st.expander(":red[**🔢 Números Enteros**]"):
        st.markdown("""<div class="justificar">
                            <spam class="destacar"> BIT: </spam>
                            <p>⚠️ En construcción...  </p>
                            <spam class="destacar"> TINYINT: </spam>
                            <p>⚠️ En construcción...  </p>
                            <spam class="destacar"> SMALLINT: </spam>
                            <p>⚠️ En construcción...  </p>
                            <spam class="destacar">INT: </spam>
                            <p>⚠️ En construcción...  </p>
                            <spam class="destacar"> BIGINT: </spam>
                            <p>⚠️ En construcción...  </p>
                            </div>""", unsafe_allow_html=True)
with num2:
    with st.expander(":red[**🔣 Números Decimales**]"):
        st.markdown("""<div class="justificar">
                            <spam class="destacar"> FLOAT: </spam>
                            <p>⚠️ En construcción...  </p>
                            <spam class="destacar"> MONEY: </spam>
                            <p>⚠️ En construcción...  </p>
                            <spam class="destacar"> DECIMAL: </spam>
                            <p>⚠️ En construcción...  </p>
                            </div>""", unsafe_allow_html=True)

st.subheader("📝 Datos de Texto:")
st.markdown("""<div class="justificar">
                    <p>⚠️ En construcción... </p>
                    </div>""", unsafe_allow_html=True)

tex1, tex2 = st.columns(2)
with tex1:
    st.markdown("""<div class="contenedor-lista">
                    <b class="destacar"> CHAR </b><br>
                    ⚠️ En construcción... 
                    </div>""", unsafe_allow_html=True)
    st.markdown("""<div class="contenedor-lista">
                        <b class="destacar"> N-CHAR </b><br>
                        ⚠️ En construcción... 
                        </div>""", unsafe_allow_html=True)
with tex2:
    st.markdown("""<div class="contenedor-lista">
                    <b class="destacar"> VARCHAR </b><br>
                    ⚠️ En construcción... 
                    </div>""", unsafe_allow_html=True)
    st.markdown("""<div class="contenedor-lista">
                        <b class="destacar"> N-VARCHAR </b><br>
                        ⚠️ En construcción... 
                        </div>""", unsafe_allow_html=True)

st.write(" ") 
with st.expander("**:red[🎯 ¿Cuando Utilizar Cada Uno?]**", expanded=True):
    st.markdown("""<div class="justificar">
                        <spam class="destacar"> CHAR </spam>
                        <p>⚠️ En construcción...  </p>
                        <spam class="destacar"> VARCHAR </spam>
                        <p>⚠️ En construcción...  </p>
                        <spam class="destacar"> UNICODE </spam>
                        <p>⚠️ En construcción...  </p>
                        </div>""", unsafe_allow_html=True)

st.subheader("📆 Datos de Fecha:")
st.markdown("""<div class="justificar">
                    <p>⚠️ En construcción... </p>
                    </div>""", unsafe_allow_html=True)

fech1, fech2 = st.columns(2)
with fech1:
       with st.container(border=True):
         st.markdown('''<b class="destacar">DATE</b><br>
                   ⚠️ En construcción...
                   ''',  unsafe_allow_html=True)
       with st.container(border=True):
         st.markdown('''<b class="destacar">DATETIME</b><br>
                   ⚠️ En construcción...
                   ''',  unsafe_allow_html=True)
with fech2:
       with st.container(border=True):
         st.markdown('''<b class="destacar">TIME</b><br>
                   ⚠️ En construcción...
                   ''',  unsafe_allow_html=True)
       with st.container(border=True):
         st.markdown('''<b class="destacar">SMALLDATETIME</b><br>
                   ⚠️ En construcción...
                   ''',  unsafe_allow_html=True)
    
utils.cambio_pag(ant="Indice/TEMA 00/01_Introduccion.py", sig="Indice/TEMA 01/00_Normalizacion.py")