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

st.header("Estructura de los Datos")
st.markdown("""<div class="justificar">
                    <p>El diseño de una base de datos determina su rendimiento técnico real. La forma en que organizamos, estructuramos y almacenamos los datos determina de manera directa la <b class="destacar">velocidad, la escalabilidad y la eficiencia</b> de la base de datos. Un modelado de datos preciso previene la degradación del rendimiento cuando el volumen de consultas aumenta, evitando costosos cuellos de botella en el uso de la memoria RAM y en los ciclos de lectura y escritura en disco.<br><br>
                    Para abordar este desafío de manera óptima, la arquitectura de datos clasifica la información según su nivel de organización interna y flexibilidad, dividiéndola formalmente en tres grandes familias:</p>
                    </div>""", unsafe_allow_html=True)

est1, est2, est3 = st.columns(3)
with est1:
        st.markdown("""<div class="contenedor">
                    <h4 class="destacar"> 💫 Datos Estructurados</h4>
                    <p class="justificar">Son aquellos datos que han sido clasificados, estandarizados y formateados bajo un esquema predefinido antes de ser almacenados. Antes de guardar un solo registro, el sistema ya exige saber el tipo exacto de dato que va a recibir, su longitud máxima y las reglas que debe cumplir.</p>
                    </div>""", unsafe_allow_html=True)
with est2:
        st.markdown("""<div class="contenedor">
                    <h4 class="destacar"> 🌟 Datos Semi-Estructurados</h4>
                    <p class="justificar">No siguen la estructura estricta de una tabla, pero contienen etiquetas o marcadores que separan y jerarquizan la información para que pueda ser leída por máquinas. Los ejemplos más comunes son los archivos JSON, XML o HTML que utilizamos a diario en el desarrollo web.</p>
                    </div>""", unsafe_allow_html=True)
with est3:
        st.markdown("""<div class="contenedor">
                    <h4 class="destacar"> ✨ Datos No Estructurados</h4>
                    <p class="justificar">Es información cruda que carece de un modelo predefinido. No encaja fácilmente en tablas tradicionales y requiere sistemas avanzados o Inteligencia Artificial para ser analizada. Incluye archivos como imágenes, videos, audios, documentos PDF o el cuerpo de un correo electrónico.</p>
                    </div>""", unsafe_allow_html=True)

st.header("Tipos de Datos")
st.markdown("""<div class="justificar">
                    <p>En el ámbito del diseño de bases de datos, los tipos de datos constituyen el componente fundamental para la construcción del esquema lógico y físico. Lejos de ser meras etiquetas, representan la especificación técnica que define el dominio de valores válidos que un atributo puede adoptar. Cada campo de una tabla debe poseer un tipo de dato asignado de forma obligatoria, actuando como un contrato de integridad que impide la corrupción de la información al rechazar automáticamente cualquier entrada incorrecta.<br><br>
                    Comprender el propósito y la mecánica de estas estructuras es el paso crítico para transformar un modelo conceptual abstracto en una base de datos física ágil, robusta y con capacidad de crecimiento a largo plazo.</p>
                    </div>""", unsafe_allow_html=True)

st.subheader("🎲 Datos Númericos:")
st.markdown("""<div class="justificar">
                    <p>Los tipos numéricos almacenan números enteros o decimales. El tipo numérico específico determinará el rango, la precisión y el tamaño de almacenamiento de los números almacenados. Los tipos de datos más comunes en esta categoría son </p>
                    </div>""", unsafe_allow_html=True)

num1, num2 = st.columns(2)
with num1:
    with st.expander(":red[**🔢 Números Enteros:**]"):
        st.markdown("""<div class="justificar">
                            <spam class="destacar"> BIT: </spam>
                            <p>Solo puede almacenar un 0, un 1. Es perfecto para valores booleanos.  </p>
                            <spam class="destacar"> TINYINT: </spam>
                            <p>Almacena números enteros muy pequeños, desde el 0 hasta el 255.  </p>
                            <spam class="destacar"> SMALLINT: </spam>
                            <p>Soporta números desde -32,768 hasta 32,767. Útil para conteos medianos.  </p>
                            <spam class="destacar">INT: </spam>
                            <p>Se utiliza frecuentemente para los identificadores (IDs) de usuarios o registros, y grandes cantidades.  </p>
                            <spam class="destacar"> BIGINT: </spam>
                            <p>Reservado para números gigantescos (soporta cifras de hasta 19 dígitos). </p>
                            </div>""", unsafe_allow_html=True)
with num2:
    with st.expander(":red[**🔣 Números Decimales:**]"):
        st.markdown("""<div class="justificar">
                            <spam class="destacar"> FLOAT: </spam>
                            <p>Almacena números con decimales de precisión flotante (aproximada)  </p>
                            <spam class="destacar"> MONEY: </spam>
                            <p>Un tipo de dato optimizado (disponible en motores como SQL Server) para manejar valores monetarios. Garantiza precisión exacta hasta con 4 decimales.  </p>
                            <spam class="destacar"> DECIMAL: </spam>
                            <p>(También llamado NUMERIC). Almacena números con una precisión y escala exacta que tú mismo defines. Evitando por completo los problemas de redondeo.  </p>
                            </div>""", unsafe_allow_html=True)

