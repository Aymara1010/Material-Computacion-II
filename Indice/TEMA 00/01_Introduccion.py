import streamlit as st
import utils

st.title("🎯 Introducción a las Bases de Datos")

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
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

st.header("¿Qué son las Bases de Datos?")
st.markdown("""<div class="justificar">
                    <p>Una <b class="destacar">base de datos</b> es un ecosistema digital diseñado para actuar como un contenedor organizado de información, a menudo, en un conjunto de tablas (llamadas entidades) que a su vez están formadas por filas (llamados registros) y columnas (llamados campos). Su propósito fundamental es almacenar, estructurar y relacionar datos con el fin de que puedan ser consultados de forma rápida y eficiente.<br><br>
                    Para comprender su utilidad de manera integral, este concepto puede abordarse desde dos perspectivas principales. Desde un <b class="destacar">enfoque analítico</b>, una base de datos se define como un conjunto de datos centralizado, persistente y en constante actualización, el cual sirve como núcleo para alimentar las operaciones y los sistemas diarios de cualquier organización.<br><br>
                    Por otro lado, desde un <b class="destacar">enfoque conceptual</b>, se entiende como la representación digital y lógica de un entorno o modelo de negocio. Bajo esta mirada, su arquitectura está diseñada para capturar fielmente la realidad de una empresa, reflejando el estado de los datos y las reglas bajo las cuales interactúan entre sí dentro del sistema.</p>
                    </div>""", unsafe_allow_html=True)

st.header("¿Qué es un Sistema de Gestión de Bases de Datos?")
st.markdown("""<div class="justificar">
                    <p>Un sistema de gestión de bases de datos (SGBD) es, en esencia, un <b class="destacar">software especializado</b> encargado de administrar este ecosistema digital. Funciona como el motor principal que traduce las peticiones de los usuarios en acciones directas sobre los archivos físicos alojados en el servidor.<br><br>
                    Gracias a este programa, los usuarios disponen de un conjunto de herramientas diseñadas para ejecutar diversas operaciones. Estas funciones les permiten tanto manipular la información almacenada para el trabajo diario, como <b class="destacar">diseñar, modificar y gestionar</b> la estructura interna de los datos.</p>
                    </div>""", unsafe_allow_html=True)

with st.expander(" 📍 **¿Por Qué Un Sistema de Gestión de Bases de Datos?**"):
    sis1, sis2 = st.columns(2)
    with sis1:
       with st.container(border=True):
         st.markdown('''<b class="destacar">⚡️ Espacio Físico</b><br>
                   Transforma archivos físicos enteros en bytes, reduciendo a cero el espacio físico requerido
                   ''',  unsafe_allow_html=True)
       with st.container(border=True):
                st.markdown('''<b class="destacar">⚡️ Seguridad</b><br>
                          Permite asignar permisos individuales para controlar con exactitud quién puede ver o modificar la información.
                          ''',  unsafe_allow_html=True)
    with sis2:
       with st.container(border=True):
         st.markdown('''<b class="destacar">⚡️ Velocidad</b><br>
                   Encuentra un dato específico entre millones de registros en solo milisegundos, ahorrando el tiempo de busqueda de la información.
                   ''',  unsafe_allow_html=True)
       with st.container(border=True):
                st.markdown('''<b class="destacar">⚡️ Capacidad</b><br>
                           Soporta millones de registros y miles de conexiones de usuarios concurrentes de forma simultánea sin colapsar.
                          ''',  unsafe_allow_html=True)

st.markdown("""<div class="justificar">
                    <p> Los sistemas de gestión de bases de datos (SGBD) se clasifican según sus estructuras o tipos de datos.</p>
                    </div>""", unsafe_allow_html=True)

st.subheader("📒 :red[Tipos de SGBD:]")
st.markdown("""<div class="justificar">
                    <p>Existen diferentes tipos de SGBD, cada uno con sus propias ventajas, desventajas y casos de uso. El tipo de SGBD determina cómo el software ve los datos y cómo permite a los usuarios buscar o modificar esa información según las necesidades del proyecto. </p>
                    </div>""", unsafe_allow_html=True)

