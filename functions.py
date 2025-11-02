import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import plotly.express as px

def config_page():
    st.set_page_config(page_title = "EDA_AYMC", page_icon=":chart", layout = "centered")

def home():
    st.header("Hábitos académicos y Situación familiar")

    st.subheader("EDA")

    st.image("./img/mini_eda_3.png", use_container_width="auto")

    st.markdown("""
                El ***ministerio de educación*** de Portugal, quiere saber en base a los datos que tienen: 
> ¿Qué afecta más al rendimiento acaémico, los hábitos estudiantiles o la situación familiar?
                """)

    st.markdown("""En este EDA tenemos el estudio de una de las preguntas que más tiempo me ha acompañado en mi vida, 
                desde que tengo uso de razón me recuerdo estudiando o teniendo que memorizar algo de temario para 
                algún exámen. Recuerdo también compañeros que se le daban muy bien y que hasta le sobraba el tiempo 
                para salir con sus amigos o de fiesta.

Con el tiempo, la vida me junto con personas que el ambiente o la relación familiar no era como la mía y desde entonces me persigue 
                esa pregunta, hoy a través de un pequeño EDA, quiero dar un poco de luz a este tema.

>> Decir que las conclusiones de este trabajo están sujetas a la muestra de los datos, que de este tema es 
                muy escaso.
                """)

#    st.write("Storytelling")

    with st.expander("Storytelling"):
        st.markdown("""Eres un analísta de datos que ha sido contratado por el **ministerio de educación** de Portugal en 2009, ellos te han 
                    dado tres datasets, el primero de ellos es sobre los habitos académicos de los estudiantes, los otros dos 
                    corresponden a la situación familiar de los estudiantes y sus notas en dos diferentes asignaturas.
                    """)
        st.markdown("""
            > Negocio te ha pedido que respondas a las siguientes preguntas:
                    
            * ¿Dentro de los hábitos académicos, quiere saber recomendaciones para los alumnos?
            * ¿Dentro de lo familiar, cúales son las conclusiones a las que llegas?
            * ¿A qué parte deberíamos aportar con más recursos?""")
        
    with st.expander("Links a Datasets"):
        st.markdown("""[Datasets de los hábitos académicos](https://www.kaggle.com/datasets/jayaantanaath/student-habits-vs-academic-performance)""")
        st.markdown("""[Datasets de la situación familiar](https://archive.ics.uci.edu/dataset/320/student+performance)""")

