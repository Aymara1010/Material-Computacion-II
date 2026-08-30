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

st.title("🧱 Arquitecturas y Modelado en las BBDD")

st.header("Introducción a los Data Wherehouse y Sus Componentes")
st.markdown("""<div class="justificar">
                    <p>Para entender más a fondo la normalización y la denormalización es necesario entender a los Datawherehouse (o almacenes de datos) y sus distintas arquitecturas. Un almacén de datos agrega información de diversas fuentes en un repositorio central optimizado para consultas y análisis. Generalmente, utiliza procesos de extracción, transformación y carga (ETL) o extracción, carga y transformación (ELT) para limpiar , preparar y organizar los datos para inteligencia empresarial (BI) y otros casos de uso de análisis de datos.<br><br>
                    Los almacenes de datos están configurados y optimizados para análisis casi en tiempo real, lo que significa que, por lo general, no son ideales para almacenar grandes cantidades de datos masivos sin procesar y no estructurados . A medida que aumenta la cantidad de datos en un almacén, también aumentan el costo y la complejidad del almacenamiento. Además, pueden surgir problemas de latencia y rendimiento.</p>
                    </div>""", unsafe_allow_html=True)

with st.expander("**📌 ESQUEMA**"):
    data1, data2, data3 = st.columns([1, 2, 1])
    with data2:
        st.image("Imagenes/Datawherehouse.jpg", width= 600)

