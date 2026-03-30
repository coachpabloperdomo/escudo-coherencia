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
    .card-red { background-color: #2b0b0b; padding: 25px; border-radius: 15px; border: 1px solid #ff4b4b; margin-bottom: 25px; }
    .card-yellow { background-color: #2b260b; padding: 25px; border-radius: 15px; border: 1px solid #f1c40f; margin-bottom: 25px; }
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

# --- PANTALLA 1: EL RADAR (AFILADO) ---
if st.session_state.pantalla == 'radar':
    st.markdown(f'<div class="header-box">{escudo_svg}<h1 style="color: #D4AF37; margin: 0;">PARTNERSHIP SHIELD</h1></div>', unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #C0C0C0; font-style: italic;'>Arquitectura del Comportamiento Humano & Estrategia Biopsicológica</p>", unsafe_allow_html=True)
    
    st.write("---")
    escenario = st.radio("**Seleccioná el escenario a auditar:**", ["Relación de Pareja", "Sociedad Comercial", "Vínculo Mixto"], horizontal=True)
    
    st.markdown("<h3 class='gold-text'>📡 Radar de Diagnóstico</h3>", unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    with c1:
        f_cancel = st.slider("Incumplimiento de Acuerdos", 0, 10, 2, help="Frecuencia con la que la otra parte rompe promesas o compromisos.")
        friccion = st.slider("Fricción Operativa (Altercados)", 0, 10, 2, help="Nivel de discusiones constantes por temas triviales que desgastan.")
    with c2:
        erosion = st.slider("Erosión del Valor (Desvalorización)", 0, 10, 2, help="¿Sentís que tu opinión o esfuerzo han perdido peso ante el otro?")
        opacidad = st.select_slider("Hermetismo / Opacidad", options=["Transparencia", "Zonas Grises", "Opacidad Total"], help="¿Qué tanto sentís que se te oculta información clave?")

    st.markdown("<br>", unsafe_allow_html=True)
    t1, t2 = st.columns(2)
    with t1:
        gaslighting = st.toggle("Gaslighting / Invalidación", help="¿Invalidan tus emociones o te dicen que 'no fue así' constantemente?")
        culpa = st.toggle("Transferencia de Culpa", help="¿Sos siempre el responsable de los errores ajenos?")
        aislamiento = st.toggle("Aislamiento Sugerido", help="Críticas sutiles para alejarte de tus amigos o familia.")
    with t2:
        amenazas = st.toggle("Amenazas / Promesas Falsas", help="Ultimátums o promesas de cambio que nunca llegan.")
        refuerzo = st.toggle("Refuerzo Intermitente", help="Ciclos de afecto extremo seguidos de indiferencia o castigo.")
        triangulacion = st.toggle("Presencia de Terceros", help="Mencionar a terceros para generar inseguridad o competencia.")

    if st.button("OBTENER DIAGNÓSTICO ESTRATÉGICO"):
        score = f_cancel + friccion + erosion + (10 if opacidad == "Opacidad Total" else 5 if opacidad == "Zonas Grises" else 0)
        score += (10 if gaslighting else 0) + (8 if culpa else 0) + (10 if amenazas else 0) + (8 if aislamiento else 0) + (10 if refuerzo else 0) + (7 if triangulacion else 0)
        st.session_state.score = score
        st.session_state.escenario = escenario
        st.session_state.pantalla = 'diagnostico'
        st.rerun()

# --- PANTALLA 2: DIAGNÓSTICO ---
elif st.session_state.pantalla == 'diagnostico':
    st.markdown(f'<div class="header-box">{escudo_svg}<h1 style="color: #D4AF37; margin: 0;">ANÁLISIS DE SITUACIÓN</h1></div>', unsafe_allow_html=True)
    score = st.session_state.score
    escenario = st.session_state.escenario

    if score >= 35:
        st.markdown(f"<div class='card-red'><h2 style='color: #ff4b4b; margin:0;'>🚨 ESTATUS: VACIADO CRÍTICO ({score})</h2><p style='color:white;'>Se detectó una dinámica de extracción activa en tu {escenario}.</p></div>", unsafe_allow_html=True)
        with st.expander("🔍 Ver Análisis Detallado"):
            st.write("Tu centro operativo está comprometido. La contraparte ha logrado instalar un sistema de deuda emocional o profesional que te impide tomar decisiones racionales.")
    else:
        st.markdown(f"<div class='card-yellow'><h2 style='color: #f1c40f; margin:0;'>⚠️ ESTATUS: DESBALANCE ({score})</h2><p style='color:white;'>Vínculo con pérdida de coherencia estratégica en {escenario}.</p></div>", unsafe_allow_html=True)
        with st.expander("🔍 Ver Análisis Detallado"):
            st.write("Existen filtraciones de autoridad. Si no se corrigen los códigos de comunicación ahora, el vínculo evolucionará hacia un vaciado total.")
    
    st.write("---")
    st.markdown("<h3 style='text-align:center;'>¿Cómo recuperar el control de tu territorio?</h3>", unsafe_allow_html=True)
    st.write("Basado en tu diagnóstico, he preparado una Hoja de Ruta de Ingeniería Conductual para reprogramar esta dinámica.")
    
    if st.button("DESCARGAR HOJA DE RUTA Y SOLICITAR AUDITORÍA"):
        st.session_state.pantalla = 'mentoria'
        st.rerun()

    if st.button("← Volver al Radar"):
        st.session_state.pantalla = 'radar'
        st.rerun()

# --- PANTALLA 3: MENTORÍA ---
elif st.session_state.pantalla == 'mentoria':
    st.markdown(f'<div class="header-box">{escudo_svg}<h1 style="color: #D4AF37; margin: 0;">PROGRAMA DE INGENIERÍA CONDUCTUAL</h1></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### Mentoría: El Arte de la Coherencia")
        st.write("""
        Este no es un proceso de coaching tradicional. Es un programa de **Ingeniería del Comportamiento** diseñado para que dejes de ser un 'jugador pasivo' en tu propia realidad.
        
        **¿Qué abarcamos?**
        - **Blindaje Emocional:** Reprogramación subconsciente para anular el efecto del gaslighting.
        - **Arquitectura de Poder:** Reconfiguración de los códigos de comunicación en tu relación o sociedad.
        - **Persuasión Biopsicológica:** Cómo instalar nuevas ideas en el entorno sin generar resistencia.
        
        **Valor del Programa:** Basado en la complejidad de la auditoría.
        """)
        
        with st.form("form_final_v7"):
            st.markdown("#### Aplicar a la Mentoría con Pablo Perdomo")
            nombre = st.text_input("Nombre Completo*")
            situacion = st.text_area("Resumen de situación*")
            submit = st.form_submit_button("ENVIAR SOLICITUD A WHATSAPP")
            
            if submit:
                if nombre and situacion:
                    msg = f"Hola Pablo, mi código es #COHERENCIA2026.\\nNombre: {nombre}\\nScore: {st.session_state.score}\\nSituación: {situacion}"
                    link_wa = f"https://wa.me/59899816392?text={urllib.parse.quote(msg)}"
                    st.balloons()
                    st.markdown(f'<a href="{link_wa}" target="_blank" style="text-decoration:none;"><div style="background-color:#25D366;color:white;padding:15px;border-radius:10px;text-align:center;font-weight:bold;">📩 CONTACTAR POR WHATSAPP</div></a>', unsafe_allow_html=True)
                else:
                    st.error("Por favor, completá los campos obligatorios.")

    with col2:
        st.markdown("""
            <div style="background-color: #D4AF37; color: black; padding: 40px 20px; border-radius: 15px; text-align: center; font-weight: bold; margin-bottom: 20px;">
                <span style="font-size: 3rem;">📄</span><br>TU HOJA DE RUTA<br>ESTÁ LISTA
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
            <div class="info-box-custom">
                <b>⚠️ IMPORTANTE:</b>
                <p>Las vacantes para mentoría personalizada son limitadas para garantizar el seguimiento biopsicológico de cada caso.</p>
            </div>
        """, unsafe_allow_html=True)

    if st.button("← Volver al Diagnóstico"):
        st.session_state.pantalla = 'diagnostico'
        st.rerun()

st.markdown("<p style='text-align: center; font-size: 0.8rem; margin-top: 50px; color: #555;'>Partnership Shield © 2026</p>", unsafe_allow_html=True)