def carga_datos(): 
    uploaded_file = st.file_uploader("Cargar CSV", type=["csv"], accept_multiple_files=True)

    datos = len(uploaded_file)

    if uploaded_file:
        if datos == 1:
            df = pd.read_csv(uploaded_file[0])
            df.set_index("student_id", inplace=True)    
            df.drop(["parental_education_level","extracurricular_participation", "internet_quality"], axis = 1, inplace=True)
            st.session_state["df"] = df
            
        elif datos == 2:
            d1=pd.read_csv(uploaded_file[0],sep=";")

            d2=pd.read_csv(uploaded_file[1],sep=";")

            d3 = pd.concat([d1,d2], ignore_index=True)

            # DROP DUPLICADOS
            df = d3.drop_duplicates(subset=["school","sex","age","address","famsize","Pstatus","Medu","Fedu","Mjob","Fjob","reason","nursery","internet"])

            # DROP FIJO
            df.drop(["G1", "G2", "school", "internet", "higher", "nursery", "activities", "paid", "studytime", "freetime", "goout", "traveltime"], axis=1, inplace=True)

            # DROP SECUNDARIO
            df.drop(["reason", "failures", "schoolsup", "Dalc", "health", "absences"], axis=1, inplace=True)

            df.reset_index()

            st.session_state["df"] = df

    if datos == 1:
        if st.button("Ver hábitos académicos"):
            st.markdown("<h3 style='text-align: center; color: white;'>HÁBITOS ACADÉMICOS</h3>", unsafe_allow_html=True)
            st.dataframe(df)
            st.subheader('''*Tabla de descripción de los datos:*''')
            st.markdown('''
|DATOS | TIPO | DESCRIPCIÓN |
|----|---|---|
|student_id| Numerica continua | Es el identificador del estudiante |
|age| Numerica discreta | Es la edad del estudiante en años |
|gender| Categorica | Indica el género del estudiante |
|study_hours_per_day| Numerica discreta | Horas diarias dedicadas al estudio |
|social_media_hours| Numerica discreta | Horas diarias en redes sociales |
|netflix_hours| Numerica discreta | Horas diarias viendo Netflix |
|> *part_time_job*| Binario Booleano | Indica si el estudiante tiene empleo parcial |                
|attendance_percentage| Numerica continua | Porcentaje de asistencia a clases |
|sleep_hours| Numerica discreta | Horas promedio de sueño por día |
|diet_quality| Categorica | Nivel de la calidad de la dieta |
|exercise_frequency| Numerica discreta | Frecuencia semanal de ejercicio |
|> *mental_health_rating*| Numerica discreta | Valoración del bienestar mental |
|examn_score| Numerica continua | Puntuación obtenida en los exámenes |
                        ''')
            st.markdown('''El dataset venía con datos que no voy a usar, como por ejemplo, la calidad del internet ( >80% con 
buen internet ), clases extracurriculares, por no ser trascendente, así como el nivel de educaión de los padres, 
ya que para eso usaré los otros datasets, me gustaría destacar 2 datos: ''')
            
            with st.expander("Debate"):
                st.markdown("""
                        - part_time_job --> Si trabaja o no
                                            
                        - mental_health_rating --> Salud mental
                                            
                        > ¿Afectan a los hábitos o son hábitos?
                                        """)
                
    elif datos == 2:
         if st.button("Ver situación familiar"):
            st.markdown("<h3 style='text-align: center; color: white;'>SITUACIÓN FAMILIAR</h3>", unsafe_allow_html=True)
            st.dataframe(df)
            st.subheader('''*Tabla de descripción de los datos:*''')
            st.markdown('''
|DATOS | TIPO | DESCRIPCIÓN |
|----|---|---|
|> *sex*| Categorica | Indica el género del estudiante |
|age| Numerica discreta | Es la edad del estudiante en años |
|address| Categorica binario | Tipo de dirección del hogar (‘U’ = urbana, ‘R’ = rural) |
|famsize| Categorica binario | Tamaño de la familia (‘LE3’ = ≤3, ‘GT3’ = >3 miembros) |
|Pstatus| Categorica binario | Estado civil de los padres (‘T’ = juntos, ‘A’ = separados) |
|Medu| Categorico numerica | Nivel educativo de la madre |
|Fedu| Categorico numerica | Nivel educativo del padre |                
|Mjob| Categorico | Profesión de la madre (docente, salud, servicios, hogar, otro) |
|Fjob| Categorico | Profesión del padre (docente, salud, servicios, hogar, otro) |
|guardian| Categorica | Tutor principal del estudiante (madre, padre u otro) |
|famsup| Categorico binario | Indica si recibe apoyo educativo familiar |
|> *romantic*| Categorico binario | Indica si tiene una relación sentimental |
|famrel| Categórica numerica | Calidad de las relaciones familiares |
|> *Walc*| Categórica numerica | Consumo de alcohol los fines de semana |
|G3| Numerica continua | Calificación final del estudiante |
                        ''')
            st.markdown('''Dentro del dataset prescindido de varios datos que también podrían ser analizados, pero para resolver las principales preguntas me centraré en estas columnas,
y he incuido también algunas con las que quiero generar debate.
                        ''')
            with st.expander("Debate"):
                st.markdown("""
> Género
     
> Consumo de alcohol (fin de semana)
                        
> Relación amorosa
                        
¿Debido a su situación familiar le tocará al estudiante asumir otros roles?
                        
¿Mala relación significa mayor consumo de alcohol o este hábito se puede deber a otra cosa de la tabla (poca supervisión)?

La media y la moda de estudiantes 17 años.
                                        """)


    return datos

