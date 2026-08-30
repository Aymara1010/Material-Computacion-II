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
    .contenedor-lista {
        background-color: #1E2023;
        padding: 15px;
        border-radius: 5px;
        border-left: 5px solid #FF4B4B;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Cardinalidad y Jerarquías")

st.header("Repaso de Interrelaciones")
st.markdown("""<div class="justificar">
            ⚠️🔨 En Construcción...
            </div>""", unsafe_allow_html=True)

st.subheader("Como Identificarlas:")
int1, int2, int3 = st.columns(3)
with int1:
    with st.container(border=True):
        st.markdown("""<div class="justificar">
                        <h4 class="destacar">Unaria</h4>
                        ⚠️🔨 En Construcción...
                       <br><br></div>""", unsafe_allow_html=True)
with int2:
    with st.container(border=True):
        st.markdown("""<div class="justificar">
                        <h4 class="destacar">Binaria</h4>
                        ⚠️🔨 En Construcción...
                       <br><br></div>""", unsafe_allow_html=True)
with int3:
    with st.container(border=True):
        st.markdown("""<div class="justificar">
                        <h4 class="destacar">Ternaria</h4>
                        ⚠️🔨 En Construcción...
                       <br><br></div>""", unsafe_allow_html=True)

st.header("Participación y Cardinalidades")
st.markdown("""<div class="justificar">
            ⚠️🔨 En Construcción...
            </div>""", unsafe_allow_html=True)

st.header("Participación:")
st.markdown("""<div class="justificar">
            ⚠️🔨 En Construcción...
            </div>""", unsafe_allow_html=True)

par1, par2 = st.columns(2)
with par1:
    st.subheader("Participación Total")
    st.markdown("""<div class="justificar">
                    <p>⚠️🔨 En Construcción...<br>
                    <h5 class="destacar">Por Ejemplo:</h5>
                    ⚠️🔨 En Construcción....</p>
                    </div>""", unsafe_allow_html=True)
    with st.expander("**Forma**"):
              st.markdown("") 
with par2:
    st.subheader("Participación Parcial")
    st.markdown("""<div class="justificar">
                    <p>⚠️🔨 En Construcción...<br>
                    <h5 class="destacar">Por Ejemplo:</h5>
                    ⚠️🔨 En Construcción....</p>
                    </div>""", unsafe_allow_html=True)
    with st.expander("**Forma**"):
              st.markdown("") 

st.header("Cardinalidad:")
st.markdown("""<div class="justificar">
            ⚠️🔨 En Construcción...
            <br><br></div>""", unsafe_allow_html=True)

car1, car2, car3 = st.columns(3)
with car1:
    st.markdown("""<div class="contenedor-lista">
                    <h4 class="destacar">Uno a Uno</h4>
                    <p>⚠️🔨 En Construcción...</p>
                    </div>""", unsafe_allow_html=True)
    st.write(" ")
    with st.expander("**Forma**"):
                  st.markdown("")
with car2:
    st.markdown("""<div class="contenedor-lista">
                    <h4 class="destacar">Uno a Muchos</h4>
                    <p>⚠️🔨 En Construcción...</p>
                    </div>""", unsafe_allow_html=True)
    st.write(" ")
    with st.expander("**Forma**"):
                  st.markdown("")
with car3:
    st.markdown("""<div class="contenedor-lista">
                    <h4 class="destacar">Muchos a Muchos</h4>
                    <p>⚠️🔨 En Construcción...</p>
                    </div>""", unsafe_allow_html=True)
    st.write(" ")
    with st.expander("**Forma**"):
                  st.markdown("")

st.header("Según el Grado de la Interrelación:")
st.markdown("""<div class="justificar">
            ⚠️🔨 En Construcción...
            <br><br></div>""", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["UNARIA" ,"BINARIA" ,"TERNARIA"])
with tab1:
    st.subheader("Unarias")
    st.markdown("""<div class="justificar">
            ⚠️🔨 En Construcción...
            <br><br></div>""", unsafe_allow_html=True)
    gra1, gra2 = st.columns(2, border=True)
    with gra1:
       st.markdown("""<div class="justificar">
                    <h4 class="destacar">Participación</h4>
                    ⚠️🔨 En Construcción...
                    <br><br></div>""", unsafe_allow_html=True) 
    with gra2:
           st.markdown("""<div class="justificar">
                        <h4 class="destacar">Cardinalidad</h4>
                        ⚠️🔨 En Construcción...
                        <br><br></div>""", unsafe_allow_html=True)
with tab2:
    st.subheader("Binarias")
    st.markdown("""<div class="justificar">
            ⚠️🔨 En Construcción...
            <br><br></div>""", unsafe_allow_html=True)
    gra1, gra2 = st.columns(2, border=True)
    with gra1:
       st.markdown("""<div class="justificar">
                    <h4 class="destacar">Participación</h4>
                    ⚠️🔨 En Construcción...
                    <br><br></div>""", unsafe_allow_html=True) 
    with gra2:
           st.markdown("""<div class="justificar">
                        <h4 class="destacar">Cardinalidad</h4>
                        ⚠️🔨 En Construcción...
                        <br><br></div>""", unsafe_allow_html=True)
with tab3:
    st.subheader("Ternarias")
    st.markdown("""<div class="justificar">
            ⚠️🔨 En Construcción...
            <br><br></div>""", unsafe_allow_html=True)
    gra1, gra2 = st.columns(2, border=True)
    with gra1:
       st.markdown("""<div class="justificar">
                    <h4 class="destacar">Participación</h4>
                    ⚠️🔨 En Construcción...
                    <br><br></div>""", unsafe_allow_html=True) 
    with gra2:
           st.markdown("""<div class="justificar">
                        <h4 class="destacar">Cardinalidad</h4>
                        ⚠️🔨 En Construcción...
                        <br><br></div>""", unsafe_allow_html=True)

st.header("Agregaciones")
st.markdown("""<div class="justificar">
            ⚠️🔨 En Construcción...
            <br><br></div>""", unsafe_allow_html=True)
with st.expander("**Forma**"):
                  st.markdown("")
                  
st.subheader("Agregación vs Ternaria:")
st.markdown("""<div class="justificar">
            ⚠️🔨 En Construcción...
            </div>""", unsafe_allow_html=True)

agr1, agr2 = st.columns(2)
with agr1:
    st.subheader("Agregación:")
    st.markdown("""<div class="justificar">
            ⚠️🔨 En Construcción...
            <br><br></div>""", unsafe_allow_html=True)
    with st.expander("**Características:**"):
        st.markdown("""<div class="justificar">
                    <spam class="destacar">Titulo:</spam>
                    <p> ⚠️🔨 En Construcción... </p>
                    </div>""", unsafe_allow_html=True) 
with agr2:
    st.subheader("Ternaria:")
    st.markdown("""<div class="justificar">
            ⚠️🔨 En Construcción...
            <br><br></div>""", unsafe_allow_html=True)
    with st.expander("**Características:**"):
        st.markdown("""<div class="justificar">
                    <spam class="destacar">Titulo:</spam>
                    <p> ⚠️🔨 En Construcción... </p>
                    </div>""", unsafe_allow_html=True) 
                
st.header("Jerarquías")
st.markdown("""<div class="justificar">
            ⚠️🔨 En Construcción...
            </div>""", unsafe_allow_html=True)

comp1, comp2 = st.columns(2)
with comp1:
    st.subheader("Cobertura:", text_alignment="center")
    with st.container(border=True):
        st.markdown("""<div class="justificar">
            ⚠️🔨 En Construcción...
            <br><br></div>""", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Total", text_alignment="center")
        with st.container(border=True):
         st.markdown("""<div class="justificar">
            ⚠️🔨 En Construcción...
         <br><br></div>""", unsafe_allow_html=True)
    with col2:
        st.subheader("Parcial", text_alignment="center")
        with st.container(border=True):
         st.markdown("""<div class="justificar">
            ⚠️🔨 En Construcción...
         <br><br></div>""", unsafe_allow_html=True)
    with st.expander("**Forma**"):
        st.markdown("""""", unsafe_allow_html=True)
with comp2:
    st.subheader("Solapamiento:", text_alignment="center")
    with st.container(border=True): 
        st.markdown("""<div class="justificar">
            ⚠️🔨 En Construcción...
            <br><br></div>""", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Disjuntas", text_alignment="center")
        with st.container(border=True):
         st.markdown("""<div class="justificar">
            ⚠️🔨 En Construcción...
            <br><br></div>""", unsafe_allow_html=True)
    with col2:
        st.subheader("Con Solapamiento", text_alignment="center")
        with st.container(border=True):
         st.markdown("""<div class="justificar">
            ⚠️🔨 En Construcción...
            <br><br></div>""", unsafe_allow_html=True)
    with st.expander("**Forma**"):
        st.markdown("""""", unsafe_allow_html=True)

utils.cambio_pag(ant="Indice/TEMA 02/00_IntroduccionDER.py", sig="Indice/TEMA 03/00_SQL.py")