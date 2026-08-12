import streamlit as st
import utils

st.title("Normalización")
st.header("¿Qué es la Normalización?")
st.markdown("""<div class="justificar">
                    <p>La normalización de bases de datos es un proceso de diseño que organiza los datos en estructuras de tabla específicas. Ayuda a mejorar la integridad de los datos , prevenir anomalías, minimizar la redundancia y optimizar el rendimiento de las consultas.<br><br>
                    La normalización optimiza las tablas en los sistemas de gestión de bases de datos (DBMS) para que cumplan con las denominadas formas normales: conjuntos de reglas que rigen la organización de los atributos dentro de una tabla. Estas reglas se basan principalmente en las relaciones entre los atributos (columnas), incluidas las claves utilizadas para identificar de forma única las filas </p>
                    </div>""", unsafe_allow_html=True)

st.subheader("¿Por Qué Normalizar?")
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
                <b class="destacar">Rendimiento y escalabilidad </b><br>
                El rendimiento y la escalabilidad mejoran cuando la estructura de la base de datos está limpia. Las tablas normalizadas suelen ser más pequeñas, lo que se traduce en consultas más rápidas y un mejor uso de la caché.
                </div>""", unsafe_allow_html=True)
    st.markdown("""<div class="contenedor-lista">
                <b class="destacar">Seguridad</b><br>
                La seguridad es más fácil de gestionar en bases de datos normalizadas. Puedes controlar el acceso a nivel de tabla con confianza, ya que los datos confidenciales se almacenan en ubicaciones específicas y bien definidas. 
                </div>""", unsafe_allow_html=True)
    
st.subheader("Ventajas y desventajas de la normalización")
st.markdown("""<div class="justificar">
                    <p>La seguridad es más fácil de gestionar en bases de datos normalizadas. Puedes controlar el acceso a nivel de tabla con confianza, ya que los datos confidenciales se almacenan en ubicaciones específicas y bien definidas. </p>
                    </div>""", unsafe_allow_html=True)

ven1, des2 = st.columns(2)
with ven1:
    with st.expander("Ventajas",expanded=True):
            st.markdown("""<div class="justificar">
                        <spam class="destacar">Redundancia reducida:</spam>
                        <p>significa que tu base de datos almacena cada dato exactamente una vez, lo que reduce los costes de almacenamiento y elimina los problemas de sincronización.  </p>
                        <spam class="destacar">Coherencia de los datos:</spam>
                        <p>La coherencia de los datos se vuelve automática cuando solo hay una fuente de verdad.</p>
                        <spam class="destacar">Actualizaciones rápidas y fiables:</spam>
                        <p>porque cambias una fila en lugar de docenas. Introduce un nuevo cliente una sola vez y haz referencia a él en cualquier otro lugar con claves externas.  </p>
                        </div>""", unsafe_allow_html=True)
with des2:
    with st.expander("Desventajas",expanded=True):
            st.markdown("""<div class="justificar">
                        <spam class="destacar">La complejidad de las consultas aumenta</spam>
                        <p>En una base de datos normalizada, estás uniendo las tablas clientes, pedidos, artículos de pedidos y productos. Más uniones significan más oportunidades de cometer errores y una ejecución más lenta de las consultas.  </p>
                        <spam class="destacar">El rendimiento puede verse afectado</spam>
                        <p> Cuando se unen tablas constantemente en lugar de leer desde tablas únicas y amplias. Cada unión añade sobrecarga,. </p>
                        <spam class="destacar">El tiempo de desarrollo aumenta:</spam>
                        <p> los programadores necesitan comprender las relaciones entre las tablas antes de escribir las consultas. </p>
                        </div>""", unsafe_allow_html=True)

st.header("Formas Normales")
st.markdown("""<div class="justificar">
                <p>La normalización de modelos de datos implica diseñar tablas que se ajusten a uno o más niveles de normalización, también conocidos como formas normales </p>
                </div>""", unsafe_allow_html=True)

fn1, fn2, fn3 = st.columns(3)
with fn1:
    st.markdown("""<div class="contenedor">
                <h4 class="destacar"> Primera Forma Normal</h4>
                <p class="justificar">el criterio de normalización de bases de datos más básico, exige que el esquema de una tabla incluya una clave primaria y excluya la repetición entre columnas. Más concretamente, una tabla en primera forma normal no debe tener campos con matrices de valores —por ejemplo, una sola celda con tres nombres diferentes— ni grupos repetidos, que son columnas distintas que almacenan el mismo tipo de datos.</p>
                </div>""", unsafe_allow_html=True)
with fn2:
    st.markdown("""<div class="contenedor">
                <h4 class="destacar"> Segunda Forma Normal</h4>
                <p class="justificar">En la segunda forma normal, ningún atributo que no sea clave tiene una dependencia parcial de la clave primaria de la tabla. En otras palabras, si una clave primaria es una clave compuesta, el atributo que no sea clave debe depender de cada columna de dicha clave compuesta.</p>
                </div>""", unsafe_allow_html=True)
with fn3:
    st.markdown("""<div class="contenedor">
                <h4 class="destacar"> Tercera Forma Normal</h4>
                <p class="justificar">Una tabla en tercera forma normal satisface tanto la primera como la segunda forma normal, evitando además situaciones en las que los atributos no clave dependen de otros atributos no clave en lugar de las claves primarias. Cuando los atributos no clave dependen de otros atributos no clave, se habla de dependencia transitiva, lo que constituye una violación de la tercera forma normal.</p>
                </div>""", unsafe_allow_html=True)

st.header("Conceptos Clave Para la Normalización")
st.markdown("""<div class="justificar">
                <p>Antes de empezar a normalizar tablas, debes comprender cómo funciona la normalización. Repasemos los conceptos esenciales que guiarán tus decisiones a lo largo del proceso.</p>
                </div>""", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["CLAVES", "DEPENDENCIAS", "RELACIONES"])

with tab1:
    st.subheader("Claves")
    st.markdown("""<div class="justificar">
                <p>Las claves son la base del diseño de bases de datos relacionales: identifican registros y conectan tablas entre sí.<br><br>
                Una clave principal identifica de forma única cada fila de una tabla. No puede haber dos filas con el mismo valor de clave principal, y este no puede ser nulo. Piensa en ello como un número de la seguridad social para tus datos: cada registro tiene uno único y no existen duplicados.</p>
                </div>""", unsafe_allow_html=True)
    clav1, clav2 = st.columns(2)
    with clav1:
       with st.container(border=True):
         st.markdown('''<b class="destacar">SIMPLE</b><br>
                   Claves primarias formadas por un único campo o columna (por ejemplo, un ID de usuario o número de pasaporte).
                   ''',  unsafe_allow_html=True)
    with clav2:
       with st.container(border=True):
         st.markdown('''<b class="destacar">COMPUESTA</b><br>
                   Claves primarias formadas por la combinación de dos o más campos.
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
                   Un campo depende de manera indirecta de otro a través de un tercero que no es una clave principal.
                   ''',  unsafe_allow_html=True)
   with dep3:
      with st.container(border=True):
         st.markdown('''<b class="destacar">PARCIAL</b><br>
                    Un campo depende solo de una parte de una clave compuesta, lo que rompe la segunda forma normal y causa duplicación de datos.
                   ''',  unsafe_allow_html=True)
with tab3:
   st.subheader("Cardinalidad")
   st.markdown("""<div class="justificar">
                <p>la cardinalidad es la restricción estructural que define la existencia de dependencias (funcionales o multivaluadas) y determina los límites correctos de las tablas. No se ve simplemente como una regla de negocio, sino como el factor matemático que dicta qué atributos pueden convivir en la misma tabla sin generar redundancia.</p>
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
                <p>En esencia, la normalización de bases de datos —a veces llamada normalización de datos— ayuda a las empresas e instituciones a organizar, consultar y mantener de forma más eficaz grandes volúmenes de datos complejos, interrelacionados y dinámicos . Si bien las empresas ahora generan y almacenan datos a una escala sin precedentes, la necesidad de normalizar las bases de datos no es nueva. Es anterior al almacenamiento en la nube e incluso a la invención de los almacenes de datos.<br><br>
                los registros de datos están relacionados entre sí en una estructura de base de datos , los cambios en valores o filas individuales de una tabla grande y compleja pueden tener consecuencias no deseadas, como inconsistencias y pérdida de datos. La normalización de bases de datos está diseñada para minimizar estos riesgos.</p>
                </div>""", unsafe_allow_html=True)


st.subheader("¿Qué anomalías de datos corrige la normalización?")
st.markdown("""<div class="justificar">
                <p>La normalización de las estructuras de datos puede prevenir tres tipos clave de anomalías: </p>
                </div>""", unsafe_allow_html=True)

an1, an2, an3 = st.columns(3)
with an1:
    with st.expander("Inserción", expanded=True):
                st.markdown("""<div class="justificar">
                <p> Se produce una anomalía de inserción cuando no se puede insertar un registro de datos en una tabla porque le faltan valores requeridos por una o más columnas de la tabla. </p>
                </div>""", unsafe_allow_html=True)
with an2:
    with st.expander("Eliminación", expanded=True):
                st.markdown("""<div class="justificar">
                <p>Una anomalía de eliminación se produce cuando la eliminación de un registro conlleva la eliminación involuntaria de datos importantes incluidos en dicho registro. </p>
                </div>""", unsafe_allow_html=True)
with an3:
    with st.expander("Actualización", expanded=True):
                st.markdown("""<div class="justificar">
                <p> Una anomalía de actualización se produce cuando una instancia de datos se actualiza en una ubicación de la base de datos, pero no en otras ubicaciones donde también se almacena ese valor de datos, lo que da como resultado una falta de coherencia de los datos. </p>
                </div>""", unsafe_allow_html=True)                   

utils.cambio_pag(ant="Indice/TEMA 00/02_TiposdeDatos.py", sig="Indice/TEMA 01/01_Arquitectura.py")

