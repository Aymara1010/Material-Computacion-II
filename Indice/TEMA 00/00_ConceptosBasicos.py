import streamlit as st
import utils

st.title("🧩 Conceptos Básicos")

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

st.divider()
st.header(":red[Sistemas y Estructuras Generales:]")

st.subheader("☁️ Base de Datos")
st.markdown("""<div class="justificar">
                    <p>Es un conjunto organizado de información o datos estructurados que se almacenan electrónicamente en un sistema (gestionado por un motor o SGBD). Su propósito es permitir el almacenamiento, administración, consulta y actualización de grandes volúmenes de datos con rapidez, orden y seguridad. </p>
                    </div>""", unsafe_allow_html=True)

bd1, bd2 = st.columns(2)
with bd1:
       with st.container(border=True):
         st.markdown('''<b class="destacar">🎯 Relacionales</b><br>
                    Son sistemas de gestión que organizan la información de manera rigurosa en tablas estructuradas, las cuales están compuestas por filas (registros) y columnas (campos). Utilizan lenguaje SQL y garantizan la integridad de los datos.
                   ''',  unsafe_allow_html=True)
with bd2:
       with st.container(border=True):
         st.markdown('''<b class="destacar">🎯 No Relacionales</b><br>
                   Son bases de datos que prescinden del modelo tradicional de tablas interconectadas. Diseñadas para ser altamente flexibles y escalables, almacenan los datos en formatos variados según su naturaleza (como documentos JSON, grafos o pares clave-valor).
                   ''',  unsafe_allow_html=True)
         
st.subheader("📌 Archivos")
st.markdown("""<div class="justificar">
                    <p>Es el conjunto de datos estructurados almacenados físicamente en un disco o dispositivo de memoria. En bases de datos, el gestor utiliza archivos de datos y archivos de registro (logs) para guardar la información real subyacente de las tablas.</p>
                    </div>""", unsafe_allow_html=True)

st.divider()
st.header(":red[Modelado de Datos:]")

st.subheader("💡 Entidades")
st.markdown("""<div class="justificar">
                    <p> Representan un objeto o concepto fundamental, ya sea real (como una persona) o abstracto (como una venta), sobre el cual se requiere almacenar información. Actúan como los "sustantivos" en el modelado y, en el diseño relacional, cada entidad se traduce en una tabla independiente.</p>
                    </div>""", unsafe_allow_html=True)

ent1, ent2 = st.columns(2)
with ent1:
    with st.expander("⚡️ :red[**Entidades Fuertes**]", expanded=True):
        st.markdown("""<div class="justificar">
                    <p>Son aquellas que existen de forma autónoma dentro del sistema. No dependen de ninguna otra entidad para tener sentido en el negocio y poseen su propia clave primaria para identificar sus registros.</p>
                    </div>""", unsafe_allow_html=True)
with ent2:
    with st.expander("⚡️ :red[**Entidades Debiles**]", expanded=True):
        st.markdown("""<div class="justificar">
                    <p>Son aquellas cuya existencia depende por completo de una entidad fuerte (entidad padre). Carecen de una clave primaria propia y necesitan combinar la clave de su entidad padre con un atributo discriminador para poder identificarse.</p>
                    </div>""", unsafe_allow_html=True)

st.subheader("🌱 Campos y  Atributos")
st.markdown("""<div class="justificar">
                    <p>Representan las unidades mínimas de información que describen las propiedades o características de una entidad. Suelen usarse como sinónimos, pero tienen un matiz técnico dependiendo de la fase de diseño:</p>
                    </div>""", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown("""<div class="contenedor">
                    <b class="destacar">🌼 Campo </b><br>
                    Se usa en la fase de diseño teórico y conceptual (Modelado de datos) para describir las características de una entidad en papel o diagrama.
                    </div>""", unsafe_allow_html=True)
with col2:
    st.markdown("""<div class="contenedor">
                    <b class="destacar">🌻 Atributos </b><br>
                    Se usa en la fase de implementación práctica y técnica (Bases de datos reales). Corresponde directamente a las columnas físicas de una tabla.
                    </div>""", unsafe_allow_html=True)
        
st.subheader("📌 Registros")
st.markdown("""<div class="justificar">
                    <p>Es el conjunto completo de datos almacenados en los campos que representan una instancia única y real de una entidad. En la práctica, cada registro es una fila completa dentro de una tabla.</p>
                    </div>""", unsafe_allow_html=True)

st.divider()
st.header(":red[Conexiones y Reglas:]")

st.subheader("📌 Relación")
st.markdown("""<div class="justificar">
                    <p>Es la asociación, vínculo o conexión lógica establecida entre dos o más entidades. Define cómo interactúan los datos entre sí y permite cruzar información de distintas tablas, actuando como los "verbos" del sistema (ej. un cliente compra un producto). </p>
                    </div>""", unsafe_allow_html=True)

st.subheader("📌 Cardinalidad")
st.markdown("""<div class="justificar">
                    <p>Define la naturaleza numérica de una relación. Especifica el número mínimo y máximo de veces que una instancia de una entidad puede asociarse con los registros de otra entidad (por ejemplo: de "uno a uno", "uno a muchos" o "muchos a muchos").</p>
                    </div>""", unsafe_allow_html=True)

st.divider()
st.header(":red[Claves e Identificadores:]")

st.subheader("🔑 Clave Primaria PK")
st.markdown("""<div class="justificar">
                    <p>Es el campo, o combinación de campos, que identifica de forma única, exclusiva e irrepetible a cada registro dentro de una tabla. Garantiza que no existan dos filas idénticas y nunca puede estar vacía (no admite valores nulos).</p>
                    </div>""", unsafe_allow_html=True)

pk1, pk2 = st.columns(2)
with pk1:
    with st.expander("📂 :red[**Simples**] ✨", expanded=True):
        st.markdown("""<div class="justificar">
                    <p>Claves primarias formadas por un único campo o columna (por ejemplo, un ID de usuario o número de pasaporte).<br><br></p>
                    </div>""", unsafe_allow_html=True)
with pk2:
    with st.expander("📂 :red[**Compuestas**] ✨", expanded=True):
        st.markdown("""<div class="justificar">
                    <p>Claves primarias formadas por la combinación de dos o más campos, usadas frecuentemente en tablas intermedias para garantizar la unicidad de ese cruce de datos.</p>
                    </div>""", unsafe_allow_html=True)

st.subheader("🔑 Clave Fóranea FK")
st.markdown("""<div class="justificar">
                    <p>Es el campo, o conjunto de campos, que hace referencia directa a la clave primaria de otra tabla. Funciona como un "ancla" que establece y garantiza el vínculo lógico (integridad referencial) entre los registros de ambas tablas, impidiendo que existan datos huérfanos.</p>
                    </div>""", unsafe_allow_html=True)

utils.cambio_pag(ant="Indice/00_inicio.py", sig="Indice/TEMA 00/01_Introduccion.py")