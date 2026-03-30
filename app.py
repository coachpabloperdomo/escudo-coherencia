import streamlit as st
import urllib.parse

# 1. Configuración de Página
st.set_page_config(page_title="Partnership Shield", page_icon="🛡️", layout="wide")

# Estilo Mejorado con Corrección de Legibilidad
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { background-color: #D4AF37; color: black; font-weight: bold; border-radius: 10px; height: 3.5em; width: 100%; border: none; }
    .gold-text { color: #D4AF37; font-family: 'Georgia', serif; text-align: center; }
    .card-red { background-color: #2b0b0b; padding: 25px; border-radius: 15px; border: 1px solid #ff4b4b; margin-bottom: 25px; }
    .card-yellow { background-color: #2b260b; padding: 25px; border-radius: 15px; border: 1px solid #f1c40f; margin-bottom: 25px; }
    .card-green { background-color: #0b2b0f; padding: 25px; border-radius: 15px; border: 1px solid #2ecc71; margin-bottom: 25px; }
    .header-box { display: flex; justify-content: center; align-items: center; margin-bottom: 10px; }
    
    /* RECUADRO IMPORTANTE CORREGIDO */
    .info-box-custom { 
        background-color: #1c1c1c; 
        padding: 20px; 
        border-radius: 10px; 
        border: 1px solid #D4AF37; 
        margin: 15px 0;
        text-align: center;
    }
    .info-box-custom b { color: #D4AF37; font-size: 1.1rem; }
    .info-box-custom p { color: #ffffff !important; margin-top: 10px; }
    </style>
    """, unsafe_allow_html=True)

escudo_svg = """
<svg viewBox="-30 -30 572 572" style="width: 55px; height: 55px; fill: #D4AF37; margin-right: 15px; flex-shrink: 0; overflow: visible;">
<path d="M466.5 83.71l-192-80a48.15 48.15 0 0 0-36.94 0l-192 80A48.07 48.07 0 0 0 16 128v192c0 148.6 125.1 267.7 230.1 289.8a48.1 48.1 0 0 0 19.8 0C370.9 587.7 496 468.6 496 320V128a48.07 48.07 0 0 0-29.5-44.29zM256 553.7V64.21l164.5 68.52V320c0 102.7-88.7 186-164.5 208.7z"/>
</svg>
"""

if 'pantalla' not in st.session_state:
    st.session_state.pantalla = 'radar'

# --- PANTALLA 1: EL RADAR ---
if st.session_state.pantalla == 'radar':
    st.markdown(f'<div class="header-box">{escudo_svg}<h1 style="color: #D4AF37; margin: 0;">PARTNERSHIP SHIELD</h1></div>', unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #C0C0C0; font-style: italic;'>Arquitectura del Comportamiento Humano & Estrategia Biopsicológica</p>", unsafe_allow_html=True)
    
    st.write("---")
    escenario = st.radio("**Seleccioná el escenario a auditar:**", ["Relación de Pareja", "Sociedad Comercial", "Vínculo Mixto"], horizontal=True)
    
    st.markdown("<h3 class='gold-text'>📡 Radar de Diagnóstico</h3>", unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    with c1:
        f_cancel = st.slider("Incumplimiento de acuerdos (Frecuencia)", 0, 10, 2)
        claridad = st.select_slider("Acceso a Información / Transparencia", options=["Total", "Zonas Grises", "Opacidad"])
        triangulacion = st.toggle("Presencia de terceros (Triangulación)")
    with c2:
        gaslighting = st.toggle("Invalidación / Gaslighting")
        culpa = st.toggle("Transferencia de Culpa / Proyección")
        persuasion_neg = st.toggle("Amenazas o Promesas incumplidas")

    if st.button("OBTENER DIAGNÓSTICO ESTRATÉGICO"):
        score = f_cancel + (10 if claridad == "Opacidad" else 5 if claridad == "Zonas Grises" else 0)
        score += (7 if triangulacion else 0) + (15 if gaslighting else 0) + (8 if culpa else 0) + (10 if persuasion_neg else 0)
        st.session_state.score = score
        st.session_state.escenario = escenario
        st.session_state.pantalla = 'diagnostico'
        st.rerun()

# --- PANTALLA 2: DIAGNÓSTICO PROFUNDO ---
elif st.session_state.pantalla == 'diagnostico':
    st.markdown(f'<div class="header-box">{escudo_svg}<h1 style="color: #D4AF37; margin: 0;">ANÁLISIS DE SITUACIÓN</h1></div>', unsafe_allow_html=True)
    
    score = st.session_state.score
    escenario = st.session_state.escenario

    if score >= 25:
        st.markdown(f"<div class='card-red'><h2 style='color: #ff4b4b; margin:0;'>🚨 ESTATUS: VACIADO CRÍTICO ({score}/50)</h2><p style='color:white;'>Se detectó una dinámica de extracción activa de valor en tu {escenario}.</p></div>", unsafe_allow_html=True)
        with st.expander("🔍 Desglose del Mecanismo de Extracción"):
            st.write("Tu contraparte está utilizando técnicas de **Invalidación Sistemática**. Esto genera que pierdas tu centro operativo.")
    else:
        st.markdown(f"<div class='card-yellow'><h2 style='color: #f1c40f; margin:0;'>⚠️ ESTATUS: DESBALANCE ({score}/50)</h2><p style='color:white;'>Vínculo con pérdida de coherencia en {escenario}.</p></div>", unsafe_allow_html=True)
        with st.expander("🔍 Análisis de la Dinámica"):
            st.write("Existen 'Zonas Grises' donde el **Código Persuasión** es tu mejor herramienta para recuperar autoridad.")

    st.write("---")
    st.markdown("<h3 style='text-align:center;'>¿Cómo recuperar el control de tu territorio?</h3>", unsafe_allow_html=True)
    st.write("He preparado un documento técnico con los pasos exactos para reprogramar esta dinámica y aplicar el Escudo de Coherencia.")
    
    if st.button("DESCARGAR HOJA DE RUTA Y SOLICITAR AUDITORÍA"):
        st.session_state.pantalla = 'mentoria'
        st.rerun()

    if st.button("← Volver al Radar"):
        st.session_state.pantalla = 'radar'
        st.rerun()

# --- PANTALLA 3: MENTORÍA & FORMULARIO ---
elif st.session_state.pantalla == 'mentoria':
    st.markdown(f'<div class="header-box">{escudo_svg}<h1 style="color: #D4AF
