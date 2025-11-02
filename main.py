import streamlit as st
import functions as ft

#basic setup and layout
ft.config_page()

#Iniciamos la página en 0
if "datos" not in st.session_state:
    st.session_state["datos"] = 0

menu = st.sidebar.selectbox("PÁGINAS", ("1. INTRODUCCIÓN", "2. CARGA DE DATOS", "3. ANÁLISIS DE DATOS"))
if menu == "1. INTRODUCCIÓN":
    ft.home()

elif menu == "2. CARGA DE DATOS":
    datos = ft.carga_datos()
    st.session_state["datos"] = datos


# UNA VEZ DENTRO DE ANÁLISIS DE DATOS
elif menu == "3. ANÁLISIS DE DATOS":
    datos = st.session_state["datos"]
    if datos == 1:
        menu_habitos = st.sidebar.radio(
            "Selecciona el análisis: ", 
            options=["Mapa de calor", "Correlación positiva", "Correlación negativa", "Recomendaciones"])
        
        if menu_habitos == "Mapa de calor":
            st.header("📚 Correlación entre hábitos y nota 💯")

            fig = ft.mapa_calor()
            st.plotly_chart(fig, use_container_width=True)
            ft.conclu_mapa_calor()

        elif menu_habitos == "Correlación positiva":
            st.header("📈 Correlación positiva 📈")
            ft.corre_posi()

        elif menu_habitos == "Correlación negativa":
            st.header("📉 Correlación negativa 📉")
            ft.corre_nega()

        elif menu_habitos == "Recomendaciones":
            st.header('''📝 Recomendaciones 📝''')
            ft.rel_cat_num()
            #ft.recom()

    elif datos == 2:
        menu_familia = st.sidebar.radio(
            "Selecciona análisis:",
            options=["Situación Familiar", "Conclusiones"]
        )

        if menu_familia == "Situación Familiar":
            st.header("🏠 Análisis de la situación familiar 🏠")
            ft.situ()

        elif menu_familia == "Conclusiones":
            st.header("💬 Conclusiones 💬")
            ft.perfiles_estudiantes()
    else:
        st.warning("Primero debes cargar el/los CSV en el paso anterior.")