st.subheader("📝 Datos de Texto:")
st.markdown("""<div class="justificar">
                    <p>Un dato tipo texto (o cadena de caracteres) es una secuencia formada por letras, números, símbolos o espacios que se usa para representar información legible, identificar etiquetas o almacenar contenidos largos sin realizar operaciones matemáticas con ellos.</p>
                    </div>""", unsafe_allow_html=True)

tex1, tex2 = st.columns(2)
with tex1:
    st.markdown("""<div class="contenedor-lista">
                    <b class="destacar">✏️ CHAR </b><br>
                    Texto de longitud fija. Si defines un tamaño de 10 caracteres y guardas la palabra "Sol", el sistema rellenará los 7 espacios restantes con espacios en blanco.
                    </div>""", unsafe_allow_html=True)
    st.markdown("""<div class="contenedor-lista">
                        <b class="destacar">✏️ N-CHAR </b><br>
                        La versión de longitud fija pero con soporte Unicode. Permite guardar caracteres de múltiples idiomas (acentos, kanjis, cirílico) e incluso emojis.<br><br> 
                        </div>""", unsafe_allow_html=True)
with tex2:
    st.markdown("""<div class="contenedor-lista">
                    <b class="destacar">✏️ VARCHAR </b><br>
                    Texto de longitud variable. Es el estándar para ahorrar almacenamiento de forma eficiente. 
                    </div>""", unsafe_allow_html=True)
    st.markdown("""<div class="contenedor-lista">
                        <b class="destacar">✏️ N-VARCHAR </b><br>
                        La versión Unicode de longitud variable. Combina lo mejor de ambos mundos: ahorra espacio ajustándose al tamaño del texto real y permite guardar cualquier tipo de carácter
                        </div>""", unsafe_allow_html=True)

st.write(" ") 
with st.expander("**:red[🎯 ¿Cuando Utilizar Cada Uno?]**", expanded=True):
    st.markdown("""<div class="justificar">
                        <spam class="destacar">📌 CHAR: </spam>
                        <p>Se utiliza solo cuando se tiene certeza absoluta de que todos los registros medirán exactamente lo mismo. Ejemplos: Códigos de país ('US', 'MX'), hashes de contraseñas, o documentos de identidad con formato estricto.  </p>
                        <spam class="destacar">📌 VARCHAR: </spam>
                        <p>Es la opción predeterminada para casi todo. Se usa cuando la longitud del texto varíe de un usuario a otro: nombres, correos electrónicos, direcciones o descripciones de productos.  </p>
                        <spam class="destacar">📌 UNICODE: </spam>
                        <p>Indispensable si la plataforma es multi-idioma o si se permite que los usuarios envíen mensajes desde sus teléfonos (para soportar emojis sin romper la base de datos). Se tiene que usar con inteligencia, ya que pesa más. </p>
                        </div>""", unsafe_allow_html=True)

st.subheader("📆 Datos de Fecha:")
st.markdown("""<div class="justificar">
                    <p>Los tipos de datos de fecha y hora permiten almacenar y consultar información temporal con precisión. Los principiantes pueden pensar que pueden utilizar tipos de datos numéricos o de cadena para codificar este tipo de información. Sin embargo, hacerlo puede causar problemas posteriores con el análisis de datos. El uso de un tipo de datos de calendario específico puede facilitar mucho las cosas.</p>
                    </div>""", unsafe_allow_html=True)

fech1, fech2 = st.columns(2)
with fech1:
       with st.container(border=True):
         st.markdown('''<b class="destacar">⏰ DATE</b><br>
                   Guarda estrictamente la fecha (Año, Mes y Día), ignorando por completo la hora.
                   ''',  unsafe_allow_html=True)
       with st.container(border=True):
         st.markdown('''<b class="destacar">⏰ TIME</b><br>
                   Almacena únicamente la hora (Horas, Minutos, Segundos y Fracciones), sin importar el día.
                   ''',  unsafe_allow_html=True)   
with fech2:
       with st.container(border=True):
         st.markdown('''<b class="destacar">⏰ DATETIME</b><br>
                   Almacena tanto la fecha como la hora exacta, incluyendo fracciones de segundo.
                   ''',  unsafe_allow_html=True)
       with st.container(border=True):
         st.markdown('''<b class="destacar">⏰ SMALLDATETIME</b><br>
                   Una versión más ligera de DATETIME. Solo llega a la precisión de minutos (redondea los segundos) y ocupa la mitad de espacio.
                   ''',  unsafe_allow_html=True)
    
utils.cambio_pag(ant="Indice/TEMA 00/01_Introduccion.py", sig="Indice/TEMA 01/00_Normalizacion.py")