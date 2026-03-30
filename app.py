import streamlit as st
import urllib.parse

# 1. Configuración y Estética Partnership Shield
st.set_page_config(page_title="Partnership Shield", page_icon="🛡️", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { background-color: #D4AF37; color: black; font-weight: bold; border-radius: 10px; height: 3em; width: 100%; }
    .gold-text { color: #D4AF37; font-family: 'Georgia', serif; text-align: center; }
    .card-red { background-color: #2b0b0b; padding: 25px; border-radius: 15px; border: 1px solid #ff4b4b; margin-bottom: 25px; color: #ffffff; }
    .card-yellow { background-color: #2b260b; padding: 25px; border-radius: 15px; border: 1px solid #f1c40f; margin-bottom: 25px; color: #ffffff; }
    .card-green { background-color: #0b2b0f; padding: 25px; border-radius: 15px; border: 1px solid #2ecc71; margin-bottom: 25px; color: #ffffff; }
    .card-red p, .card-yellow p, .card-green p { color: #ffffff !important; }
    /* Estilo para el bloque de mensaje a copiar */
    .mensaje-copiar { background-color: #121212; border-left: 5px solid #D4AF37; padding: 15px; font-family: monospace; color: #D4AF37; margin: 10px 0; }
    </style>
    """, unsafe_allow_html=True)

if 'pantalla' not in st.session_state:
    st.session_state.pantalla = 'radar'

# --- PANTALLA 1: EL RADAR ---
if st.session_state.pantalla == 'radar':
    # Título con escudo dorado integrado
    st.markdown("<h1 style='text-align: center; color: #D4AF37;'>🛡️ PARTNERSHIP SHIELD</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #C0C0C0; font-style: italic;'>Arquitectura del Comportamiento Humano & Estrategia Biopsicológica</p>", unsafe_allow_html=True)
    
    st.write("---")
    escenario = st.radio("**Seleccioná el escenario a auditar:**", ["Relación de Pareja", "Sociedad Comercial", "Vínculo Mixto"], horizontal=True)
    
    st.markdown("<h3 class='gold-text'>📡 Radar de Diagnóstico</h3>", unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    with c1:
        f_cancel = st.slider("Incumplimiento de acuerdos (0-10)", 0, 10, 2)
        claridad = st.select_slider("Acceso a Información", options=["Transparencia", "Gris", "Opacidad"])
        triangulacion = st.toggle("Triangulación con terceros")
    with c2:
        gaslighting = st.toggle("Gaslighting / Invalidez")
        culpa = st.toggle("Transferencia de Culpa")
        persuasion_neg = st.toggle("Amenazas / Promesas falsas")

    if st.button("OBTENER DIAGNÓSTICO Y SOLUCIÓN"):
        score = f_cancel + (10 if claridad == "Opacidad" else 5 if claridad == "Gris" else 0)
        score += (7 if triangulacion else 0) + (15 if gaslighting else 0) + (8 if culpa else 0) + (7 if persuasion_neg else 0)
        st.session_state.score = score
        st.session_state.escenario = escenario
        st.session_state.pantalla = 'solucion'
        st.rerun()

# --- PANTALLA 2: LA SOLUCIÓN ---
elif st.session_state.pantalla == 'solucion':
    score = st.session_state.score
    escenario = st.session_state.escenario
    st.markdown("<h1 class='gold-text'>🛡️ TU ESTRATEGIA DE DEFENSA</h1>", unsafe_allow_html=True)
    
    if score >= 20:
        st.markdown(f"""
        <div class='card-red'>
            <h2 style='color: #ff4b4b; margin-top:0;'>🚨 ESTATUS: VACIADO CRÍTICO</h2>
            <p><b>Análisis:</b> Se ha detectado una dinámica de extracción activa de valor en tu <b>{escenario}</b>. Estás en zona de riesgo biopsicológico.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("### 🛠️ Acción Inmediata: El Protocolo de Silencio")
        st.write("Copiá el siguiente texto y envialo ahora mismo por **WhatsApp o el chat que usen habitualmente**. No agregues nada más y no respondas a las provocaciones siguientes.")
        
        texto_mensaje = "He decidido que para proteger la integridad de nuestro vínculo/proyecto, toda comunicación futura será documentada por escrito. No participaré en discusiones verbales fuera de este canal."
        st.markdown(f"<div class='mensaje-copiar'>{texto_mensaje}</div>", unsafe_allow_html=True)
        st.caption("Mantené el silencio absoluto después de enviarlo. El silencio es tu posición de poder.")
        
    elif 10 <= score < 20:
        st.markdown(f"""
        <div class='card-yellow'>
            <h2 style='color: #f1c40f; margin-top:0;'>⚠️ ESTATUS: DESBALANCE ESTRATÉGICO</h2>
            <p><b>Análisis:</b> Tu vínculo en <b>{escenario}</b> muestra pérdida de coherencia. Hay manipulación activa detectada.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("### 🛠️ Acción Inmediata: El Patrón Interruptor")
        st.warning("**Táctica:** La próxima vez que te reclamen algo, no te expliques. Respondé: 'Entiendo tu punto. Lo voy a procesar y te aviso cuando tenga una decisión'. Acto seguido, retitrate del lugar.")

    else:
        st.markdown("<div class='card-green'><h2>✅ ESTATUS: COHERENCIA ESTABLE</h2><p>Vínculo saludable.</p></div>", unsafe_allow_html=True)

    # Formulario
    st.markdown("---")
    st.markdown("<h3 class='gold-text'>¿Querés que analice tu caso personalmente?</h3>", unsafe_allow_html=True)
    with st.form("contacto_v4_2"):
        nombre = st.text_input("Nombre Completo*")
        situacion = st.text_area("Resumen de tu situación*")
        if st.form_submit_button("SOLICITAR EVALUACIÓN ESTRATÉGICA"):
            if nombre and situacion:
                msg = f"Hola Pablo, mi código es #COHERENCIA2026.\n\nNombre: {nombre}\nDiagnóstico: Score {score}/50\nSituación: {situacion}"
                st.balloons()
                st.markdown(f'<a href="https://wa.me/59899816392?text={urllib.parse.quote(msg)}" target="_blank" style="text-decoration:none;"><div style="background-color:#25D366;color:white;padding:15px;border-radius:10px;text-align:center;font-weight:bold;">📩 ENVIAR POR WHATSAPP</div></a>', unsafe_allow_html=True)
            else:
                st.error("Completá los campos obligatorios.")

    if st.button("← Volver al Radar"):
        st.session_state.pantalla = 'radar'
        st.rerun()

st.markdown("<p style='text-align: center; font-size: 0.8rem; margin-top: 50px; color: #555;'>Partnership Shield © 2026</p>", unsafe_allow_html=True)
