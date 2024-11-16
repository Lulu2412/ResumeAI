import streamlit as st
from openai import OpenAI

# Show title and description.
st.title("💬 ResumeAI")
st.write(
    "Esta aplicación te permite generar resúmenes automáticos de textos, extraer las ideas clave y visualizar los conceptos más importantes de manera clara y sencilla."

"Con esta herramienta, podrás transformar textos largos en resúmenes concisos, identificar las palabras clave y crear cuadros conceptuales para una comprensión más profunda."

"Simplifica tu proceso de lectura y análisis con nuestra app: resume, extrae palabras clave y organiza la información en cuadros conceptuales, todo en un solo clic."
)
# Instalar dependencias
!python -m spacy download es_core_news_sm

# Código de la IA
import streamlit as st
from transformers import pipeline
from keybert import KeyBERT
import spacy

def cargar_modelos():
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    kw_model = KeyBERT()
    nlp = spacy.load("es_core_news_sm")
    return summarizer, kw_model, nlp

def generar_resumen(texto, summarizer):
    resumen = summarizer(texto, max_length=150, min_length=30, do_sample=False)
    return resumen[0]['summary_text']

def extraer_palabras_clave(texto, kw_model):
    palabras_clave = kw_model.extract_keywords(
        texto, keyphrase_ngram_range=(1, 2), stop_words='spanish'
    )
    return [kw[0] for kw in palabras_clave]

def generar_cuadro_conceptual(texto, nlp):
    relaciones = []
    doc = nlp(texto)
    for token in doc:
        if token.dep_ in ["nsubj", "dobj"]:
            relaciones.append(f"{token.text} ({token.dep_}) -> {token.head.text}")
    return relaciones

def main():
    st.title("Asistente de Escritura Inteligente")
    summarizer, kw_model, nlp = cargar_modelos()
    texto_largo = st.text_area("Introduce el texto (máximo 5000 palabras)", height=300)
    opcion = st.selectbox("Selecciona la tarea:", ["Resumen", "Palabras clave", "Cuadro conceptual"])
    if st.button("Procesar"):
        if opcion == "Resumen":
            resultado = generar_resumen(texto_largo, summarizer)
            st.subheader("Resumen")
            st.write(resultado)
        elif opcion == "Palabras clave":
            resultado = extraer_palabras_clave(texto_largo, kw_model)
            st.subheader("Palabras clave")
            st.write(resultado)
        elif opcion == "Cuadro conceptual":
            resultado = generar_cuadro_conceptual(texto_largo, nlp)
            st.subheader("Cuadro conceptual")
            st.write(resultado)