# HÁBITOS ACADÉMICOS
def mapa_calor():
    df = st.session_state["df"]

    df["ocio_al_dia"] = df.netflix_hours + df.social_media_hours
    df = df.drop(["netflix_hours", "social_media_hours"], axis=1)

    df["nota"] = df.pop("exam_score")

    df_numeric = df.select_dtypes(include="number")

    corr = df_numeric.corr()
    st.session_state["corr"] = corr

    mask = np.triu(np.ones_like(corr, dtype=bool))
    
    corr_masked = corr.mask(mask)

    fig = px.imshow(
        corr_masked,
        text_auto=".3f",      
        aspect="auto",         
        color_continuous_scale="YlOrRd", 
        origin="upper"
    )
    return fig

def conclu_mapa_calor():
    corr = st.session_state["corr"]
    ranking_corr = corr.sort_values(by = "nota", ascending=False)
    ranking_corr.drop("nota", axis=0, inplace=True)

    top_3 = ranking_corr.nota.head(3).index
    top_3_d = reversed(ranking_corr.nota.tail(3).index)

    st.header("🔍 Correlation Insights:")

    st.subheader("📈 Las 3 correlaciones positivas más fuertes con nota:")
    for i in top_3:
        st.markdown(f"• {i}: {ranking_corr['nota'].loc[i]:.3f}")

    st.subheader("📉 Las 3 correlaciones negativas más fuertes con nota:")
    for i in top_3_d:
        st.markdown(f"• {i}: {ranking_corr['nota'].loc[i]:.3f}")

def corre_posi():
    df = st.session_state["df"]
    with st.sidebar:
        st.subheader("⚙️ Configuración ⚙️")

        # Variables categóricas disponibles (ajústalas a tus columnas reales)
        posibles_vars = [
            "Horas_de_estudio_al_día",
            "Rango_salud_mental",
            "Rango_actividad_fisica_a_la_semana"
        ]

        #RANGO DE NOTAS
        rangos = [0, 50, 70, 90, 100]
        etiquetas = ["Suspenso", "Bien", "Notable", "Sobresaliente"]
        df['Rango_notas'] = pd.cut(df['exam_score'], bins=rangos, labels=etiquetas, include_lowest=True)

        #RANGO DE HORAS ESTUDIADO:
        rangos = [0, 3, 6, 9]
        etiquetas = ["0-2", "3-5", "6-9"]
        df['Horas_de_estudio_al_día'] = pd.cut(df['study_hours_per_day'], bins=rangos, labels=etiquetas, include_lowest=True)

        #RANGO SALUD MENTAL
        rangos = [1, 3, 5, 8, 10]
        etiquetas = ["bajo", "medio-bajo", "medio-alto", "alto"]
        df['Rango_salud_mental'] = pd.cut(df['mental_health_rating'], bins=rangos, labels=etiquetas, include_lowest=True)

        #RANGO ACTIVIDAD FÍSICA SEMANAL
        rangos = [0, 3, 5, 6]
        etiquetas = ["0-2", "3-4", "5-6"]
        df['Rango_actividad_fisica_a_la_semana'] = pd.cut(df['exercise_frequency'], bins=rangos, labels=etiquetas, include_lowest=True)

        # Selector principal
        cat_vars = st.multiselect(
            "Escoge el hábito:",
            options=posibles_vars,
            default=["Horas_de_estudio_al_día"]
        )

        # Opciones adicionales
        relative = st.checkbox("Mostrar frecuencias relativas", value=True)
        show_values = st.checkbox("Mostrar valores en las barras", value=True)

        tipo_barra = st.radio(
            "Tipo de visualización de barras:",
            options=["Agrupadas", "Apiladas"],
            index=0,
            horizontal=True
        )

    # --- Construcción del gráfico ---
    for cat_col1 in cat_vars:
        count_data = df.groupby([cat_col1, "Rango_notas"]).size().reset_index(name='count')
        total_counts = df[cat_col1].value_counts()

        if relative:
            count_data['count'] = count_data.apply(
                lambda x: x['count'] / total_counts[x[cat_col1]], axis=1
            )
            y_label = f"Frecuencia relativa {cat_col1.replace('_',' ')}"
            text_format = ".2%"
        else:
            y_label = f"Frecuencia absoluta {cat_col1.replace('_',' ')}"
            text_format = ",d"

        barmode = "group" if tipo_barra == "Agrupadas" else "stack"

        fig = px.bar(
            count_data,
            x=cat_col1,
            y="count",
            color="Rango_notas",
            barmode=barmode,
            color_discrete_sequence=px.colors.qualitative.Set2,
            text="count" if show_values else None
        )

        if show_values:
            fig.update_traces(
                texttemplate=f"%{{text:{text_format}}}",
                textposition="outside"
            )
        else:
            fig.update_traces(text=None, texttemplate=None) 

        fig.update_layout(
            title=f"Relación entre {cat_col1.replace('_',' ')} y {"Rango_notas".replace('_',' ')}",
            xaxis_title=cat_col1.replace("_", " ").capitalize(),
            yaxis_title=y_label,
            legend_title="Rango_notas".replace("_", " "),
            bargap=0.15,
            height=550,
        )

        st.plotly_chart(fig, use_container_width=True)

