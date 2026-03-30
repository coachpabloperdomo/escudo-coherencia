import streamlit as st
import urllib.parse

# 1. Configuración de Página
st.set_page_config(page_title="Partnership Shield", page_icon="🛡️", layout="wide")

# Estilos CSS
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { background-color: #D4AF37; color: black; font-weight: bold; border-radius: 10px; height: 3.5em; width: 100%; border: none; }
    .gold-text { color: #D4AF37; font-family: 'Georgia', serif; text-align: center; }
    .header-box { display: flex; justify-content: center; align-items: center; margin-bottom: 10px; }
    .info-box-custom { background-color: #1c1c1c; padding: 20px; border-radius: 10px; border: 1px solid #D4AF37; margin: 15px 0; text-align: center; }
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
    
    # --- BLOQUE DE SLIDERS AFILADOS ---
    c1, c2 = st.columns(2)
    with c1:
        f_cancel = st.slider("Incumplimiento de Acuerdos", 0, 10, 2, 
                             help="¿Con qué frecuencia la otra parte rompe promesas o compromisos (por más pequeños que sean)?")
        
        friccion = st.slider("Fricción Operativa (Altercados)", 0, 10, 2,
                             help="Nivel de discusiones constantes o discrepancias por temas triviales que desgastan la energía.")
        
    with c2:
        erosion = st.slider("Erosión del Valor (Desvalorización)", 0, 10, 2,
                            help="¿Sentís que tu palabra, tiempo o esfuerzo han perdido peso frente a la otra parte?")
        
        opacidad = st.select_slider("Hermetismo / Opacidad", options=["Transparencia", "Zonas Grises", "Opacidad Total"],
                                    help="¿Qué tanto sentís que se te oculta información clave o que hay 'secretos' en el ambiente?")

    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- BLOQUE DE TOGGLES CON CÓDIGO PERSUASIÓN ---
    t1, t2 = st.columns(2)
    with t1:
        gaslighting = st.toggle("Gaslighting / Invalidación", 
                                help="¿Te dicen que 'estás loco/a', que 'no fue así' o invalidan tus emociones constantemente?")
        
        culpa = st.toggle("Transferencia de Culpa (Proyección)", 
                          help="¿La otra parte siempre encuentra la forma de que vos seas el responsable de sus errores?")
        
        aislamiento = st.toggle("Aislamiento Sugerido", 
                                help="¿Existen críticas o presiones sutiles para que te alejes de amigos, socios o familia?")

    with t2:
        amenazas = st.toggle("Amenazas / Promesas Falsas", 
                             help="Uso de ultimátums o promesas de cambio que nunca se materializan para mantenerte en el vínculo.")
        
        refuerzo = st.toggle("Refuerzo Intermitente (Montaña Rusa)", 
                             help="Ciclos de afecto extremo seguidos de indiferencia total o castigo con el silencio.")
        
        triangulacion = st.toggle("Presencia de Terceros (Triangulación)", 
                                  help="¿La otra parte mete a terceros (ex, amigos, otros socios) en la dinámica para generarte inseguridad?")

    if st.button("OBTENER DIAGNÓSTICO ESTRATÉGICO"):
        # Recálculo del Score con las nuevas variables
        score = f_cancel + friccion + erosion + (10 if opacidad == "Opacidad Total" else 5 if opacidad == "Zonas Grises" else 0)
        score += (10 if gaslighting else 0) + (8 if culpa else 0) + (10 if amenazas else 0) + (8 if aislamiento else 0) + (10 if refuerzo else 0) + (7 if triangulacion else 0)
        
        st.session_state.score = score
        st.session_state.escenario = escenario
        st.session_state.pantalla = 'diagnostico'
        st.rerun()

# --- (Las pantallas de diagnóstico y mentoría se mantienen igual pero con el score actualizado) ---
# ... (Resto del código de las pantallas 2 y 3)
