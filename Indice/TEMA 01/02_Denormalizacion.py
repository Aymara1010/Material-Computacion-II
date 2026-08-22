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
    </style>
    """, unsafe_allow_html=True)

st.title("🔑 Denormalización")

st.header("¿Qué es la Denormalización en Bases de Datos?")
st.markdown("""<div class="justificar">
                <p>Ya hemos abarcado las múltiples ventajas y desventajas que de la normalización, pero, ¿Qué pasa cuando la normalización trae más problemas que soluciones? Ahí es cuando entra la denormalización.<br><br>
                La denormalización es el acto deliberado de añadir datos redundantes a un esquema previamente normalizado para acelerar las lecturas y simplificar las consultas. Se trata de una optimización del rendimiento específica.
                Si eres bastante nuevo en el diseño de bases de datos, conviene analizar el significado de «normalizado», «desnormalizado» y «no normalizado». Estos tres términos se utilizan con bastante frecuencia y es importante no confundirlos.<br><br>
                🧩 <b class="destacar">Normalizado:</b> Los datos se dividen en tablas bien estructuradas que minimizan la redundancia y protegen la integrida.<br>
                🧩 <b class="destacar">Desnormalizado:</b> Reintroduce redundancia selectiva a través de distintas técnicas, además de ese modelo normalizado, para acelerar las lecturas comunes.<br>
                🧩 <b class="destacar">Sin normalizar:</b> Datos sin procesar, o desordenados, cuya estructura y restricciones nunca se diseñaron adecuadamente. Eso no es lo que estamos haciendo aquí. </p>
                </div>""", unsafe_allow_html=True)

st.subheader("📢 Por qué y Cuándo Denormalizar:")
st.markdown("""<div class="justificar">
                <p>Realmente conviene utilizar la desnormalización cuando te proporciona la mayor velocidad de lectura con la menor carga operativa adicional, y solo después de haber descartado soluciones más económicas.<br><br>
                La desnormalización resulta realmente útil cuando los usuarios reales y las consultas reales se ven bloqueados por uniones, agregaciones o búsquedas repetidas. Una vez que hayas confirmado que la indexación, el ajuste de consultas y el almacenamiento en caché no son suficientes, es posible que desees recurrir a la desnormalización para optimizar la velocidad de lectura en patrones de acceso predecibles.</p>
                </div>""", unsafe_allow_html=True)

ra1, ra2 = st.columns(2)
with ra1:
    with st.container(border=True):
        st.markdown('''<b class="destacar">🎯 Informes de BI:</b><br>
                    Usan la desnormalización porque calcular millones de filas en tiempo real vuelve los reportes muy lentos. Al guardar los datos ya sumados y agrupados, los ejecutivos pueden ver gráficos y tomar decisiones de forma inmediata y efeciente sin sobrecargar el servidor.
                   ''',  unsafe_allow_html=True)    
    with st.container(border=True):
        st.markdown('''<b class="destacar">🎯 Contadores:</b><br>
                    La aplican porque millones de usuarios ven un perfil al mismo tiempo y contar sus "me gusta" desde cero en cada visita colapsaría la base de datos. Guardar el número final directamente permite que las redes sociales muestren la información al instante con un consumo mínimo de recursos.
                   ''',  unsafe_allow_html=True)
with ra2:
    with st.container(border=True):
        st.markdown('''<b class="destacar">🎯 Análisis de eventos a gran escala:</b><br>
                   La necesitan porque las consultas tradicionales con uniones de tablas fallan cuando se manejan miles de millones de registros. Aplanar los datos en filas anchas permite que las bases de datos modernas escaneen la información en un orden predecible y a máxima velocidad.
                   ''',  unsafe_allow_html=True)    
    with st.container(border=True):
        st.markdown('''<b class="destacar">🎯 Catálogo y páginas de búsqueda:</b><br>
                    La implementan porque los compradores abandonan las tiendas online si las búsquedas tardan más de un segundo. Duplicar datos clave como marcas o precios finales evita hacer cruces de tablas complejos, logrando que los filtros y las páginas carguen de forma instantánea.
                   ''',  unsafe_allow_html=True)

st.header("✒️ Ventajas y Desventajas de la Denormalización:")
st.markdown("""<div class="justificar">
                <p>La desnormalización es una estrategia que rompe las reglas tradicionales de organización de datos para introducir duplicación de información de forma inteligente y controlada. No se trata de un error de diseño, sino de un intercambio estratégico: se sacrifica el espacio de almacenamiento y la facilidad de actualizar datos con el único fin de conseguir una velocidad de respuesta extrema en sistemas de reportes y análisis.<br><br>
                A continuación, te presento el balance detallado de los beneficios y problemas que genera esta técnica: </p>
                </div>""", unsafe_allow_html=True)

ven1, des2 = st.columns(2)
with ven1:
    with st.expander(":red[**🔋 VENTAJAS:**]", expanded=True):
                st.markdown("""<div class="justificar">
                        <spam class="destacar">🔓 Estructura Ideal para BI:</spam>
                        <p> Encaja de forma nativa con el diseño de esquemas en estrella, maximizando el rendimiento de herramientas como Power BI o Tableau.  </p>
                        <spam class="destacar">🔓 Simplificación de Consultas SQL:</spam>
                        <p> Las consultas se vuelven mucho más cortas y fáciles de escribir para los analistas de negocio, ya que no requieren conectar múltiples tablas. </p>
                        <spam class="destacar">🔓 Consultas Ultrarrápidas:</spam>
                        <p> Al unificar los datos relacionados en una sola tabla, la base de datos lee menos archivos físicos y responde en una fracción de tiempo. </p>
                        </div>""", unsafe_allow_html=True)
with des2:
    with st.expander(":red[**🪫 DESVENTAJAS:**]", expanded=True):
                st.markdown("""<div class="justificar">
                        <spam class="destacar">🔐 Anomalías e Inconsistencias de Datos:</spam>
                        <p> Al duplicar la información, se corre el riesgo de que un dato se actualice en un lugar pero se olvide en otro, provocando anomalías e inconsistencias de datos. </p>
                        <spam class="destacar">🔐 Procesos de Actualización más Lentos:</spam>
                        <p> Las operaciones de insertar, actualizar y eliminar se vuelven complejas y lentas, ya que la base de datos debe modificar múltiples filas replicadas para mantener la coherencia.</p>
                        <spam class="destacar">🔐 Mayor Consumo de Almacenamiento:</spam>
                        <p> Repetir cadenas de texto, nombres y descripciones a lo largo de millones de filas incrementa considerablemente el tamaño físico de la base de datos en disco.</p>
                        </div>""", unsafe_allow_html=True)
                
st.header("🔑 4 Pasos de Kimball:")
st.markdown("""<div class="justificar">
                <p>El modelado dimensional de Kimball sigue un proceso de cuatro pasos: selección de un proceso de negocio, identificación del nivel de detalle, definición de dimensiones e identificación de hechos. El modelo dimensional resultante estructura los datos en tablas de hechos y dimensiones que permiten consultas rápidas, informes intuitivos y análisis escalables, lo que lo convierte en uno de los enfoques más utilizados para las soluciones modernas de almacenamiento de datos e inteligencia empresarial. </p>
                </div>""", unsafe_allow_html=True)
st.markdown("""<div class="justificar">
                <p> La desnormalización no se aplica al azar, sino que se ejecuta de forma ordenada a través de cada una de estas etapas de diseño. Los cuatro pasos son la guía estructurada para saber qué datos desnormalizar, en qué medida y dónde colocarlos sin perder el control de la información.</p>
                </div>""", unsafe_allow_html=True)
st.write(" ")
pas1, pas2, pas3, pas4 = st.columns(4)
with pas1:
        st.markdown("""<div class="contenedor">
                <h4 class="destacar">💡 Paso 1: Proceso Organizacional</h4>
                <p class="justificar">Selecciona un proceso de negocio para modelar. El enfoque de Kimball comienza con un proceso de negocio, ya que, en última instancia, los usuarios querrán hacer preguntas sobre los procesos. Esto contrasta con metodologías de modelado anteriores, como la de Bill Inmon, que partían de las entidades de negocio (por ejemplo, el modelo de cliente, el modelo de producto, etc.). Podemos comparar este paso con el universo estadístico. </p>
                </div>""", unsafe_allow_html=True)
with pas2:
        st.markdown("""<div class="contenedor">
                <h4 class="destacar">💡 Paso 2: Declarar Granularidad</h4>
                <p class="justificar">Decide el nivel de detalle . Aquí, el nivel de detalle se refiere al nivel de datos que se almacenará como tabla de hechos principal. Debe ser el nivel más básico posible, es decir, un nivel de datos que no se pueda dividir más. Por ejemplo, en nuestro ejemplo de punto de venta anterior, el nivel de detalle debería ser el de los artículos dentro de cada pedido, en lugar del pedido en sí. Podemos asociar este paso con la unidad estadística.  </p>
                </div>""", unsafe_allow_html=True)
with pas3:
        st.markdown("""<div class="contenedor">
                <h4 class="destacar">💡 Paso 3: Identificar Dimensiones</h4>
                <p class="justificar">Selecciona las dimensiones que se aplican a cada fila de la tabla de hechos. Esto suele ser bastante sencillo si ha definido correctamente los parámetros. Las dimensiones surgen de la pregunta "¿cómo describen los profesionales los datos que resultan del proceso empresarial?". Deberá incorporar a las tablas de hechos un conjunto sólido de dimensiones que representen todas las descripciones posibles. </p>
                </div>""", unsafe_allow_html=True)
with pas4:
        st.markdown("""<div class="contenedor">
                <h4 class="destacar">💡 Paso 4: Identificar Hechos</h4>
                <p class="justificar">Identifica los datos numéricos que se incluirán en cada fila de la tabla de hechos. Los datos numéricos de la tabla de hechos surgen de la pregunta "¿qué estamos respondiendo?". Se deberá decidir cuáles son las medidas numéricas más importantes que se almacenarán en la tabla de hechos para recombinarlas posteriormente y responder a sus consultas. Los hechos deben corresponder al nivel de detalle definido en el paso 2.</p>
                </div>""", unsafe_allow_html=True)
st.write(" ")


st.header("🏮 Técnicas de Denormalización:")
st.markdown("""<div class="justificar">
                <p>Ya sabemos que la denormalización es una técnica basada en la optimización de consultas. Para lograr esto sin generar un caos de información, se aplican estrategias específicas (como los esquemas en estrella de Kimball) que agrupan los datos en tablas anchas, eliminando las uniones (joins) pesadas entre tablas y permitiendo a las herramientas de visualización consultar millones de registros en segundos.<br><br>
                Por eso, para facilitar el proceso de denormalizacion es importante tener en cuenta ciertas técnicas que nos pueden ayudar a la hora de denormalizar una base de datos.</p>
                </div>""", unsafe_allow_html=True)

tec1, tec2, tec3 = st.tabs(["**COLUMNAS**", "**TABLAS**", "**VISTAS**"])
with tec1:
    mo1, mo2 = st.columns(2)
with mo1:
    st.subheader("💫 Atributos Derivados:")
    st.markdown("""<div class="justificar">
                    <p>Consiste en calcular un dato de forma anticipada y guardar el resultado directamente en una columna de la tabla, en lugar de calcularlo en tiempo real cada vez que un usuario abre un reporte.<br>
                    <h5 class="destacar">📢 Por Ejemplo:</h5>
                    Si para obtener un valor necesitas hacer operaciones matemáticas (sumas, multiplicaciones) o aplicar lógica de texto sobre otras columnas, haces el cálculo una sola vez (por ejemplo, durante la carga de datos por la noche) y almacenas el valor final.</p>
                    </div>""", unsafe_allow_html=True)
    with st.expander("**📌 ¿Cuando Usar?**"):
        st.markdown("""<div class="justificar">
                                <spam class="destacar">🧩 Cálculos repetitivos y costosos:</spam>
                                <p>Cuando los usuarios consultan frecuentemente reportes que suman o promedian millones de filas (ej. "Ventas totales del año").</p>
                                <spam class="destacar">🧩 Uso intensivo de funciones agregadas:</spam>
                                <p>Si tus consultas usan demasiado las funciones SUM(), AVG() o fórmulas complejas que ralentizan el servidor.</p>
                                <spam class="destacar">🧩 Datos históricos congelados:</spam>
                                <p>Cuando necesitas que el valor no cambie aunque cambie la fórmula en el futuro (ej. el total de una factura del año pasado debe quedarse igual).</p>
                                </div>""", unsafe_allow_html=True)  
with mo2:
    st.subheader("💫 Duplicación de Columnas:")
    st.markdown("""<div class="justificar">
                    <p>Consiste en copiar una columna descriptiva de una tabla secundaria e inyectarla directamente en la tabla principal, rompiendo la regla de "guardar el dato en un solo lugar".<br>
                    <h5 class="destacar">📢 Por Ejemplo:</h5>
                    En lugar de tener la descripción de un producto en la tabla Productos y obligar a la base de datos a hacer un JOIN (unión) con la tabla Ventas para saber qué se vendió, copias el Nombre_Producto directamente dentro de la tabla Ventas. El dato ahora existe en dos lugares al mismo tiempo.</p>
                    </div>""", unsafe_allow_html=True)
    with st.expander("**📌 ¿Cuando Usar?**"):
        st.markdown("""<div class="justificar">
                                <spam class="destacar">🧩 Cuellos de Botella por JOINs: </spam>
                                <p>Cuando el rendimiento de tus reportes cae drásticamente debido a que necesitas unir 5, 10 o más tablas para armar una sola vista de datos.  </p>
                                <spam class="destacar">🧩 Baja Frecuencia de Actualización: </spam>
                                <p>Cuando el dato duplicado casi nunca cambia (ej. los nombres de los productos o las categorías de tecnología rara vez cambian).</p>
                                <spam class="destacar">🧩 Consultas Masivas de Filtrado:  </spam>
                                <p>Cuando los usuarios necesitan filtrar o agrupar constantemente las transacciones por un texto específico (ej. "Filtrar todas las ventas por el nombre de la región").</p>
                                </div>""", unsafe_allow_html=True)   
with tec2:
    mo3, mo4 = st.columns(2)
with mo3:
    st.subheader("✨ Tablas Preunidas:")
    st.markdown("""<div class="justificar">
                    <p>Consiste en fusionar dos o más tablas relacionadas en una sola gran tabla física, eliminando la separación lógica que existía en el modelo normalizado.<br>
                    <h5 class="destacar">📢 Por Ejemplo:</h5>
                    En lugar de mantener la clásica estructura donde una tabla apunta a otra mediante claves (por ejemplo, tener una tabla de Clientes separada de la tabla de Ciudades), ejecutas la unión (join) de forma anticipada. Al hacerlo, guardas toda la información combinada en una sola tabla ancha. </p>
                    </div>""", unsafe_allow_html=True)
    with st.expander("**📌 ¿Cuando Usar?**"):
        st.markdown("""<div class="justificar">
                                <spam class="destacar">🧩 Uniones (joins) Masivas y Frecuentes:</spam>
                                <p>Cuando tienes consultas críticas o reportes diarios que obligatoriamente deben unir tres o más tablas grandes para mostrar información básica. </p>
                                <spam class="destacar">🧩 Relaciones con Jerarquías Fijas:</spam>
                                <p> Cuando las tablas independientes representan una jerarquía clara y natural del negocio que casi nunca cambia (como País -> Estado -> Ciudad). </p>
                                <spam class="destacar">🧩 Optimización para Herramientas de BI:</spam>
                                <p>Cuando necesitas aplanar el modelo de datos para que plataformas como Power BI carguen la información de forma más eficiente y sin modelos de relaciones complejos. </p>
                                </div>""", unsafe_allow_html=True)  
with mo4:
    st.subheader("✨ Tablas de Resumen:")
    st.markdown("""<div class="justificar">
                    <p>Consiste en crear una tabla nueva que almacena datos totalmente consolidados o agregados en un nivel de detalle mucho más alto (menor granularidad) que la tabla original.<br>
                    <h5 class="destacar">📢 Por Ejemplo:</h5>
                    Si tu tabla principal registra millones de transacciones al detalle (grano fino, como cada café vendido por segundo), la tabla de resumen procesa esos datos (usando SUM, COUNT, AVG) y guarda únicamente el resultado consolidado (grano grueso, como el total de ventas por tienda y por día).</p>
                    </div>""", unsafe_allow_html=True)
    with st.expander("**📌 ¿Cuando Usar?**"):
        st.markdown("""<div class="justificar">
                                <spam class="destacar">🧩 Volúmenes de Datos Masivos:</spam>
                                <p> Cuando la tabla transaccional es tan gigantesca que calcular totales en tiempo real congela el sistema o toma varios minutos. </p>
                                <spam class="destacar">🧩 Páneles de Control Ejecutivos (Dashboards):</spam>
                                <p>Cuando los directores o gerentes solo necesitan ver tendencias macro (ej. "Ventas por mes" o "Rendimiento por año") y nunca necesitan bajar al detalle del ticket individual. </p>
                                <spam class="destacar">🧩 Consultas Repetitivas Sobre Datos Históricos:</spam>
                                <p>Cuando los datos del pasado ya no van a cambiar y no tiene sentido volver a sumar los mismos millones de filas una y otra vez cada vez que alguien abre un reporte histórico.</p>
                                </div>""", unsafe_allow_html=True) 
with tec3:
    st.subheader("🌟 Vistas Materializadas:")
    st.markdown("""<div class="justificar">
                    <p>Consiste en almacenar físicamente en el disco el resultado de una consulta SQL compleja (que puede incluir uniones, filtros y sumas) para que pueda ser leída de inmediato de forma directa.<br>
                    <h5 class="destacar">📢 Por Ejemplo:</h5>
                    A diferencia de una vista común (que es solo un atajo de código que vuelve a ejecutar la consulta desde cero cada vez que la usas), la vista materializada ejecuta la consulta una sola vez y congela el resultado en un espacio del disco. Cuando un usuario la consulta, la base de datos no calcula nada; simplemente entrega los datos guardados al instante. Posee un mecanismo automatizado que refresca o actualiza los datos guardados cada cierto tiempo.</p>
                    </div>""", unsafe_allow_html=True)
    with st.expander("**📌 ¿Cuando Usar?**"):
        st.markdown("""<div class="justificar">
                                <spam class="destacar">🧩 Datos de Origen que Cambian Poco:</spam>
                                <p>Cuando las tablas originales se actualizan de forma controlada (por ejemplo, cargas de datos nocturnas o cada pocas horas) y los usuarios no necesitan ver datos en tiempo real estricto. </p>
                                <spam class="destacar">🧩 Consultas Analíticas Idénticas y Repetitivas:</spam>
                                <p>Cuando muchos usuarios o un panel de BI abren constantemente el mismo reporte pesado que procesa fórmulas matemáticas y uniones complejas en paralelo.</p>
                                <spam class="destacar">🧩 Soporte de Actualización Automática::</spam>
                                <p>Cuando tu motor de base de datos (como Oracle, PostgreSQL, SQL Server o BigQuery) cuenta con soporte nativo para refrescar vistas materializadas de forma eficiente (incremental o programada), evitando que tú tengas que programar códigos complejos para actualizar los datos duplicados.</p>
                                </div>""", unsafe_allow_html=True) 

utils.cambio_pag(ant="Indice/TEMA 01/01_Arquitectura.py", sig="Indice/TEMA 02/00_DER.py")