def corre_nega():
    df = st.session_state["df"]
    with st.sidebar:
        st.subheader("⚙️ Configuración ⚙️")

        # Variables categóricas disponibles (ajústalas a tus columnas reales)
        posibles_vars = [
            "Rango_ocio_al_dia",
            "age",
            "Rango_attendance_percentage"
        ]

        #RANGO DE NOTAS
        rangos = [0, 50, 70, 90, 100]
        etiquetas = ["Suspenso", "Bien", "Notable", "Sobresaliente"]
        df['Rango_notas'] = pd.cut(df['exam_score'], bins=rangos, labels=etiquetas, include_lowest=True)

        #RANGO OCIO AL DIA
        rangos = [0, 4, 8, 10]
        etiquetas = ["0-3", "4-7", "8-10"]
        df['Rango_ocio_al_dia'] = pd.cut(df['ocio_al_dia'], bins=rangos, labels=etiquetas, include_lowest=True)
        
        #RANGO ASISTENCIA A CLASE
        rangos = [56, 84, 100]
        etiquetas = ["Poco", "Mucho"]
        df['Rango_attendance_percentage'] = pd.cut(df['attendance_percentage'], bins=rangos, labels=etiquetas, include_lowest=True)

        # Selector principal
        cat_vars = st.multiselect(
            "Escoge el hábito:",
            options=posibles_vars,
            default=["Rango_ocio_al_dia"]
        )

        # Opciones adicionales
        relative = st.checkbox("Frecuencia relativa", value=True)
        show_values = st.checkbox("Mostrar valores en las barras", value=True)

        tipo_barra = st.radio(
            "Tipo de visualización de barras:",
            options=["Agrupadas", "Apiladas"],
            index=0,
            horizontal=True
        )

    # --- Construcción del gráfico ---
    for cat_col1 in cat_vars:
        count_data = df.groupby([cat_col1, "Rango_notas"]).size().reset_index(name='count')
        total_counts = df[cat_col1].value_counts()

        if relative:
            count_data['count'] = count_data.apply(
                lambda x: x['count'] / total_counts[x[cat_col1]], axis=1
            )
            y_label = f"Frecuencia relativa {cat_col1.replace('_',' ')}"
            text_format = ".2%"
        else:
            y_label = f"Frecuencia absoluta {cat_col1.replace('_',' ')}"
            text_format = ",d"

        barmode = "group" if tipo_barra == "Agrupadas" else "stack"

        fig = px.bar(
            count_data,
            x=cat_col1,
            y="count",
            color="Rango_notas",
            barmode=barmode,
            color_discrete_sequence=px.colors.qualitative.Set2,
            text="count" if show_values else None
        )

        if show_values:
            fig.update_traces(
                texttemplate=f"%{{text:{text_format}}}",
                textposition="outside"
            )
        else:
            fig.update_traces(text=None, texttemplate=None) 

        fig.update_layout(
            title=f"Relación entre {cat_col1.replace('_',' ')} y {"Rango_notas".replace('_',' ')}",
            xaxis_title=cat_col1.replace("_", " ").capitalize(),
            yaxis_title=y_label,
            legend_title="Rango_notas".replace("_", " "),
            bargap=0.15,
            height=550,
        )

        st.plotly_chart(fig, use_container_width=True)

