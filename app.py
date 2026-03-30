import streamlit as st
import urllib.parse

# 1. Configuración de Página
st.set_page_config(page_title="Partnership Shield", page_icon="🛡️", layout="wide")

# Estilo Mejorado
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { background-color: #D4AF37; color: black; font-weight: bold; border-radius: 10px; height: 3.5em; width: 100%; border: none; }
    .gold-text { color: #D4AF37; font-family: 'Georgia', serif; text-align: center; }
    .card-red { background-color: #2b0b0b; padding: 25px; border-radius: 15px; border: 1px solid #ff4b4b; margin-bottom: 25px; }
    .card-yellow { background-color: #2b260b; padding: 25px; border-radius: 15px; border: 1px solid #f1c40f; margin-bottom: 25px; }
    .card-green { background-color: #0b2b0f; padding: 25px; border-radius: 15px; border: 1px solid #2ecc71; margin-bottom: 25px; }
    .header-box { display: flex; justify-content: center; align-items: center; margin-bottom: 10px; }
    .info-box { background-color: #1e2127; padding: 20px; border-radius: 10px; border-left: 5px solid #D4AF37; margin: 15px 0; }
    </style>
    """, unsafe_allow_html=True)

escudo_svg = """
<svg viewBox="-30 -30 572 572" style="width: 55px; height: 55px; fill: #D4AF37; margin-right: 15px; flex-shrink: 0; overflow: visible;">
<path d="M466.5 83.71l-192-80a48.15 48.15 0 0 0-36.94 0l-192 80A48.07 48.07 0 0 0 16 128v192c0 148.6 125.1 267.7 230.1 289.8a48.1 48.1 0 0 0 19.8 0C370.9 587.7 496 468.6 496 320V128a48.07 48.07 0 0 0-29.5-44.29zM256 553.7V64.21l164.5 68.52V320c0 102.7-88.7 186-164.5 208.7z"/>
</svg>
"""

# Manejo de navegación
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
        # Cálculo de Score (Valor Perdido)
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

    # Lógica de Semáforo
    if score >= 25:
        st.markdown(f"<div class='card-red'><h2 style='color: #ff4b4b; margin:0;'>🚨 ESTATUS: VACIADO CRÍTICO ({score}/50)</h2><p style='color:white;'>Se detectó una dinámica de extracción activa de valor en tu {escenario}. Estás operando bajo un déficit biopsicológico grave.</p></div>", unsafe_allow_html=True)
        with st.expander("🔍 Desglose del Mecanismo de Extracción"):
            st.write("Tu contraparte está utilizando técnicas de **Invalidación Sistemática**. Esto genera que pierdas tu centro operativo, permitiendo que la otra persona tome el control de la narrativa y de tus recursos (emocionales o financieros).")
        st.info("**Protocolo de Coherencia:** Es vital que cortes la filtración de información. Usá el mensaje de escudo que vimos anteriormente.")
    else:
        st.markdown(f"<div class='card-yellow'><h2 style='color: #f1c40f; margin:0;'>⚠️ ESTATUS: DESBALANCE ({score}/50)</h2><p style='color:white;'>Vínculo con pérdida de coherencia en {escenario}.</p></div>", unsafe_allow_html=True)
        with st.expander("🔍 Análisis de la Dinámica"):
            st.write("Existen 'Zonas Grises' donde la comunicación se vuelve un campo de batalla. El **Patrón Interruptor** es tu mejor herramienta aquí para recuperar autoridad.")

    st.write("---")
    st.markdown("<h3 style='text-align:center;'>¿Cómo recuperar el control de tu territorio?</h3>", unsafe_allow_html=True)
    st.write("He preparado un documento técnico con los pasos exactos para reprogramar esta dinámica y aplicar el Escudo de Coherencia según tu diagnóstico.")
    
    if st.button("DESCARGAR HOJA DE RUTA Y SOLICITAR AUDITORÍA"):
        st.session_state.pantalla = 'mentoria'
        st.rerun()

    if st.button("← Volver al Radar"):
        st.session_state.pantalla = 'radar'
        st.rerun()

# --- PANTALLA 3: MENTORÍA & FORMULARIO ---
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
        
        with st.form("form_final"):
            st.markdown("#### Aplicar a la Mentoría con Pablo Perdomo")
            nombre = st.text_input("Nombre Completo*")
            situacion = st.text_area("Breve resumen de la situación que querés transformar*")
            submit = st.form_submit_button("ENVIAR SOLICITUD A WHATSAPP")
            
            if submit:
                if nombre and situacion:
                    msg = f"Hola Pablo, vengo de Partnership Shield.\nNombre: {nombre}\nScore: {st.session_state.score}\nSituación: {situacion}"
                    link_wa = f"https://wa.me/59899816392?text={urllib.parse.quote(msg)}"
                    st.success("¡Solicitud preparada!")
                    st.markdown(f'<a href="{link_wa}" target="_blank" style="text-decoration:none;"><div style="background-color:#25D366;color:white;padding:15px;border-radius:10px;text-align:center;font-weight:bold;">📩 CONTACTAR POR WHATSAPP</div></a>', unsafe_allow_html=True)
                else:
                    st.error("Por favor, completá los campos obligatorios.")

    with col2:
        st.image("https://via.placeholder.com/300x400/0e1117/D4AF37?text=Ebook+Placeholder", caption="Tu Hoja de Ruta Personalizada")
        st.markdown("<div class='info-box'><b>Importante:</b> Las vacantes para mentoría personalizada son limitadas para garantizar el seguimiento biopsicológico de cada caso.</div>", unsafe_allow_html=True)

    if st.button("← Volver al Diagnóstico"):
        st.session_state.pantalla = 'diagnostico'
        st.rerun()

st.markdown("<p style='text-align: center; font-size: 0.8rem; margin-top: 50px; color: #555;'>Partnership Shield © 2026</p>", unsafe_allow_html=True)
