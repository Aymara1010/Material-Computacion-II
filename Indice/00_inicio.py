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
    </style>
    """, unsafe_allow_html=True)

st.title("**🏠 ¡Bienvenid@ a Mis Apuntes de Computación II!**")

st.markdown('''
            <div class="justificar">
            ¡Hola, mi nombre es Aymara! Y he creado esta app para guardar todo el contenido referente a la materia <spam class="destacar">Computación II</spam>, aquí encontrarás material de todo tipo así como ejemplos y ejercicios prácticos ¿Qué esperas? ¡Sientete libre de explorar! ✨✨<br><br>
            </div>''', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown('''
            <div class="contenedor">
            <spam class="destacar"> 🔎 ¿Cómo Usar la App? </spam>
            <p class="justificar">  Puedes ver en la barra lateral izquierda todos los temas en los que puedes navegar o simplemente ve al final de la página para ir al siguiente capítulo.</p>
            </div>
            ''',  unsafe_allow_html=True)
    
    st.subheader("📋 Plan de Evaluación:")
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["General" ,"Challenges" ,"Parcial", "Exposición", "Trabajo Final"])
    
    with tab1:
        st.image("Plan-de-Evaluacion.jpeg")
        st.markdown("""<div class="justificar">
                    <p> <spam class="destacar">NOTA:</spam> La materia cuenta con algunos requisitos para aprobarla como el hecho de que para pasar la materia es necesario sacar 10 pts o más en el trabajo final. Así mismo, para hacer el trabajo final es necesario tener un un promedio mayor o igual a 12 pts entre el parcial y la exposición, como requisito adicional. </p>
                    </div>""", unsafe_allow_html=True)       
    with tab2:
        st.markdown("""<div class="justificar">
                    <spam class="destacar"> Challenge #1:</spam>
                    <p> La evaluación abarca el Tema 1 (Normalización y Denormalización), vale el 5% de la nota y será hecha por dos miembros del grupo.</p>
                    <spam class="destacar"> Challenge #2:</spam>
                    <p> La evaluación abarca el Tema 2 (DER), vale el 5% de la nota y será hecha por un miembro del grupo que no haya pasado antes.</p>
                    <spam class="destacar"> Challenge #3:</spam>
                    <p> La evaluación abarca el Tema 3 (SQL), vale el 5% de la nota y será hecha por los últimos dos miembros del grupo que no hayan pasado antes.</p>
                    </div>""", unsafe_allow_html=True)
    with tab3:
        st.markdown("""<div class="justificar">
                    <center class="destacar"> PARCIAL</center>
                    <p> Está es una evaluación representa el 30% de la nota final y abarca los tres temas vistos en clase (tanto la parte teorica como la parte práctica).<br><br>
                    La evaluación se hará de forma individual y su nota, junto con la exposición grupal, forman parte del requisito minimo para hacer el Trabajo Final.<br><br>
                    Si el promedio entre la <spam class="destacar">Nota del Parcial</spam> y la Nota de la exposición es mayor o igual a 12 pts, entonces se puede hacer el Trabajo Final.</p>
                    </div>""", unsafe_allow_html=True) 
    with tab4:
        st.markdown("""<div class="justificar">
                    <center class="destacar"> EXPOSICIONES</center>
                    <p> Esta evaluación representa el 20% de la nota final y consiste en exponer una herramienta (ya sea un SGBD, una herramienta de BI o un controlador de versiones), esta exposición estará dividida en tres partes:<br><br>
                    <spam class="destacar">Parte I: Teoria (7 pts)</spam>, donde se explica el mercado y las bondades de la herramienta.<br><br>
                    <spam class="destacar">Parte II: Práctica (7 pts)</spam>, donde se busca atender y explicar un ejercicio propuesto por los profesores, simulando un caso real.<br><br>
                    <spam class="destacar">Parte III: Video (6 pts)</spam>, donde se realizará un video explicando toda el aspecto práctico de la herramienta.</p>
                    </div>""", unsafe_allow_html=True)
    with tab5:
        st.markdown("""<div class="justificar">
                    <center class="destacar"> TRABAJO FINAL</center>
                    <p> Esta evaluación representa el 35% de la nota final, para poder presentarla es necesario tener un promedio entre el parcial y la exposición de <spam class="destacar">minimo 12 pts</spam>, además, se tiene como requisito para pasar la materia tener 10 pts o más en esta evaluación.<br><br>
                    La evaluación consiste en realizar un trabajo práctico donde se utilizarán todas las habilidades dadas a lo largo de la materia, como SQL, normalización y denormalización.</p>
                    </div>""", unsafe_allow_html=True)

with col2:        
    st.subheader("📖 Temas a Explorar:")
    
    with st.expander("**📌 TEMA 00:**  Introducción a las BBDD", expanded=True):
        st.markdown("""<div class="justificar">
                    <spam class="destacar"> 0.1 - Introducción a las BBDD:</spam>
                    <p>📑 ¿Qué son las BBDD? ¿Cuales son sus Tipos? Tipos de Datos, Importancia y Uso de las BBDD...</p>
                    <spam class="destacar"> 0.2 - Conceptos Básicos:</spam>
                    <p>📑 Glosario de térmimos importantes de las bases de datos... </p>
                    </div>""", unsafe_allow_html=True) 
           
    with st.expander("**📌 TEMA 01:**  Normalización en BBDD", expanded=True):
        st.markdown("""<div class="justificar">
                    <spam class="destacar"> 1.1 - Normalización:</spam>
                    <p>📑 Introducción a las normalización en bases de datos y sus 3 formas normales. </p>
                    <spam class="destacar"> 1.2 - Denormalización:</spam>
                    <p>📑 Introducción a la Denormalización y sus técnicas.</p>
                    <spam class="destacar"> 1.3 - Comparación de Modelos:</spam>
                    <p>📑 Comparación entre la normalización y denormalización, cuando y como usar cada una y su importancia en el diseño de BBDD.</p>
                    </div>""", unsafe_allow_html=True)
        
    with st.expander("**📌 TEMA 02:**  Diagramas Entidad Relación"):
        st.markdown("""<div class="justificar">
                    <spam class="destacar"> 2.1 - Introducción a DER:</spam>
                    <p>📑 Introducción a los diagramas entidad-relación y conceptos importantes a tomar en cuenta. </p>
                    <spam class="destacar"> 2.2 - Notación de DER:</spam>
                    <p>📑 Notación necesaria para DER y sus elementos. </p>
                    </div>""", unsafe_allow_html=True)
        
    with st.expander("**📌 TEMA 03:**  Consultas con SQL"):
        st.markdown("""<div class="justificar">
                    <spam class="destacar"> 3.0 - Consultas en SQL</spam>
                    <p>⚠️ En construcción... </p>
                    </div>""", unsafe_allow_html=True)

utils.cambio_pag(sig="Indice/GENERAL/01_Introduccion.py")