bd1, bd2 = st.columns(2)
with bd1:
    with st.expander("✨ :red[**Bases de Datos Relacionales:**]", expanded=True):
        st.markdown("""<div class="justificar">
                    <p>Se define este tipo como sistemas que organizan la información en <b class="destacar">tablas estructuradas</b> con filas (registros) y columnas (atributos). Los datos de diferentes tablas se conectan explícitamente mediante claves primarias y foráneas. </p>
                    </div>""", unsafe_allow_html=True)
with bd2:
    with st.expander("✨ :red[**Bases de Datos No Relacionales:**]", expanded=True):
        st.markdown("""<div class="justificar">
                    <p>las bases de datos no relacionales representan cualquier sistema que <b class="destacar">no utiliza</b> el formato rígido de tablas, filas y columnas. Nacieron para gestionar datos no estructurados o semiestructurados. </p>
                    </div>""", unsafe_allow_html=True)

st.header("Bases de Datos Relacionales")
st.markdown("""<div class="justificar">
                    <p>Como ya se ha mencionado antes, una base de datos relacional es un tipo de base de datos que organiza la información en <b class="destacar">filas y columnas</b>, formando tablas donde los puntos de datos se conectan entre sí. Este tipo de base de datos suele ser el más utilizado debido a su estructura, por lo que es importante conocer los elementos que la conforman y las operaciones que se pueden hacer con ellas. </p>
                    </div>""", unsafe_allow_html=True)

st.subheader("💡 Elementos de una Base de Datos:")

ele1, ele2 = st.columns(2)
with ele1:
       with st.container(border=True):
         st.markdown('''<b class="destacar">🎯 Entidades</b><br>
                   Son los objetos principales de almacenamiento. Contienen toda la información organizada en filas y columnas.
                   ''',  unsafe_allow_html=True)
       with st.container(border=True):
                st.markdown('''<b class="destacar">🎯 Registros</b><br>
                          Contienen la información o datos individuales de una observación única.
                          ''',  unsafe_allow_html=True)
with ele2:
       with st.container(border=True):
         st.markdown('''<b class="destacar">🎯 Campos</b><br>
                   Definen el tipo específico de información que se va a guardar. Cada columna tiene un nombre y un tipo de dato fijo.
                   ''',  unsafe_allow_html=True)
       with st.container(border=True):
                st.markdown('''<b class="destacar">🎯 Claves</b><br>
                          Vinculan entidades mediante Claves Primarias y Claves Foráneas.
                          ''',  unsafe_allow_html=True)

st.subheader("🔎 Principales Operaciones en Una Base de Datos:")
st.markdown("""<div class="justificar">
                    <p>Las bases de datos relacionales se apoyan en un conjunto de operaciones fundamentales que van desde la creación del espacio de almacenamiento hasta el control diario de cada dato. Estas operaciones son: </p>
                    </div>""", unsafe_allow_html=True)

op1, op2, op3 = st.columns(3)
with op1:
    st.markdown("""<div class="contenedor">
                    <b class="destacar">🧩 Agregar Archivos </b><br>
                     Crea el espacio físico o la estructura digital para empezar a almacenar la información. 
                    </div>""", unsafe_allow_html=True)
    st.markdown("""<div class="contenedor">
                        <b class="destacar">🧩 Insertar Datos </b><br>
                        Añade registros de información nueva dentro de las tablas del sistema.
                        </div>""", unsafe_allow_html=True)
with op2:
    st.markdown("""<div class="contenedor">
                    <b class="destacar">🧩 Repuperar Datos </b><br>
                    Busca y muestra la información guardada para que el usuario pueda leerla.
                    </div>""", unsafe_allow_html=True)
    st.markdown("""<div class="contenedor">
                        <b class="destacar">🧩 Modificar Datos </b><br>
                        Actualiza o cambia la información existente que se ha vuelto obsoleta.
                        </div>""", unsafe_allow_html=True)