def rel_cat_num():
    df = st.session_state["df"]
    df["Aprobar"] = df.exam_score >= 50

    with st.sidebar:
        st.subheader("⚙️ Configuración ⚙️")

        # Definir variables categóricas y numéricas disponibles
        posibles_cat = [
            "Rango_notas",
            "Aprobar"
        ]
        posibles_num = ["study_hours_per_day", "ocio_al_dia"]

        # --- Controles interactivos ---
        cat_col = st.selectbox("Variable categórica:", opciones := posibles_cat)
        num_col = st.selectbox("Variable numérica:", opciones_num := posibles_num, index=0)

        measure = st.radio(
            "Medida de tendencia central:",
            options=["Media", "Mediana", "Moda"],
            index=0,
            horizontal=True
        )

        show_values = st.checkbox("Mostrar valores en las barras", value=True)

    # --- Procesamiento de datos ---
    if measure == "Mediana":
        grouped_data = df.groupby(cat_col)[num_col].median().sort_values(ascending=False)
    elif measure == "Moda":  
        grouped_data = (
            df.groupby(cat_col)[num_col]
            .apply(lambda x: x.mode().iloc[0] if not x.mode().empty else np.nan)
            .sort_values(ascending=False)
        )
    else:
        grouped_data = df.groupby(cat_col)[num_col].mean().sort_values(ascending=False)
    
    grouped_data = grouped_data.reset_index(name=measure.lower())

    # --- Construcción del gráfico ---
    unique_categories = grouped_data[cat_col].unique()
    num_plots = int(np.ceil(len(unique_categories) / 5))

    for i in range(num_plots):
        categories_subset = unique_categories[i * 5:(i + 1) * 5]
        data_subset = grouped_data[grouped_data[cat_col].isin(categories_subset)]

        fig = px.bar(
            data_subset,
            x=cat_col,
            y=measure.lower(),
            text=measure.lower() if show_values else None,
            color=cat_col,
            color_discrete_sequence=px.colors.qualitative.Set2
        )

        if show_values:
            fig.update_traces(
                texttemplate="%{text:.0f}",
                textposition="outside"
            )

        fig.update_layout(
            title=f"Relación entre {cat_col.replace('_',' ')} y {num_col.replace('_',' ')}"
                  + (f" - Grupo {i + 1}" if num_plots > 1 else ""),
            xaxis_title=cat_col.replace("_", " ").capitalize(),
            yaxis_title=f"{measure} de {num_col.replace('_', ' ')}",
            showlegend=False,
            bargap=0.3,
            height=550,
        )

        st.plotly_chart(fig, use_container_width=True)

