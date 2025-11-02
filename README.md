
# 🎓 Análisis Exploratorio de Datos: Hábitos Académicos y Situación Familiar

## 📘 Descripción general

Este proyecto realiza un **Análisis Exploratorio de Datos (EDA)** sobre el comportamiento académico de los estudiantes, integrando dos ejes principales:

1. **Hábitos académicos y personales** — horas de estudio, tiempo de ocio, salud mental, actividad física y asistencia.  
2. **Situación familiar y contexto socioeconómico** — nivel educativo de los padres, relaciones familiares, tamaño del hogar, tipo de tutor y apoyo educativo.

El objetivo principal es **entender cómo ambos factores se relacionan con el rendimiento académico** y con la probabilidad de aprobar, generando visualizaciones interactivas, correlaciones y perfiles de estudiante.

---

## 🎯 Objetivos del proyecto

- Analizar la relación entre **hábitos académicos, de ocio y bienestar personal** frente al **rendimiento escolar**.  
- Estudiar cómo variables como las **horas de estudio, la salud mental, la asistencia o el ocio diario** influyen en las calificaciones.  
- Identificar **los hábitos más determinantes** en el éxito académico mediante un **mapa de calor de correlaciones**, destacando las tres correlaciones positivas y negativas más fuertes con la nota.  
- Explorar la influencia de **hábitos positivos** (como el estudio diario, la salud mental o la actividad física) y **hábitos negativos** (como el exceso de ocio o baja asistencia) sobre el rendimiento.  
- Aplicar medidas de **tendencia central** (media, mediana y moda) para comparar valores numéricos según categorías, con visualizaciones configurables (agrupadas/apiladas, absolutas/relativas).  

- Analizar cómo la **situación familiar** (nivel educativo de los padres, convivencia, relaciones familiares, tipo de tutor y apoyo) puede reforzar o contrarrestar los patrones académicos.  
- Generar **perfiles descriptivos de estudiantes** aprobados, suspendidos o sobresalientes, mostrando sus características familiares más frecuentes.  

---

## 🧠 Metodología y estructura de análisis

El proyecto se ha desarrollado en **Streamlit**, estructurado en distintas vistas interactivas que permiten navegar entre los distintos ejes del análisis:

### 1. 📊 Hábitos académicos
Incluye el análisis de las variables más relacionadas con el rendimiento:
- `study_hours_per_day`
- `mental_health_rating`
- `exercise_frequency`
- `attendance_percentage`
- `ocio_al_dia` (combinación de `netflix_hours` + `social_media_hours`)

### 2. 🏠 Situación familiar
Se analizan variables como:
- `address`, `famsize`, `Pstatus`, `Rango_edu_mother`, `Rango_edu_father`, `Rango_fam_rel`, `Mjob`, `Fjob`, `guardian`, `famsup`.

Las relaciones se visualizan frente a `Rango_notas` y `G3`, explorando tendencias y patrones familiares asociados al rendimiento.

---

## 📁 Estructura del proyecto

```
📦 EDA
 ┣ 📂 data/
 ┃ ┣ 📂 habitos/
 ┃ ┃ ┗ student_habits_performance.csv
 ┃ ┗ 📂 personal/
 ┃   ┣ student-mat-csv
 ┃   ┣ student-merge.R
 ┃   ┣ student-por.csv
 ┃   ┗ student.txt
 ┃
 ┣ 📂 img/
 ┃ ┣ mini_eda_1.png
 ┃ ┗ mini_eda_3.png
 ┃
 ┣ 📂 memoria/
 ┃ ┣ bootcampviztools.py
 ┃ ┗ memoria.ipynb
 ┃
 ┣ 📂 notebooks/
 ┃ ┣ bootcampviztools.py
 ┃ ┣ Hábitos.py
 ┃ ┗ Personal.py
 ┃
 ┣ funtions.py
 ┣ main.py
 ┣ README.md
 ┗ requierements.txt
```

---

## ⚙️ Instalación y ejecución

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/aldairyasser/EDA-AYMC.git
   cd EDA_Estudiante
   ```

2. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar la aplicación:**
   ```bash
   streamlit run main.py
   ```

---

## 📦 requirements.txt

[requirements.txt](requirements.txt)

---

## 🧩 Conclusión general

El análisis revela que el **rendimiento académico no depende de un solo factor**, sino de la interacción entre **hábitos personales y entorno familiar**.  

Los estudiantes con **hábitos equilibrados** (estudio constante, salud mental estable, ocio moderado) y **apoyo familiar positivo** tienden a obtener **mejores resultados académicos**.