with op3:
    st.markdown("""<div class="contenedor">
                    <b class="destacar">🧩 Eliminar Archivos </b><br>
                    Destruye por completo el contenedor físico y toda la información almacenada en él.
                    </div>""", unsafe_allow_html=True)
    st.markdown("""<div class="contenedor">
                    <b class="destacar">🧩 Eliminar Datos </b><br>
                    Borra registros específicos de las tablas sin dañar el resto del sistema.
                    </div>""", unsafe_allow_html=True)
    
st.header("Claves Primarias y Foráneas:")
st.markdown("""<div class="justificar">
                    <p>Las claves primarias y foráneas son los elementos esenciales que permiten conectar tablas de forma lógica y mantener el orden en una base de datos relacional. <b class="destacar">Una clave primaria (PK)</b> es la columna (o grupo de columnas) que identifica de forma única e irrepetible a cada fila de una tabla, mientras que, <b class="destacar">una Clave Foránea (FK)</b> es la columna de una tabla secundaria que almacena la clave primaria de una tabla principal para crear un vínculo entre ambas.<br><br>
                    Ambas, son elementos escenciales al momento de conectar diferentes entidades (o tablas) entre si, permitiendo unir informacion relevante al momento de hacer alguna consulta, es por eso que cada una tiene ciertas reglas que cumplir para que no exista ningún inconveniente al momento de conectar cada las tablas entre si. </p>
                    </div>""", unsafe_allow_html=True)

pk, fk = st.columns(2)
with pk:
    with st.expander("📂 :red[**Reglas de las Claves Primarias: (PK)**]"):
        st.markdown("""<div class="justificar">
                    <spam class="destacar"> Regla #1:</spam>
                    <p>Solo puede existir una clave primaria por cada tabla.  </p>
                    <spam class="destacar"> Regla #2:</spam>
                    <p>No pueden existir dos filas con el mismo valor en esa columna.</p>
                    <spam class="destacar"> Regla #3:</spam>
                    <p>No puede quedar vacía; jamás acepta valores nulos.  </p>
                    <spam class="destacar"> Regla #4:</spam>
                    <p> Su valor no debe cambiar con el tiempo.<br><br> </p>
                    </div>""", unsafe_allow_html=True)
with fk:
    with st.expander("📂 :red[**Reglas de las Llaves Foráneas: (FK)**]"):
        st.markdown("""<div class="justificar">
                            <spam class="destacar"> Regla #1: </spam>
                            <p> El valor insertado en la clave foránea debe existir obligatoriamente en la clave primaria de la tabla origen.  </p>
                            <spam class="destacar"> Regla #2: </spam>
                            <p>A diferencia de la primaria, una clave foránea sí puede repetirse muchas veces.  </p>
                            <spam class="destacar"> Regla #3: </spam>
                            <p>Puede aceptar valores vacíos (NULL) si la relación es opcional.  </p>
                            <spam class="destacar"> Regla #4: </spam>
                            <p>En todas las entidades el tipo de dato debe estar igualmente definido.  </p>
                            </div>""", unsafe_allow_html=True)

st.subheader("🔑 :red[Tipos de Claves Primarias:]")
st.markdown("""<div class="justificar">
                    <p>Las claves primarias se dividen en simples y compuestas y se clasifican según la cantidad de campos que utilizan para identificar de forma única un registro dentro de una tabla. Eso si, no importa el tipo de clave que sea, esta siempre debe de cumplir las reglas anteriormente mencionadas. </p>
                    </div>""", unsafe_allow_html=True)

tip1, tip2 = st.columns(2)
with tip1:
    st.markdown("""<div class="contenedor">
                        <b class="destacar"> PKs Simples </b><br>
                        Es la opción estándar y más recomendada para el diseño de bases de datos relacionales y se define como un registro identificado de forma única mediante un solo campo.
                        </div>""", unsafe_allow_html=True)
with tip2:
    st.markdown("""<div class="contenedor">
                        <b class="destacar"> PKs Compuestas </b><br>
                        Registro identificado de forma única mediante la combinación de dos o más campos, se utiliza cuando un solo campo no es suficiente para garantizar la unicidad de un registro.
                        </div>""", unsafe_allow_html=True)

utils.cambio_pag(ant="Indice/TEMA 00/00_ConceptosBasicos.py", sig="Indice/TEMA 00/02_TiposdeDatos.py")