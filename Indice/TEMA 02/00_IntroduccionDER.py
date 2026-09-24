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
    .contenedor-lista {
        background-color: #1E2023;
        padding: 15px;
        border-radius: 5px;
        border-left: 5px solid #FF4B4B;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Introducción a DER")

st.header("¿Qué son los Diagramas de Entidad Relación?")
st.markdown("""<div class="justificar">
            Como su nombre lo indica, un diagrama ER representa la relación entre dos o más entidades. Pueden ser entidades del mundo real o un conjunto de entidades de una base de datos. El modelo nos ayuda a construir una estructura lógica de la base de datos o la conectividad general en el desarrollo de software. En un principio, un Diagrama de entidad-relación se parece a cualquier otro diagrama de flujo. Sin embargo, hay símbolos y propiedades específicas que los diferencian.<br><br>
            Existen diferentes tipos de diagramas ER utilizados para representar las dependencias conceptuales, lógicas y físicas entre las diferentes entidades. Por lo tanto, estos diagramas pueden ir desde una estructura simple hasta una compleja.
            </div>""", unsafe_allow_html=True)

st.subheader("Importancia de DER:")
st.markdown("""<div class="justificar">
            Los diagramas entidad-relación (DER) ayudan a comprender los fundamentos de los datos o la información que se almacenarán en la base de datos. Son fáciles de configurar y, al ser visuales, prácticamente cualquiera puede entenderlos. Estos proporcionan un diseño de base de datos bien documentado al que se puede recurrir para realizar cualquier cambio. Los diagramas entidad relación nos permiten: <br><br>
            <b class="destacar">Visualiza las relaciones: </b> Un DER  Te permite visualizar cómo se relacionan las entidades entre sí, cómo funcionan sus relaciones y dónde se pueden mejorar estas relaciones.<br>
            <b class="destacar">Simplifica sistemas complejos:</b>  Mira cómo las entidades interconectadas se conectan y se superponen para comprender mejor cómo funciona el sistema.<br>
            <b class="destacar">Educa a empleados:</b>  Utiliza un modelo lógico de datos para mostrar a los empleados nuevos y existentes cómo funcionan tus sistemas.
            </div>""", unsafe_allow_html=True)
 
st.header("Componentes de DER")
st.markdown("""<div class="justificar">
            Los diagramas de entidad-relación incluyen entidades, los atributos de dichas entidades y las relaciones entre ellas. Algunos diagramas de entidad-relación también representan la cardinalidad, que cuantifica la relación entre dos entidades.
            <br><br></div>""", unsafe_allow_html=True)
co1, co2, co3, co4 = st.columns(4)
with co1:
    st.markdown("""<div class="contenedor">
                <h4 class="destacar">Entidad:</h4>
                <p>Los conjuntos de entidades son elementos sobre los que se recopila información para representar en la base de datos. Existen dos tipos de entidades y se representan gráficamente con un rectángulo.</p>
                </div>""", unsafe_allow_html=True)
with co2:    
    st.markdown("""<div class="contenedor">
                    <h4 class="destacar">Atributos:</h4>
                    <p>Los atributos son las características o detalles que describen una entidad. Son como las propiedades que definen a un elemento dentro de las bases de datos existentes. Suela expresarse como un adjetivo.</p>
                    </div>""", unsafe_allow_html=True)    
with co3:
    st.markdown("""<div class="contenedor">
                    <h4 class="destacar">Interrelaciones:</h4>
                    <p>Una relación indica cómo interactúan o se conectan dos o más entidades. Se representa con un rombo y suele expresarse como un verbo. Existen distintos tipos de relaciones según su grado.</p>
                    </div>""", unsafe_allow_html=True)
with co4:    
    st.markdown("""<div class="contenedor">
                    <h4 class="destacar">Cardinalidad:</h4>
                    <p>La cardinalidad define cuántas veces una entidad puede estar relacionada con otra. Básicamente, muestra cuántos elementos de una entidad pueden asociarse con los de otra entidad.</p>
                    </div>""", unsafe_allow_html=True)
st.write(" ")
with st.expander("**Leyenda**"):
    st.markdown("")

st.header("Entidades y Atributos")
st.markdown("""<div class="justificar">
            Las entidades y atributos son la base del DER porque actúan como el plano arquitectónico que traduce la realidad de un negocio al lenguaje informático. Definirlos correctamente permite transformar conceptos del mundo real (como clientes o ventas) en estructuras de datos organizadas, asegurando que cada elemento del sistema esté en su lugar antes de escribir una sola línea de código.
            </div>""", unsafe_allow_html=True)

st.subheader("Entidades:")
st.markdown("""<div class="justificar">
            Una entidad en un diagrama entidad-relación (DER) es algo definible, como una persona, un rol, un evento, un concepto o un objeto, sobre el cual se puede almacenar información en una base de datos relacional. Las entidades son similares a los sustantivos en un sentido gramatical. Son elementos centrales de la base de datos, con atributos y relaciones que transmiten información sobre estas entidades, del mismo modo que los adjetivos y los verbos proporcionan más información sobre los sustantivos en una oración.
            <br><br></div>""", unsafe_allow_html=True)
ent1, ent2 = st.columns(2)
with ent1:
    st.subheader("Entidades Fuertes")
    st.markdown("""<div class="justificar">
            Objeto independiente con clave primaria propia identificado por un rectángulo simple. Representan elementos tangibles o intangibles que tienen valor por sí mismos, como Clientes, Vehículos o Cursos
            <br><br></div>""", unsafe_allow_html=True)
    with st.expander("**Forma**"):
      st.markdown("")      
with ent2:
    st.subheader("Entidades Débiles")
    st.markdown("""<div class="justificar">
            Representan subdivisiones, componentes o extensiones de información ligadas estrictamente a un elemento principal, como los Familiares de un empleado o las Líneas de un contrato de telefonía. Identificado por un rectángulo doble
            <br><br></div>""", unsafe_allow_html=True)
    with st.expander("**Forma**"):
          st.markdown("") 

st.subheader("Atributos:")
st.markdown("""<div class="justificar">
            Los atributos son cualidades, propiedades y características que definen una entidad o un tipo de entidad. En un diagrama entidad-relación (DER) clásico, los atributos se representan como óvalos y se muestran junto a la entidad correspondiente.
            <br><br></div>""", unsafe_allow_html=True)
atri1, atri2, atri3 = st.columns(3)
with atri1:
    with st.container(border=True):
      st.markdown("""<div class="justificar">
                <h4>Simples</h4>
                 Atributos atómicos que tienen un único componente y no se pueden dividir en partes más pequeñas con significado propio. Se representan con una elipse o un óvalo conectado directamente a la entidad.
                <h5 class="destacar">Por Ejemplo:</h5>
                 El Género de una persona, el Precio de un producto o la Edad.
               <br><br></p></div>""", unsafe_allow_html=True) 
    with st.expander("**Forma**"):
      st.markdown("")      
with atri2:
    with st.container(border=True):
          st.markdown("""<div class="justificar">
                    <h4>Identificatorios</h4>
                    Atributos (también llamados claves primarias o llaves) cuyo valor es único para cada registro de la entidad, impidiendo que se dupliquen. Se representan con una elipse u óvalo, pero con el texto subrayado
                    <h5 class="destacar">Por Ejemplo:</h5>
                    El Número de Cédula (DNI), el Código de Barra de un artículo o un ID_Usuario autogenerado.
                   <br><br></p></div>""", unsafe_allow_html=True)
    with st.expander("**Forma**"):
          st.markdown("") 
with atri3:
    with st.container(border=True):
          st.markdown("""<div class="justificar">
                    <h4>De una Relación</h4>
                    Atributos propios de una interrelación que describen una característica que nace únicamente cuando dos o más entidades se conectan entre sí. Solo se aplican en el caso de muchos a muchos.
                    <h5 class="destacar">Por Ejemplo:</h5>
                    La Fecha_De_Inscripción (relación entre Alumno y Curso) o las Horas_Trabajadas (relación entre Empleado y Proyecto).
                   </p></div>""", unsafe_allow_html=True)
    with st.expander("**Forma**"):
          st.markdown("") 
          
st.header("Tipos de Interrelaciones")
st.markdown("""<div class="justificar">
            Las interrelaciones (o relaciones) en un DER son el pegamento del sistema, ya que definen cómo se conectan y dependen las entidades entre sí en el mundo real. Su importancia radica en que establecen las reglas del negocio y la lógica de los datos, permitiendo que la información aislada se transforme en conocimiento útil y coherente para la toma de decisiones.<br><br>
            Definir con precisión el tipo de interrelación es el paso más crítico del diseño de bases de datos porque dicta las reglas de negocio y la estructura física del sistema. Si este paso se omite o se hace mal, el programador creará tablas equivocadas, lo que provocará fallos en la aplicación, pérdida de datos o consultas lentas y complejas.<br><br>
            </div>""", unsafe_allow_html=True)

int1, int2 = st.columns(2)
with int1:
    st.subheader("Interrelación Común:")
    st.markdown("""<div class="justificar">
                    <p>Asocia entidades fuertes que tienen existencia independiente y autónoma dentro del sistema. Su pérdida o modificación no afecta la identidad de las entidades participantes; simplemente describe una acción o vínculo cotidiano del negocio donde cada objeto conserva su propio identificador único.<br>
                    <h5 class="destacar">Por Ejemplo:</h5>
                    La relación entre Cliente y Artículo. Un cliente existe en el sistema aunque no haya comprado nada, y un artículo existe en el inventario aunque nadie lo haya adquirido. La relación "Comprar" solo une sus datos temporalmente.</p>
                    </div>""", unsafe_allow_html=True)
    with st.expander("**Forma**"):
              st.markdown("")
with int2:
    st.subheader("Interrelación Identificatoria:")
    st.markdown("""<div class="justificar">
                    <p>Vincula una entidad fuerte (dominante) con una entidad débil (subordinada) que no puede existir de forma independiente ni tiene claves propias para diferenciarse. En este tipo de relación, la entidad débil depende obligatoriamente de la fuerte para obtener su identidad y subsistir en la base de datos.<br>
                    <h5 class="destacar">Por Ejemplo:</h5>
                    La relación entre Película y Ejemplar (copias físicas en un videoclub). El ejemplar "Copia 1" o "Copia 2" no tiene sentido ni puede registrarse en el sistema si no está estrictamente identificado y amarrado a una Película específica.</p>
                    </div>""", unsafe_allow_html=True)
    with st.expander("**Forma**"):
              st.markdown("")
              
st.subheader("Según el Grado de la Interrelación:")
gra1, gra2, gra3 = st.columns(3)
with gra1:
    st.markdown("""<div class="contenedor-lista">
                    <h4 class="destacar">Unaria:</h4>
                    <p>Una sola entidad se relaciona consigo misma. Son vitales para modelar jerarquías o dependencias internas, como un Empleado que supervisa a otros Empleados.</p>
                    </div>""", unsafe_allow_html=True)
    st.write(" ")
    with st.expander("**Forma**"):
                  st.markdown("")
with gra2:
    st.markdown("""<div class="contenedor-lista">
                    <h4 class="destacar">Binaria:</h4>
                    <p>Es el tipo de relación más común y vincula exactamente a dos entidades distintas. Permite estructurar la gran mayoría de las interacciones, transacciones y flujos de trabajo habituales de un sistema de información.</p>
                    </div>""", unsafe_allow_html=True)
    st.write(" ")
    with st.expander("**Forma**"):
                  st.markdown("")
with gra3:
    st.markdown("""<div class="contenedor-lista">
                    <h4 class="destacar">Ternaria:</h4>
                    <p>Vinculan tres entidades simultáneamente debido a que la relación no puede explicarse asociándolas solo por parejas.  por ejemplo, un Proveedor que suministra un Componente específico a un Proyecto concreto.</p>
                    </div>""", unsafe_allow_html=True)
    st.write(" ")
    with st.expander("**Forma**"):
                  st.markdown("")

utils.cambio_pag(ant="Indice/TEMA 01/02_Denormalizacion.py", sig="Indice/TEMA 02/01_NotacionDER.py")