#NO USADO
def recom():
    df = st.session_state["df"]
    df["Aprobar"] = df.exam_score >= 50
    horas = df.groupby(["Aprobar"])["study_hours_per_day"].mean().astype(int).values
    st.markdown(f"Si quieres aprobar deberías estudiar más de {horas[1]} horas diarias.")

    notas = df.groupby(["Rango_notas"])["study_hours_per_day"].mean().astype(int).index
    horas = df.groupby(["Rango_notas"])["study_hours_per_day"].mean().astype(int).values

    for i in range(len(notas)):
        if notas[i] == "Suspenso":
            if horas[i] == 1:
                st.markdown(f"Para evitar suspender estudia más de {horas[i]} hora")
            else: 
                st.markdown(f"Para evitar suspender estudia más de {horas[i]} horas")
        else:
            st.markdown(f"Para llegar al {notas[i]} estudia más de {horas[i]} horas")

# SITUACIÓN FAMILIAR
def situ():
    df = st.session_state["df"]
    df["Aprobar"] = df.G3 >= 10
    
    with st.sidebar:
        st.subheader("⚙️ Configuración ⚙️")

        posibles_cat = [
            "sex", "address", "famsize", "Pstatus", "Mjob", "Fjob", "guardian",
            "famsup", "romantic", "Rango_edu_mother", "Rango_edu_father", "Rango_fam_rel"
        ]

        cat_vars = st.multiselect(
            "Escoge la variable categórica:",
            options=posibles_cat,
            default=["address"]
        )
        #RANGO DE NOTAS
        rangos = [0, 9, 14, 17, 20]
        etiquetas = ["Suspenso", "Bien", "Notable", "Sobresaliente"]
        df['Rango_notas'] = pd.cut(df['G3'], bins=rangos, labels=etiquetas, include_lowest=True)

        #RANGO EDU MAMA:
        rangos = [0, 1, 2, 3, 4]
        etiquetas = ["Bajo", "Medio-Bajo", "Medio-Alto", "Alto"]
        df['Rango_edu_mother'] = pd.cut(df['Medu'], bins=rangos, labels=etiquetas, include_lowest=True)

        #RANGO EDU PAPA
        rangos = [0, 1, 2, 3, 4]
        etiquetas = ["Bajo", "Medio-Bajo", "Medio-Alto", "Alto"]
        df['Rango_edu_father'] = pd.cut(df['Fedu'], bins=rangos, labels=etiquetas, include_lowest=True)
        
        #RANGO ACTIVIDAD FÍSICA SEMANAL
        rangos = [1, 3, 4, 5]
        etiquetas = ["Baja", "Media", "Alta"]
        df['Rango_fam_rel'] = pd.cut(df['famrel'], bins=rangos, labels=etiquetas, include_lowest=True)

        # --- VARIABLES DISPONIBLES ---
        target = st.radio(
            "Nota:",
            options=["Rango_notas", "G3"],
            horizontal=True
        )

        show_values = st.checkbox("Mostrar valores en las barras", value=True)

        if target == "Rango_notas":
            relative = st.checkbox("Frecuencia relativa", value=True)
            tipo_barra = st.radio(
                "Tipo de visualización de barras:",
                options=["Agrupadas", "Apiladas"],
                index=0,
                horizontal=True
            )
        else:
            measure = st.radio(
                "Medida de tendencia central:",
                options=["Media", "Mediana"],
                index=0,
                horizontal=True
            )

    # --- VISUALIZACIÓN ---
    for cat_col in cat_vars:

        # 🔹 CASO 1: Análisis categórica vs Rango_notas (frecuencias)
        if target == "Rango_notas":
            count_data = df.groupby([cat_col, "Rango_notas"]).size().reset_index(name="count")
            total_counts = df[cat_col].value_counts()

            if relative:
                count_data["count"] = count_data.apply(
                    lambda x: x["count"] / total_counts[x[cat_col]], axis=1
                )
                y_label = "Frecuencia relativa"
                text_format = ".2%"
            else:
                y_label = "Frecuencia absoluta"
                text_format = ",d"

            barmode = "group" if tipo_barra == "Agrupadas" else "stack"

            fig = px.bar(
                count_data,
                x=cat_col,
                y="count",
                color="Rango_notas",
                barmode=barmode,
                color_discrete_sequence=px.colors.qualitative.Set2,
                text="count" if show_values else None
            )

            if show_values:
                fig.update_traces(texttemplate=f"%{{text:{text_format}}}", textposition="outside")

            fig.update_layout(
                title=f"Relación entre {cat_col.replace('_',' ')} y {target.replace('_',' ')}",
                xaxis_title=cat_col.replace("_", " ").capitalize(),
                yaxis_title=y_label,
                legend_title="Rango de notas",
                bargap=0.15,
                height=550,
            )

            st.plotly_chart(fig, use_container_width=True)

        # 🔹 CASO 2: Análisis categórica vs G3 (nota numérica)
        else:
            if measure == "Mediana":
                grouped_data = df.groupby(cat_col)["G3"].median().reset_index()
            else:
                grouped_data = df.groupby(cat_col)["G3"].mean().reset_index()

            # Truncar valores decimales (sin redondear)
            grouped_data["G3"] = grouped_data["G3"].apply(lambda x: int(np.floor(x)))

            fig = px.bar(
                grouped_data,
                x=cat_col,
                y="G3",
                text="G3" if show_values else None,
                color=cat_col,
                color_discrete_sequence=px.colors.qualitative.Set2
            )

            if show_values:
                fig.update_traces(texttemplate="%{text}", textposition="outside")

            fig.update_layout(
                title=f"Relación entre {cat_col.replace('_',' ')} y Nota final (G3)",
                xaxis_title=cat_col.replace("_", " ").capitalize(),
                yaxis_title=f"{measure} truncada de la nota (G3)",
                showlegend=False,
                bargap=0.3,
                height=550,
            )

            st.plotly_chart(fig, use_container_width=True)