st.subheader("📝 Componentes de la Arquitectura de un Almacén de Datos:")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""<div class="contenedor-lista">
                    <b class="destacar">1.✏️ Fuentes de Datos</b><br>
                    Un almacén de datos recopila información de diversas fuentes, incluidos datos estructurados de bases de datos relacionales y datos no estructurados como registros o archivos de texto. 
                    </div>""", unsafe_allow_html=True)
    st.markdown("""<div class="contenedor-lista">
                    <b class="destacar">4.✏️ Almacenamiento de Datos</b><br>
                    En el núcleo del almacén de datos se encuentra la capa de almacenamiento, donde los datos se organizan en tablas de hechos y dimensiones. Estos suelen estar compuestos por DataMarts (pequeños almacenes).
                    </div>""", unsafe_allow_html=True)
with col2:
    st.markdown("""<div class="contenedor-lista">
                    <b class="destacar">2.✏️ ETL o ELT</b><br>
                    En el ETL se extraen datos de los sistemas de origen, los transforman en un área de preparación y los cargan en el almacén de datos. En ELT, los datos se transforman después de haber sido cargados en el almacén. 
                    </div>""", unsafe_allow_html=True)
    st.markdown("""<div class="contenedor-lista">
                    <b class="destacar">5.✏️ Metadatos</b><br>
                    La capa de metadatos gestiona y mantiene la estructura y las relaciones dentro del almacén de datos. Los metadatos nos proporcionan información sobre las fuentes de datos, el esquema y las transformaciones. 
                    </div>""", unsafe_allow_html=True)
with col3:
    st.markdown("""<div class="contenedor-lista">
                    <b class="destacar">3.✏️ Área de Preparación</b><br>
                    El área de preparación es un espacio de almacenamiento temporal y opcional donde se guardan los datos sin procesar antes de ser procesados ​y cargados en el almacén de datos.
                    </div>""", unsafe_allow_html=True)
    st.markdown("""<div class="contenedor-lista">
                    <b class="destacar">6.✏️ Acceso y Análisis de Datos</b><br>
                    Los usuarios empresariales y los analistas de datos pueden utilizar paneles, aplicaciones y herramientas de visualización de datos  para interactuar con ellos y extraer información valiosa.
                    </div>""", unsafe_allow_html=True)

st.write(" ")
st.subheader("📦 ¿Qué es un Data Mart?:")
st.markdown("""<div class="justificar">
                    <p>Un data mart es una base de datos enfocada en un área o departamento específico de una organización (como Ventas, Finanzas o Recursos Humanos) diseñada para facilitar el análisis de datos de forma rápida. A diferencia de un almacén de datos (Data Warehouse), que centraliza toda la información de la empresa, el data mart es un subconjunto de datos optimizado para las necesidades de un grupo concreto de usuarios.<br><br>
                    Los data marts crean conjuntos de datos adaptados a objetivos y escenarios específicos ayuda a mejorar la inteligencia empresarial y el análisis. Los equipos y departamentos pueden extraer conocimientos más eficientemente, lo que lleva a procesos empresariales más rápidos y operaciones optimizadas. </p>
                    </div>""", unsafe_allow_html=True)

st.header("⛓ Arquitecturas de Inmon y Kimball")
st.markdown("""<div class="justificar">
                    <p>El almacenamiento de datos es un componente fundamental de la ingeniería de datos moderna, ya que permite a las organizaciones almacenar, gestionar y analizar grandes volúmenes de datos, por lo tanto, el enfoque sobre el cual se apoya su arquitectura afecta directamente estas cualidades. Dos enfoques destacados para la arquitectura de almacenes de datos son los propuestos por Bill Inmon y Ralph Kimball:</p>
                    </div>""", unsafe_allow_html=True)

with st.expander("📌 **ESQUEMAS**"):
    esq1, esq2, esq3 = st.columns([1, 2, 1])
    with esq2:
        st.image("Imagenes/inmonvskimball.png", width= 600)

arq1, arq2 = st.columns(2)
with arq1:
    st.subheader("🏠 Arquitectura de Inmon:")
    with st.container(border=True):
         st.markdown('''<p class="justificar">
                     <b class="destacar">ENFOQUE</b><br>
                     El enfoque de Inmon es un método de arriba hacia abajo (top-down) que propone construir primero un único almacén de datos centralizado para toda la empresa. En este modelo, la información se organiza de forma altamente estructurada y normalizada (en 3FN), lo que elimina la repetición de datos .
                    </p>''',  unsafe_allow_html=True)
    st.subheader("Ventajas / Desventajas",text_alignment="center")
    Inmon1, Inmon2 = st.columns(2, border=True)
    with Inmon1:
        st.markdown("""<div class="justificar">
                        <spam class="destacar">🔋 Integridad de los datos:</spam>
                        <p>La normalización de los datos reduce la redundancia y garantiza la coherencia de los mismos. </p>
                        <spam class="destacar">🔋 Modelo de datos integral:</spam>
                        <p>Al centralizar los datos en un solo lugar, se eliminan las contradicciones entre áreas.</p>
                        <spam class="destacar">🔋 Escalabilidad:</spam>
                        <p>Su estructura centralizada permite procesar cantidades masivas de información y responder a preguntas de negocio muy difíciles.</p>
                        </div>""", unsafe_allow_html=True)
    with Inmon2:
            st.markdown("""<div class="justificar">
                        <spam class="destacar">🪫 Consumo de tiempo:</spam>
                        <p>Requiere una cantidad considerable de tiempo y recursos para su diseño e implementación. </p>
                        <spam class="destacar">🪫 Complejidad:</spam>
                        <p>Gestionar y mantener un almacén de datos normalizado puede resultar complejo. </p>
                        <spam class="destacar">🪫 Menor rendimiento</spam>
                        <p>Los datos normalizados pueden provocar un rendimiento más lento en las consultas en comparación con las estructuras desnormalizadas.  </p>
                        </div>""", unsafe_allow_html=True)
    with st.expander("📌 **¿Cuando Usar?:**"):
        st.markdown("""<div class="justificar">
                    <p>Se elige la arquitectura de Inmon si trabajas en una gran corporación que exige una única versión de la verdad, consistencia global y un control de auditoría estricto a largo plazo. Este enfoque es necesario cuando se deben integrar masivas y complejas fuentes de datos heterogéneas en un repositorio central completamente normalizado (3NF), aceptando un costo inicial más alto y tiempos de desarrollo prolongados a cambio de un mantenimiento corporativo robusto y estructurado. </p>
                    </div>""", unsafe_allow_html=True)  
with arq2:
    st.subheader("🏠 Arquitectura de Kimball:")
    with st.container(border=True):
         st.markdown('''<p class="justificar">
                   <b class="destacar">ENFOQUE</b><br>
                   El enfoque de Kimball es un método de abajo hacia arriba (bottom-up) que prioriza las necesidades urgentes del negocio creando directamente esos Data Marts departamentales. Estos almacenes se diseñan con un modelo dimensional que resulta muy fácil de entender y usar por los analistas y las herramientas de reportes.
                   </p>''',  unsafe_allow_html=True)
    st.subheader("Ventajas / Desventajas",text_alignment="center")
    kim1, kim2 = st.columns(2, border=True)
    with kim1:
        st.markdown("""<div class="justificar">
                        <spam class="destacar">🔋 Implementación rápida:</spam>
                        <p>Los almacenes de datos se pueden implementar rápidamente para satisfacer las necesidades inmediatas del negocio.  </p>
                        <spam class="destacar">🔋 Fácil de usar:</spam>
                        <p>El diseño del esquema en estrella es intuitivo y fácil de entender y consultar para los usuarios finales.  </p>
                        <spam class="destacar">🔋 Flexibilidad:</spam>
                        <p>Permite adaptar y ampliar el almacén de datos con mayor facilidad a medida que surgen nuevos requisitos.  </p>
                        </div>""", unsafe_allow_html=True)
    with kim2:
            st.markdown("""<div class="justificar">
                        <spam class="destacar">🪫 Redundancia de datos:</spam>
                        <p>Los datos desnormalizados pueden generar redundancia y aumentar los requisitos de almacenamiento.  </p>
                        <spam class="destacar">🪫 Inconsistencias:</spam>
                        <p>Existe la posibilidad de que se produzcan inconsistencias entre los almacenes de datos si no se gestionan adecuadamente.  </p>
                        <spam class="destacar">🪫 Desafíos de integración:</spam>
                        <p>Integrar almacenes de datos para formar un almacén de datos coherente puede resultar complicado.   </p>
                        </div>""", unsafe_allow_html=True)
    with st.expander("📌 **¿Cuando Usar?:**"):
        st.markdown("""<div class="justificar">
                    <p>Se usa la arquitectura de Kimball cuando necesites resultados rápidos, cuentes con un presupuesto limitado y el objetivo principal sea facilitar el análisis directo a los usuarios mediante paneles de BI o consultas SQL sencillas. Es ideal para proyectos enfocados en procesos de negocio específicos (como ventas o inventario), ya que construye la solución de manera modular mediante almacenes de datos descentralizados (Data Marts) que se integran rápidamente sin requerir una gran infraestructura inicial. </p>
                    </div>""", unsafe_allow_html=True)

st.header("Modelado Dimensional de Kimball")
st.markdown("""<div class="justificar">
                    <p>El modelado dimensional es una técnica de diseño de bases de datos utilizada para estructurar almacenes de datos (Data Warehouses) y Data Marts, cuyo objetivo principal es optimizar la velocidad de las consultas analíticas y hacer que los datos sean fáciles de entender por los usuarios de negocio.<br><br>
                    A diferencia del modelado relacional tradicional (que normaliza las tablas para evitar redundancias), el modelado dimensional desnormaliza los datos a propósito. Su estructura se basa en dos tipos de tablas organizadas en esquemas de Estrella o Copo de Nieve. </p>
                    </div>""", unsafe_allow_html=True)

mo1, mo2 = st.columns(2)
with mo1:
    st.subheader("💫 :red[Tabla de Dimensiones]")
    st.markdown("""<div class="justificar">
                    <p>Rodean a la tabla de hechos. Contienen los atributos cualitativos que dan contexto a las métricas (el "quién, qué, dónde, cuándo y por qué"). Ejemplos comunes son las dimensiones de Cliente, Tiempo, Producto o Ubicación. </p>
                    </div>""", unsafe_allow_html=True)
    with st.expander("📌 **Características**"):
        st.markdown("""<div class="justificar">
                                <spam class="destacar">✅ Contienen Atributos Textuales:</spam>
                                <p> Almacenan descripciones cualitativas que responden al quién, qué, dónde, cuándo y por qué. </p>
                                <spam class="destacar">✅ Clave Primaria Única:</spam>
                                <p> Poseen una clave primaria simple (normalmente una clave subrogada o surrogate key autoincremental) para conectarse con la tabla de hechos.  </p>
                                <spam class="destacar">✅ Crecimiento Horizontal Alto:</spam>
                                <p> Son tablas anchas y cortas (muchas columnas descriptivas, pero significativamente menos filas que la tabla de hechos).  </p>
                                <spam class="destacar">✅ Estructura Jerárquica:</spam>
                                <p> Organizan la información en niveles lógicos de consulta, como una dimensión de tiempo que incluye Año > Trimestre > Mes > Día.  </p>                                                                
                                </div>""", unsafe_allow_html=True)  
with mo2:
    st.subheader("💫 :red[Tabla de Hechos]")
    st.markdown("""<div class="justificar">
                    <p>Son el centro del modelo. Contienen las métricas cuantitativas o medidas numéricas de un proceso de negocio (como montos de ventas, cantidades de productos vendidos o costos) y las claves foráneas que las conectan con las dimensiones. </p>
                    </div>""", unsafe_allow_html=True)
    with st.expander("📌 **Características**"):
        st.markdown("""<div class="justificar">
                                <spam class="destacar">✅ Contienen Métricas Numéricas:</spam>
                                <p>Almacenan valores cuantitativos continuamente medibles. Estas se actualizan con mayor frecuencia. </p>
                                <spam class="destacar">✅ Claves Horáneas Compuestas:</spam>
                                <p>Su clave primaria suele ser una combinación de claves foráneas (FK) que apuntan a las tablas de dimensiones que la rodean.  </p>
                                <spam class="destacar">✅ Crecimiento Vertical Rápido:</spam>
                                <p>Son tablas sumamente largas y estrechas (pocas columnas, pero millones o miles de millones de filas). </p>
                                <spam class="destacar">✅ Nivel de Granularidad Fijo:</spam>
                                <p>Cada fila representa un evento específico en un punto exacto en el tiempo. Debe ser el nivel más básico posible donde el dato que no se pueda dividir más. </p>                                
                                </div>""", unsafe_allow_html=True)   

st.subheader("🧩 Ventajas del Modelo Dimensional:")

ven1, ven2, ven3 = st.columns(3)
with ven1:
    st.markdown("""<div class="contenedor-lista">
                    <b class="destacar">🎯 Fácil comprensión para el negocio</b><br>
                    La estructura refleja de forma intuitiva cómo piensan los usuarios de la empresa, organizando los datos en métricas (hechos) y contextos (dimensiones).
                    </div>""", unsafe_allow_html=True)
with ven2:
    st.markdown("""<div class="contenedor-lista">
                    <b class="destacar">🎯 Integración con herramientas de BI</b><br>
                    Optimiza de forma nativa la conexión con plataformas de visualización de datos como Power BI, Tableau o Looker Studio.
                    </div>""", unsafe_allow_html=True)
with ven3:
    st.markdown("""<div class="contenedor-lista">
                    <b class="destacar">🎯 Diseño altamente modular</b><br>
                    Permite añadir nuevas dimensiones o tablas de hechos al modelo existente sin necesidad de reestructurar las tablas que ya están en producción.
                    </div>""", unsafe_allow_html=True)

st.header("Esquemas del Modelo Dimensional")
st.markdown("""<div class="justificar">
                    <p>Existen numerosos patrones de diseño para almacenes de datos, pero cada uno se adapta a necesidades diferentes según la complejidad de los datos y los tipos de consultas que se ejecutan. Exploremos algunos de los más comunes y analicemos los escenarios más adecuados para utilizarlos con la máxima eficiencia.  </p>
                    </div>""", unsafe_allow_html=True)

with st.expander("📌 :red[**ESQUEMAS**]"):
    mode1, mode2, mode3 = st.columns([1, 2, 1])
    with mode2:
        st.image("Imagenes/Esquemas.jpg", width= 600)

mod1, mod2 = st.columns(2)
with mod1:
    st.subheader("⭐️ **Esquema Estrella:**")
    st.markdown("""<div class="justificar">
                    <p>Los esquemas en estrella constan de una única tabla de hechos central rodeada de tablas de dimensiones. En un diagrama, la tabla de hechos aparece en el centro de la estructura en forma de estrella. El esquema en estrella se considera el tipo de esquema más simple y común, ya que ofrece a los usuarios una mayor velocidad de consulta. </p>
                    </div>""", unsafe_allow_html=True)
    with st.expander("💡 :red[**Características**]"):
                    st.markdown("""<div class="justificar">
                                <spam class="destacar">🧩 Dimensiones Desnormalizadas:</spam>
                                <p> Las tablas de dimensiones no se dividen; guardan toda la información cualitativa y sus jerarquías en una sola tabla ancha. </p>
                                <spam class="destacar">🧩 Estructura Simple:</spam>
                                <p> La tabla de hechos se ubica en el centro y se conecta directamente con cada dimensión mediante una sola unión (join). </p>
                                <spam class="destacar">🧩 Máxima Velocidad de Consulta:</spam>
                                <p> Al requerir muy pocas uniones entre tablas para extraer la información, ofrece el mejor rendimiento en bases de datos analíticas.  </p>
                                <spam class="destacar">🧩 Más Consumo de Almacenamiento:</spam>
                                <p> Al repetir textos y descripciones en las filas de las dimensiones, requiere más espacio en disco.  </p>
                                </div>""", unsafe_allow_html=True) 
    with st.expander("🔎 :red[**Cuando Usar:**]"):
                    st.markdown("""<div class="justificar">
                            <p>Se usa el Modelo Estrella cuando tu prioridad absoluta sea la velocidad de las consultas analíticas, la simplicidad del diseño y la facilidad de uso para los analistas de negocio a través de herramientas de BI. Es la opción ideal cuando trabajas con motores de bases de datos modernos en la nube (como BigQuery, Snowflake o Redshift) que manejan de forma masiva el almacenamiento desnormalizado, o cuando el volumen de tus tablas de dimensiones es relativamente pequeño y no justifica la complejidad de fragmentar los datos descriptivos.</p>
                            </div>""", unsafe_allow_html=True)
with mod2:
    st.subheader("❄️ **Esquema Copo de Nieve:**")
    st.markdown("""<div class="justificar">
                            <p>Un esquema de copo de nieve sitúa una tabla de hechos central en el núcleo, con numerosas tablas de dimensiones hacia afuera otras tablas de dimensiones mediante relaciones de muchos a uno. Los esquemas de copo de nieve presentan bajos niveles de redundancia de datos, pero esta ventaja conlleva un menor rendimiento en las consultas. </p>
                            </div>""", unsafe_allow_html=True)
    with st.expander("💡 :red[**Características**]"):
                    st.markdown("""<div class="justificar">
                                <spam class="destacar">🧩 Dimensiones Normalizadas:</spam>
                                <p> Las tablas de dimensiones se dividen en subtablas para eliminar la redundancia de datos. </p>
                                <spam class="destacar">🧩 Estructura Compleja:</spam>
                                <p> Las dimensiones secundarias no se conectan directamente a la tabla de hechos central, lo que genera un diseño visual expandido similar a un copo de nieve.  </p>
                                <spam class="destacar">🧩 Consultas Más Lentas:</spam>
                                <p> Para armar un reporte, la base de datos debe realizar múltiples uniones (joins) en cadena, lo que incrementa el esfuerzo de procesamiento y reduce el rendimiento.  </p>
                                <spam class="destacar">🧩 Ahorro de Almacenamiento:</spam>
                                <p> Al estar normalizado en Tercera Forma Normal (3NF), elimina la duplicación de cadenas de texto y optimiza el uso del disco.  </p>
                                </div>""", unsafe_allow_html=True)                                               
    with st.expander("🔎 :red[**Cuando Usar:**]"):
                    st.markdown("""<div class="justificar">
                            <p>Se elige el Modelo Copo de Nieve cuando utilices bases de datos relacionales tradicionales (como PostgreSQL o SQL Server) y necesites optimizar al máximo el espacio en disco minimizando la redundancia de texto. Este enfoque es el adecuado cuando tus tablas de dimensiones contienen millones de filas con jerarquías complejas y cambiantes que requieren un mantenimiento centralizado, o cuando los datos origen ya vienen normalizados de un sistema y prefieres mantener esa misma estructura para facilitar los procesos de carga de datos (ETL). </p>
                            </div>""", unsafe_allow_html=True)

utils.cambio_pag(ant="Indice/TEMA 01/00_Normalizacion.py", sig="Indice/TEMA 01/02_Denormalizacion.py")