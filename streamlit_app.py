import streamlit as st
from transformers import pipeline
# Show title and description.
st.title("💬 ResumeAI")
st.write(
    "Esta aplicación te permite generar resúmenes automáticos de textos, extraer las ideas clave y visualizar los conceptos más importantes de manera clara y sencilla."

"Con esta herramienta, podrás transformar textos largos en resúmenes concisos, identificar las palabras clave y crear cuadros conceptuales para una comprensión más profunda."

"Simplifica tu proceso de lectura y análisis con nuestra app: resume, extrae palabras clave y organiza la información en cuadros conceptuales, todo en un solo clic."
)
# Cargar los modelos de IA para resumen y palabras clave
resumen_modelo = pipeline("summarization")
keywords_modelo = pipeline("ner")

# Título de la aplicación
st.title("Aplicación de Resúmenes, Cuadros Conceptuales y Palabras Clave")

# Descripción
st.write("""
    Esta aplicación te ayudará a generar resúmenes automáticos, extraer palabras clave y crear cuadros conceptuales.
    Ingresa el texto en el campo de abajo y selecciona una de las opciones para procesarlo.
""")

# Entrada de texto
texto_entrada = st.text_area("Introduce el texto para analizar", height=200)

# Función para generar resumen
def generar_resumen(texto):
    try:
        resumen = resumen_modelo(texto)
        return resumen[0]['summary_text']
    except Exception as e:
        return f"Error generando resumen: {str(e)}"

# Función para generar cuadro conceptual (se puede personalizar según lo que necesites)
def generar_cuadro_conceptual(texto):
    try:
        # Aquí puedes implementar la lógica para cuadros conceptuales
        return f"Cuadro conceptual generado para: {texto[:50]}..."  # Ejemplo básico
    except Exception as e:
        return f"Error generando cuadro conceptual: {str(e)}"

# Función para identificar palabras clave
def identificar_palabras_clave(texto):
    try:
        palabras_clave = [entidad['word'] for entidad in keywords_modelo(texto)]
        return palabras_clave
    except Exception as e:
        return f"Error identificando palabras clave: {str(e)}"

# Botones para ejecutar las funciones
if st.button("Generar Resumen"):
    if texto_entrada:
        resumen = generar_resumen(texto_entrada)
        st.subheader("Resumen:")
        st.write(resumen)
    else:
        st.error("Por favor, ingresa un texto para resumir.")

if st.button("Generar Cuadro Conceptual"):
    if texto_entrada:
        cuadro_conceptual = generar_cuadro_conceptual(texto_entrada)
        st.subheader("Cuadro Conceptual:")
        st.write(cuadro_conceptual)
    else:
        st.error("Por favor, ingresa un texto para generar el cuadro conceptual.")

if st.button("Identificar Palabras Clave"):
    if texto_entrada:
        palabras_clave = identificar_palabras_clave(texto_entrada)
        st.subheader("Palabras Clave:")
        st.write(", ".join(palabras_clave))
    else:
        st.error("Por favor, ingresa un texto para identificar las palabras clave.")