def perfiles_estudiantes():
    df = st.session_state["df"]

    st.subheader("👨‍🎓 Perfiles 👩‍🎓")

    # --- Preparar las categorías ---
    categorias = ["address", "famsize", "Pstatus", "Rango_edu_mother", 
                  "Rango_edu_father", "Rango_fam_rel", "Mjob", "Fjob", 
                  "guardian", "famsup"]

    # --- PERFIL 1: Estudiantes que aprueban ---
    st.subheader("✅ Estudiantes que aprueban")
    mask = df["Aprobar"] == True
    perfil_aprueban = df.loc[mask, categorias].mode().iloc[0]
    st.dataframe(perfil_aprueban.to_frame(name="Valor más frecuente"))

    # --- PERFIL 2: Estudiantes que suspenden ---
    st.subheader("❌ Estudiantes que suspenden")
    mask = df["Aprobar"] == False
    perfil_suspenden = df.loc[mask, categorias].mode().iloc[0]
    st.dataframe(perfil_suspenden.to_frame(name="Valor más frecuente"))

    # --- PERFIL 3: Estudiantes sobresalientes ---
    st.subheader("🏆 Estudiantes sobresalientes")
    mask = df["Rango_notas"] == "Sobresaliente"
    perfil_sobresalientes = df.loc[mask, categorias].mode().iloc[0]
    st.dataframe(perfil_sobresalientes.to_frame(name="Valor más frecuente"))

    # --- Conclusión visual ---
    st.markdown("### 📊 Interpretación general")
    st.write("""
    - Dentro de esta muestra y con respecto a estos perfiles, columnas como el **address, guardian, Fjob, Pstatus**, ya que se repiten en todos los perfiles.
             
    - **Quienes aprueban** suelen compartir ciertas características como entornos familiares estables o niveles educativos medios-altos de los padres.  
             
    - **Los que suspenden** tienden a concentrarse en entornos con menor apoyo familiar o niveles educativos más bajos.  
    
    - **Los sobresalientes** presentan un perfil de mayor estabilidad sociofamiliar, con padres de educación alta y buena calidad de relaciones familiares.
    """)

