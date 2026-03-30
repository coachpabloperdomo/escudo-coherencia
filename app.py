import streamlit as st
import urllib.parse

# 1. Configuración de Página
st.set_page_config(page_title="Partnership Shield", page_icon="🛡️", layout="wide")

# Estilos CSS Profesionales
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { background-color: #D4AF37; color: black; font-weight: bold; border-radius: 10px; height: 3.5em; width: 100%; border: none; }
    .gold-text { color: #D4AF37; font-family: 'Georgia', serif; text-align: center; }
    .header-box { display: flex; justify-content: center; align-items: center; margin-bottom: 10px; }
    
    /* Colores de Tarjetas con Texto Forzado en Blanco */
    .card-red { background-color: #2b0b0b; padding: 25px; border-radius: 15px; border: 1px solid #ff4b4b; margin-bottom: 25px; border-left: 10px solid #ff4b4b; color: #ffffff !important; }
    .card-yellow { background-color: #2b260b; padding: 25px; border-radius: 15px; border: 1px solid #f1c40f; margin-bottom: 25px; border-left: 10px solid #f1c40f; color: #ffffff !important; }
    .card-green { background-color: #0b2b0f; padding: 25px; border-radius: 15px; border: 1px solid #2ecc71; margin-bottom: 25px; border-left: 10px solid #2ecc71; color: #ffffff !important; }
    
    .card-red h2, .card-yellow h2, .card-green h2, .card-red p, .card-yellow p, .card-green p { color: #ffffff !important; }

    .tactic-box { background-color: #161b22; padding: 15px; border-radius: 8px; border-top: 2px solid #D4AF37; margin-top: 10px; color: #f0f0f0 !important; font-weight: 500; }
    
    .download-box { background: linear-gradient(145deg, #1e1e1e, #121212); border: 1px dashed #D4AF37; padding: 20px; border-radius: 15px; text-align: center; margin-top: 20px; }
    
    .wa-button { background-color: #25D366; color: white !important; padding: 15px; border-radius: 10px; text-align: center; font-weight: bold; text-decoration: none; display: block; margin-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

escudo_svg = """
<svg viewBox="-30 -30 572 572" style="width: 55px; height: 55px; fill: #D4AF37; margin-right: 15px; flex-shrink: 0; overflow: visible;">
<path d="M466.5 83.71l-192-80a48.15 48.15 0 0 0-36.94 0l-192 80A48.07 48.07 0 0 0 16 128v192c0 148.6 125.1 267.7 230.1 289.8a48.1 48.1 0 0 0 19.8 0C370.9 587.7 496 468.6 496 320V128a48.07 48.07 0 0 0-29.5-44.29zM256 553.7V64.21l164.5 68.52V320c0 102.7-88.7 186-164.5 208.7z"/>
</svg>
"""

CONTENIDOS = {
    "Relación de Pareja": {
        "Crítico": {"titulo": "VACIADO CRÍTICO: Crisis de Confianza", "diag": "El sistema está en modo supervivencia por falta de previsibilidad.", "codigo": "Blindaje de Salida
