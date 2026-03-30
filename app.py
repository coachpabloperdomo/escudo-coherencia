import streamlit as st
import urllib.parse

# 1. Configuración de Página
st.set_page_config(page_title="Partnership Shield", page_icon="🛡️", layout="wide")

# Estilo Limpio
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { background-color: #D4AF37; color: black; font-weight: bold; border-radius: 10px; height: 3em; width: 100%; }
    .gold-text { color: #D4AF37; font-family: 'Georgia', serif; text-align: center; }
    .card-red { background-color: #2b0b0b; padding: 25px; border-radius: 15px; border: 1px solid #ff4b4b; margin-bottom: 25px; color: #ffffff; }
    .card-yellow { background-color: #2b260b; padding: 25px; border-radius: 15px; border: 1px solid #f1c40f; margin-bottom: 25px; color: #ffffff; }
    .card-green { background-color: #0b2b0f; padding: 25px; border-radius: 15px; border: 1px solid #2ecc71; margin-bottom: 25px; color: #ffffff; }
    .card-red p, .card-yellow p, .card-green p { color: #ffffff !important; font-size: 1.1rem; }
    .mensaje-copiar { background-color: #121212; border-left: 5px solid #D4AF37; padding: 20px; font-family: monospace; color: #D4AF37; margin: 15px 0; border-radius: 8px; }
    </style>
    """, unsafe_allow_html=True)

# Encabezado HTML unificado para la Pantalla 1 (Radar) - Centrado y sin cortes
header_radar = """
<div style="display: flex; justify-content: center; align-items: center; margin-top: 10px; margin-bottom: 5px;">
    <svg viewBox="-20 -20 552 552" style="width: 55px; height: 55px; fill: #D4AF37; margin-right: 15px; flex-shrink: 0; overflow: visible;">
        <path d="M466.5 83.71l-192-80a48.15 48.15 0 0 0-36.94 0l-192 80A48.07 48.07 0 0 0 16 128v192c0 148.6 125.1 267.7 230.1 289.8a48.1 48.1 0 0 0 19.8 0C370.9 587.7 496 468.6 496 320V128a48.07 48.07 0 0 0-29.5-44.29zM256 553.7V64.21l164.5 68.52V320c0 102.7-88.7 186-164.5 208.7z"/>
    </svg>
    <h1 style="color: #D4AF37; margin: 0; padding: 0; font-size: 2.8rem; line-height: 1;">PARTNERSHIP SHIELD</h1>
</div>
"""

# Encabezado HTML unificado para la Pantalla 2 (Solución)
header_solucion = """
<div style="display: flex; justify-content: center; align-items: center; margin-top: 10px; margin-bottom: 20px;">
    <svg viewBox="-20 -20 552 552" style="width: 55px; height: 55px; fill: #D4AF37; margin-right: 15px; flex-shrink: 0; overflow: visible;">
        <path d="M466.5 83.71l-192-80a48.15 48.15 0 0 0-36.94 0l-192 80A48.07 48.07 0 0 0 16 128v192c0 148.6 125.1 267.7 230.1 289.8a48.1 48.1 0 0 0 19.8 0C370.9 587.7 496 468.6 496 320V128a48.07 48.07 0 0 0-29.5-44.29zM256 553.7V64.21l164.5 68.52V320c0 102.7-88.7 186-164.5 208.7z"/>
    </svg>
    <h1 style="color: #D4AF37; margin: 0; padding: 0; font-size: 2.8rem; line-height: 1;">TU ESTRATEGIA DE DEFENSA</h1>
</div>
"""

if 'pantalla' not in st.session_state:
    st.session_state.pantalla = 'radar'

# --- PANTALLA 1: EL RADAR ---
if st.session_state.pantalla == 'radar':
    
    # Renderizamos el título centrado
    st.markdown(header_radar, unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #C0C0C0; font-style: italic; margin-bottom: 30px;'>Arquitectura del Comportamiento Humano & Estrategia Biopsicológica</p>", unsafe_allow_html=True)
    
    st.write("---")
    escenario = st.radio("**Escenario a auditar:**", ["Relación de Pareja", "Sociedad Comercial", "Vínculo Mixto"], horizontal=True)
    
    st.markdown("<h3 class='gold-text'>📡 Radar de Diagnóstico</h3>", unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    with c1:
        f_cancel = st.slider("Incumplimiento de acuerdos (0-10)", 0, 10, 2)
        claridad = st.select_slider("Acceso a Información", options=["Transparencia", "Zonas Grises", "Opacidad Total"])
        triangulacion = st.toggle("Triangulación con terceros")
    with c2:
        gaslighting = st.toggle("Gaslighting / Invalidez")
        culpa = st.toggle("Transferencia de Culpa")
        persuasion_neg = st.toggle("Amenazas / Promesas falsas")

    if st.button("OBTENER DIAGNÓSTICO Y SOLUCIÓN"):
        score = f_cancel + (10 if claridad == "Opacidad Total" else 5 if claridad == "Zonas Grises" else 0)
        score += (7 if triangulacion else 0) + (15 if gaslighting else 0) + (8 if culpa else 0) + (7 if persuasion_neg else 0)
        st.session_state.score = score
        st.session_state.escenario = escenario
        st.session_state.pantalla = 'solucion'
        st.rerun()

# --- PANTALLA 2: LA SOLUCIÓN ---
elif st.session_state.pantalla == 'solucion':
    score = st.session_state.score
    escenario = st.session_state.escenario
    
    # Renderizamos el título centrado para la solución
    st.markdown(header_solucion, unsafe_allow_html=True)
    
    if score >= 20:
        st.markdown(f"<div class='card-red'><h2 style='color: #ff4b4b; margin-top:0;'>🚨 ESTATUS: VACIADO CRÍTICO</h2><p><b>Análisis:</b> Se detectó una dinámica de extracción activa en tu <b>{escenario}</b>.</p></div>", unsafe_allow_html=True)
        st.write("### 🛠️ Orientación Inmediata: Protocol
