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
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("**🏠 ¡ Bienvenid@ a Mis Apuntes de Computación II !**")

st.markdown('''
            <div class="justificar">
            Aquí encontrarás todo el contenido teorico referente a la materia <spam class="destacar"> Computación II </spam>, puedes ver en la barra lateral izquierda todos los temas en los que puedes navegar o simplemente ve al final de la página para ir al siguiente capítulo, ¿Qué esperas? ¡Sientete libre de explorar y aprender! ✨✨<br><br>
            </div>''', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown('''
            <div class="contenedor">
            <spam class="destacar"> 🔎 ¿Cómo Usar la App? </spam>
            <p class="justificar"> Texto</p>
            </div>
            ''',  unsafe_allow_html=True)
    
    st.subheader("📋 Plan de Evaluación:")
    
    tab1, tab2, tab3, tab4 = st.tabs(["Challenges" ,"Parcial", "Exposición", "Trabajo Final"])
    
    with tab1:
        st.markdown("""""", unsafe_allow_html=True)  
    with tab2:
        st.markdown("""""", unsafe_allow_html=True)
    with tab3:
        st.markdown("""""", unsafe_allow_html=True) 
    with tab4:
        st.markdown("""""", unsafe_allow_html=True)

with col2:        
    st.subheader("📖 Temas a Explorar:")
    

utils.cambio_pag(sig="Indice/GENERAL/01_Introduccion.py")