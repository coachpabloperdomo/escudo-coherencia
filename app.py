import streamlit as st
import urllib.parse

# 1. Configuración de Página
st.set_page_config(page_title="Partnership Shield", page_icon="🛡️", layout="wide")

# Estilo y Escudo Dorado con Contenedor Seguro
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { background-color: #D4AF37; color: black; font-weight: bold; border-radius: 10px; height: 3em; width: 100%; }
    .gold-text { color: #D4AF37; font-family: 'Georgia', serif; text-align: center; }
    
    /* Contenedor del Título para evitar recortes de padding */
    .header-container {
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 10px;
        margin-bottom: 10px;
        overflow: visible;
    }

    /* Escudo Dorado SVG con margen de seguridad */
    .header-shield {
        fill: #D4AF37;
        width: 45px;
        height: 45px;
        margin-right: 20px;
        flex-shrink: 0;
        filter: drop-shadow(0px 0px 3px rgba(212, 175, 55, 0.3));
    }

    .card-red { background-color: #2b0b0b; padding: 25px; border-radius: 15px; border: 1px solid #ff4b4b; margin-bottom: 25px; color: #ffffff; }
    .card-yellow { background-color: #2b260b; padding: 25px; border-radius: 15px; border: 1px solid #f1c40f; margin-bottom: 25px; color: #ffffff; }
    .card-green { background-color: #0b2b0f; padding: 25px; border-radius: 15px; border: 1px solid #2ecc71; margin-bottom: 25px; color: #ffffff; }
    .card-red p, .card-yellow p, .card-green p { color: #ffffff !important; font-size: 1.1rem; }
    .mensaje-copiar { background-color: #121212; border-left: 5px solid #D4AF37; padding: 20px; font-family: monospace; color: #D4AF37; margin: 15px 0; border-radius: 8px; }
    </style>
    """, unsafe_allow_html=True)

# SVG del Escudo (Optimizado)
escudo_svg = """
<svg class="header-shield" viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg">
<path d="M466.5 83.71l-192-80a48.15 48.15 0 0 0-36.94 0l-192 80A48.07 48.07 0 0 0 16 128v192c0 148.6 125.1 267.7 230.1 289.8a48.1 48.1 0 0 0 19.8 0C370.9 587.7 496 468.6 496 320V128a48.07 48.07 0 0 0-29.5-44.29zM256 553.7V64.21l164.5 68.52V320c0 102.7-88.7 186-164.5 208.7z"/>
</svg>
"""

if 'pantalla' not in st.session_state:
    st.session_state.pantalla = 'radar'

# --- PANTALLA 1: EL RADAR ---
if st.session_state.pantalla == 'radar':
    st.markdown(f"""
        <div class="header-container">
            {escudo_svg}
            <h1 style="color: #D4AF37; margin: 0; padding: 0;">PARTNERSHIP SHIELD</h1>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #C0C0C0; font-style: italic;'>Arquitectura del Comportamiento Humano & Estrategia Biopsicológica</p>", unsafe_allow_html=True)
    
    st.write("---")
    escenario = st.radio("**Seleccioná el escenario a auditar:**", ["Relación de Pareja", "Sociedad Comercial", "Vínculo Mixto"], horizontal=True)
    
    st.markdown("<h3 class='gold-text'>📡 Radar de Diagnóstico</h3>", unsafe_allow_html=True)
