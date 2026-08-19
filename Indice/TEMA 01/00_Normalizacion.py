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
    .contenedor-lista {
        background-color: #1E2023;
        padding: 15px;
        border-radius: 5px;
        border-left: 5px solid #FF4B4B;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Normalización")

st.header("¿Qué es la Normalización?")
st.markdown("""<div class="justificar">
                    <p> Cuando trabajamos con bases de datos, es común encontrar ciertas dificultades a la hora de realizar ciertas operaciones en las bases de datos, para esto existe una técnica utilizada en el diseño de bases de datos conocida como normalización.</p>
                   </div>""", unsafe_allow_html=True)

st.subheader("Definición")
st.markdown("""<div class="justificar">
                    <p> La normalización de bases de datos es un proceso de diseño que organiza los datos en estructuras de tabla específicas. Ayuda a mejorar la integridad de los datos , prevenir anomalías, minimizar la redundancia y optimizar el rendimiento de las consultas.<br><br>
                    Esta técnica optimiza las tablas en los sistemas de gestión de bases de datos (DBMS) para que cumplan con las denominadas formas normales: conjuntos de reglas que rigen la organización de los atributos dentro de una tabla. Estas reglas se basan principalmente en las relaciones entre los atributos (columnas), incluidas las claves utilizadas para identificar de forma única las filas </p>
                    </div>""", unsafe_allow_html=True)

st.subheader("¿Por Qué Normalizar?")
st.markdown("""<div class="justificar">
                    <p> Como se ha mencionado anteriormente, la normalización es una técnica muy utilizada en el diseño de bases de datos, por lo que hay que tener en cuenta las principales razones por la que es tan aplicada en esta área.</p>
                   </div>""", unsafe_allow_html=True)
nor1, nor2 = st.columns(2)
with nor1:
    st.markdown("""<div class="contenedor-lista">
                <b class="destacar">Redundancia</b><br>
                La redundancia es el asesino silencioso del rendimiento de las bases de datos. La normalización soluciona esto asegurándose de que cada dato se encuentre en un único lugar.
                </div>""", unsafe_allow_html=True)
    st.markdown("""<div class="contenedor-lista">
                <b class="destacar">Integridad</b><br>
                Las restricciones de clave externa evitan los registros huérfanos. No puedes eliminar accidentalmente a un cliente que aún tenga pedidos activos.
                </div>""", unsafe_allow_html=True)
with nor2: 
    st.markdown("""<div class="contenedor-lista">
                <b class="destacar">Escalabilidad </b><br>
                las tablas normalizadas son más pequeñas y están más centradas. Los índices funcionan mejor en tablas más pequeñas. Puedes particionar los datos de forma lógica sin duplicar la información entre fragmentos.
                </div>""", unsafe_allow_html=True)
    st.markdown("""<div class="contenedor-lista">
                <b class="destacar">Seguridad</b><br>
                La seguridad es más fácil de gestionar en bases de datos normalizadas. Permite controlar el acceso a nivel de tabla con confianza. 
                </div>""", unsafe_allow_html=True)
    
st.subheader("Ventajas y desventajas de la normalización")
st.markdown("""<div class="justificar">
                    <p>La normalización no es una solución milagrosa: resuelve problemas importantes, pero crea nuevos retos, principalmente en torno a la complejidad de las consultas SQL. Por eso es vital tener en cuenta las ventajas y desventajas que esta técnica puede acarrear.  </p>
                    </div>""", unsafe_allow_html=True)



ven1, des2 = st.columns(2)
with ven1:
    with st.expander("Ventajas",expanded=True):
            st.markdown("""<div class="justificar">
                        <spam class="destacar">Redundancia reducida:</spam>
                        <p>significa que tu base de datos almacena cada dato exactamente una vez, lo que reduce los costes de almacenamiento y elimina los problemas de sincronización.  </p>
                        <spam class="destacar">Coherencia de los datos:</spam>
                        <p>Tu aplicación no puede mostrar información contradictoria porque, en primer lugar, no puede existir información contradictoria.</p>
                        <spam class="destacar">Actualizaciones rápidas:</spam>
                        <p>porque cambias una fila en lugar de docenas. Introduce un nuevo cliente una sola vez y haz referencia a él en cualquier otro lugar con claves externas.  </p>
                        </div>""", unsafe_allow_html=True)
with des2:
    with st.expander("Desventajas",expanded=True):
            st.markdown("""<div class="justificar">
                        <spam class="destacar">Consultas Complejas</spam>
                        <p>En una base de datos normalizada, se requiere unir multiples tablas, más uniones significa una ejecución más lenta de las consultas.  </p>
                        <spam class="destacar">Bajo rendimiento</spam>
                        <p> Cuando se unen tablas constantemente en lugar de leer desde tablas únicas y amplias. Cada unión añade sobrecarga,. </p>
                        <spam class="destacar">Más tiempo de desarrollo:</spam>
                        <p> los programadores necesitan comprender las relaciones entre las tablas antes de escribir las consultas. </p>
                        </div>""", unsafe_allow_html=True)

st.header("Formas Normales")
st.markdown("""<div class="justificar">
                <p>La normalización de modelos de datos implica diseñar tablas que se ajusten a uno o más niveles de normalización, también conocidos como formas normales.
                Las formas normales de una base de datos son criterios específicos que ayudan a estructurar la información de manera que se minimicen las redundancias y se maximice la integridad de los datos. Cada forma normal representa un nivel de optimización mayor, partiendo desde la Primera Forma Normal (1FN) hasta la Tercera Forma Normal (3FN). A continuación, veremos cada una de estas formas en detalle.<br></p>
                </div>""", unsafe_allow_html=True)

fn1, fn2, fn3 = st.columns(3)
with fn1:
    st.markdown("""<div class="contenedor">
                <h4 class="destacar"> Primera Forma Normal - 1FN</h4>
                <p class="justificar">el criterio de normalización de bases de datos más básico, exige que el esquema de una tabla incluya una clave primaria y excluya la repetición entre columnas. Más concretamente, una tabla en primera forma normal no debe tener campos con matrices de valores ni grupos repetidos, que son columnas distintas que almacenan el mismo tipo de datos.</p>
                </div>""", unsafe_allow_html=True)
with fn2:
    st.markdown("""<div class="contenedor">
                <h4 class="destacar"> Segunda Forma Normal - 2FN</h4>
                <p class="justificar">En la segunda forma normal, ningún atributo que no sea clave tiene una dependencia parcial de la clave primaria de la tabla. En otras palabras, si una clave primaria es una clave compuesta, el atributo que no sea clave debe depender de cada columna de dicha clave compuesta. Por lo tanto, para satisfacer la 2FN debe cumplir con esta condición y la 1FN.</p>
                </div>""", unsafe_allow_html=True)
with fn3:
    st.markdown("""<div class="contenedor">
                <h4 class="destacar"> Tercera Forma Normal - 3FN</h4>
                <p class="justificar">Una tabla en tercera forma normal satisface tanto la 1FN como la 2FN, evitando además situaciones en las que los atributos no clave dependen de otros atributos no clave en lugar de las claves primarias. Cuando los atributos no clave dependen de otros atributos no clave, se habla de dependencia transitiva, lo que constituye una violación de la tercera forma normal.</p>
                </div>""", unsafe_allow_html=True)

st.header("Conceptos Clave Para la Normalización")
st.markdown("""<div class="justificar">
                <p>Para poder normalizar correctamente una base de datos, es vital comprender algunos conceptos que nos pueden ayudar a aplicar con facilidad cada una de las formas normales. Entender conceptos como lo son las claves, dependencias o cardinalidad te serán de ayuda al momento de aplicr sta técnica.</p>
                </div>""", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["CLAVES", "DEPENDENCIAS", "RELACIONES"])

with tab1:
    st.subheader("Claves")
    st.markdown("""<div class="justificar">
                <p>Ya hemos explorado anteriormente el concepto de las claves primarias y fóraneas. Las claves son la base del diseño de bases de datos relacionales: identifican registros y conectan tablas entre sí.
                En normalización, las  claves primarias juegan un papel importante en la primera y segúnda forma normal, por lo que es importante identificar las claves primarias simples y compuestas para facilitar el proceso.</p>
                </div>""", unsafe_allow_html=True)
    clav1, clav2 = st.columns(2)
    with clav1:
       with st.container(border=True):
         st.markdown('''<b class="destacar">SIMPLE</b><br>
                   Claves primarias formadas por un único campo o columna. Son las más sencillas de tratar, no suelen dar muchos problemas y es sencillo identificarlas.
                   ''',  unsafe_allow_html=True)
    with clav2:
       with st.container(border=True):
         st.markdown('''<b class="destacar">COMPUESTA</b><br>
                   Claves primarias formadas por la combinación de dos o más campos. Pueden acarrear problemas con la atomicidad de los datos y es más fácil ver dependencias parciales.
                   ''',  unsafe_allow_html=True)
with tab2:
   st.subheader("Dependencias")
   st.markdown("""<div class="justificar">
                <p>Varias restricciones de normalización de bases de datos se basan en las relaciones (también conocidas como dependencias) entre las claves primarias y las columnas que no son ni claves primarias ni candidatas. Estas últimas se conocen como atributos no clave o atributos no primarios. </p>
                </div>""", unsafe_allow_html=True)
   dep1, dep2, dep3 = st.columns(3)
   with dep1:
      with st.container(border=True):
         st.markdown('''<b class="destacar">FUNCIONAL</b><br>
                    Un campo depende por completo de una clave primaria (incluso si es compuesta), necesitando de todos sus elementos para ser identificado.
                   ''',  unsafe_allow_html=True)
   with dep2:
      with st.container(border=True):
         st.markdown('''<b class="destacar">TRANSITIVA</b><br>
                   Un campo depende de manera indirecta de otro a través de un tercero que no es una clave principal. La 3FN no acepta este tipo de dependencias.
                   ''',  unsafe_allow_html=True)
   with dep3:
      with st.container(border=True):
         st.markdown('''<b class="destacar">PARCIAL</b><br>
                    Un campo depende solo de una parte de una clave compuesta, lo que rompe la segunda forma normal y causa duplicación de datos.
                   ''',  unsafe_allow_html=True)
with tab3:
   st.subheader("Cardinalidad")
   st.markdown("""<div class="justificar">
                <p>la cardinalidad es la restricción estructural que define la existencia de dependencias (funcionales o multivaluadas) y determina los límites correctos de las tablas. No se ve simplemente como una regla de negocio, sino como el factor matemático que dicta qué atributos pueden convivir en la misma tabla sin generar redundancia. En la normalización, identificar el tipo de cardinalidad puede ser útil, cuando hay una relación de muchos a muchos se suele crear una tabla intermedia para disminuir la redundancia.</p>
                </div>""", unsafe_allow_html=True)
   re1, re2, re3 = st.columns(3)
   with re1:
      with st.container(border=True):
         st.markdown('''<b class="destacar">UNO A UNO</b><br>
                   Cada registro de la Tabla A se relaciona con un único registro de la Tabla B.
                   ''',  unsafe_allow_html=True)
   with re2:
      with st.container(border=True):
         st.markdown('''<b class="destacar">UNO A MUCHOS</b><br>
                   Un registro de la Tabla A se puede asociar con varios registros de la Tabla B.
                   ''',  unsafe_allow_html=True)
   with re3:
      with st.container(border=True):
         st.markdown('''<b class="destacar">MUCHOS A MUCHOS</b><br>
                   Múltiples registros de la Tabla A se pueden asociar con múltiples registros de la Tabla B.
                   ''',  unsafe_allow_html=True)

st.header("¿Por Qué es Importante la Normalización?")
st.markdown("""<div class="justificar">
                <p>En esencia, la normalización de bases de datos ayuda a las empresas e instituciones a organizar, consultar y mantener de forma más eficaz grandes volúmenes de datos complejos, interrelacionados y dinámicos . Si bien las empresas ahora generan y almacenan datos a una escala sin precedentes, la necesidad de normalizar las bases de datos no es nueva. Es anterior al almacenamiento en la nube e incluso a la invención de los almacenes de datos.<br><br>
                los registros de datos están relacionados entre sí en una estructura de base de datos , los cambios en valores o filas individuales de una tabla grande y compleja pueden tener consecuencias no deseadas, como inconsistencias y pérdida de datos. La normalización de bases de datos está diseñada para minimizar estos riesgos.</p>
                </div>""", unsafe_allow_html=True)


st.subheader("¿Qué anomalías de datos corrige la normalización?")
st.markdown("""<div class="justificar">
                <p>Por último, se sabe que la normalización de las estructuras de datos puede prevenir anomalías de datos, por lo cuál es importante reconocerlas y entenderlas, hay tres tipos clave de anomalías: </p>
                </div>""", unsafe_allow_html=True)

an1, an2, an3 = st.columns(3)
with an1:
    with st.expander("Inserción", expanded=True):
                st.markdown("""<div class="justificar">
                <p> Se produce una anomalía de inserción cuando no se puede insertar un registro de datos en una tabla porque le faltan valores requeridos por una o más columnas de la tabla.<br><br> </p>
                </div>""", unsafe_allow_html=True)
with an2:
    with st.expander("Eliminación", expanded=True):
                st.markdown("""<div class="justificar">
                <p>Una anomalía de eliminación se produce cuando la eliminación de un registro conlleva la eliminación involuntaria de datos importantes incluidos en dicho registro.<br><br> </p>
                </div>""", unsafe_allow_html=True)
with an3:
    with st.expander("Actualización", expanded=True):
                st.markdown("""<div class="justificar">
                <p> Una anomalía de actualización se produce cuando una instancia de datos se actualiza en una ubicación de la base de datos, pero no en otras ubicaciones donde también se almacena ese valor de datos, lo que da como resultado una falta de coherencia de los datos. </p>
                </div>""", unsafe_allow_html=True)                   

utils.cambio_pag(ant="Indice/TEMA 00/02_TiposdeDatos.py", sig="Indice/TEMA 01/01_Arquitectura.py")

