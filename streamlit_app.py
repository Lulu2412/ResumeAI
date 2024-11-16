import streamlit as st
from openai import OpenAI

# Show title and description.
st.title("💬 ResumeAI")
st.write(
    "Esta aplicación te permite generar resúmenes automáticos de textos, extraer las ideas clave y visualizar los conceptos más importantes de manera clara y sencilla."

"Con esta herramienta, podrás transformar textos largos en resúmenes concisos, identificar las palabras clave y crear cuadros conceptuales para una comprensión más profunda."

"Simplifica tu proceso de lectura y análisis con nuestra app: resume, extrae palabras clave y organiza la información en cuadros conceptuales, todo en un solo clic."
)
import streamlit as st
from modelo import generar_resumen, generar_cuadro_conceptual, identificar_palabras_clave

# Título de la aplicación
st.title("Aplicación de Resúmenes, Cuadros Conceptuales y Palabras Clave")

# Descripción
st.write("Este es un asistente interactivo que te ayudará a generar resúmenes automáticos, cuadros conceptuales y a identificar palabras clave de tus textos.")

# Entrada de texto
texto_entrada = st.text_area("Introduce el texto para analizar", height=200)

# Botones de acción
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
# Modelo de IA: Generación de Resúmenes, Cuadros Conceptuales y Palabras Clave

from transformers import pipeline

# Cargar los modelos para resumen, cuadro conceptual y extracción de palabras clave
resumen_modelo = pipeline("summarization")
keywords_modelo = pipeline("ner")

def generar_resumen(texto):
    resumen = resumen_modelo(texto)
    return resumen[0]['summary_text']

def generar_cuadro_conceptual(texto):
    # Aquí puedes agregar tu lógica para generar cuadros conceptuales.
    # Este es solo un ejemplo de cómo podrías hacerlo.
    return f"Cuadro conceptual generado para: {texto[:50]}..."  # Lógica de ejemplo

def identificar_palabras_clave(texto):
    # Aquí usamos el modelo NER para extraer entidades como ejemplo de palabras clave
    palabras_clave = [entidad['word'] for entidad in keywords_modelo(texto)]
    return palabras_clave
streamlit
transformers
torch
