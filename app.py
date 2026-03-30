import streamlit as st
import urllib.parse

# 1. Configuración y Estilo
st.set_page_config(page_title="Partnership Shield", page_icon="🛡️", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { background-color: #D4AF37; color: black; font-weight: bold; border-radius: 10px; height: 3em; }
    .gold-text { color: #D4AF37; font-family: 'Georgia', serif; text-align: center; }
    .card { background-color: #1e2130; padding: 20px; border-radius: 15px; border: 1px solid #D4AF37; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# Inicializar el estado de la aplicación
if 'pantalla' not in st.session_state:
    st.session_state.pantalla = 'radar'

# --- PANTALLA 1: EL RADAR ---
if st.session_state.pantalla == 'radar':
    st.markdown("<h1 class='gold-text'>🛡️ PARTNERSHIP SHIELD</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #C0C0C0;'>Auditoría Biopsicológica de Vínculos</p>", unsafe_allow_html=True)
    
    escenario = st.radio("**Escenario a Auditar:**", ["Relación de Pareja", "Sociedad Comercial", "Vínculo Mixto"], horizontal=True)
    
    st.markdown("---")
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

    # Cálculo de Score
    score = f_cancel + (10 if claridad == "Opacidad" else 5 if claridad == "Gris" else 0)
    score += (7 if triangulacion else 0) + (15 if gaslighting else 0) + (8 if culpa else 0) + (7 if persuasion_neg else 0)

    if st.button("OBTENER DIAGNÓSTICO Y HOJA DE RUTA"):
        st.session_state.score = score
        st.session_state.escenario = escenario
        st.session_state.pantalla = 'solucion'
        st.rerun()

# --- PANTALLA 2: LA SOLUCIÓN (Personalizada) ---
elif st.session_state.pantalla == 'solucion':
    score = st.session_state.score
    st.markdown("<h1 class='gold-text'>🛡️ TU ESTRATEGIA DE DEFENSA</h1>", unsafe_allow_html=True)
    
    if score >= 20:
        st.markdown("""
        <div class='card'>
            <h2 style='color: #ff4b4b;'>🚨 ESTATUS: VACIADO CRÍTICO</h2>
            <p><b>Análisis:</b> Estás en una zona de alto riesgo. Se ha detectado una dinámica de extracción activa de tu valor personal o financiero.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("### 🛠️ Solución Inmediata: El Protocolo de Silencio")
        st.info("Copiá este mensaje y envialo ahora. No des explicaciones adicionales.")
        st.code("He decidido documentar toda interacción futura. No participaré en discusiones fuera de este canal oficial.")
        
        st.write("### 📄 Tu Recurso de Valor")
        st.write("Hemos preparado un **Informe Forense Preliminar** basado en tus respuestas.")
        if st.button("Descargar Auditoría de Riesgo (PDF Simulado)"):
            st.success("Preparando descarga... (Aquí conectaríamos el generador de PDF real)")

    elif 10 <= score < 20:
        st.markdown("""
        <div class='card'>
            <h2 style='color: #f1c40f;'>⚠️ ESTATUS: DESBALANCE ESTRATÉGICO</h2>
            <p><b>Análisis:</b> El vínculo está perdiendo coherencia. Hay manipulación presente, pero todavía hay margen de maniobra táctica.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("### 🛠️ Solución Inmediata: El Patrón Interruptor")
        st.write("Tu contraparte espera que reacciones con queja o explicación. Hacé lo opuesto.")
        st.warning("**Táctica:** Ante el próximo reclamo, respondé: 'Entiendo tu punto. Lo voy a procesar y te aviso cuando tenga una decisión'. Y retirate físicamente.")

    else:
        st.success("### ✅ ESTATUS: COHERENCIA ESTABLE")
        st.write("Tu estructura vincular es sólida. Te entregamos una guía de optimización.")

    # --- FORMULARIO FINAL (Al final de la solución) ---
    st.markdown("---")
    st.markdown("<h3 class='gold-text'>¿Querés que Pablo analice tu caso personalmente?</h3>", unsafe_allow_html=True)
    
    with st.form("contacto_pablo"):
        nombre = st.text_input("Nombre Completo*")
        situacion = st.text_area("Breve resumen de la situación*")
        submit = st.form_submit_button("SOLICITAR MENTORÍA ESTRÁTEGICA")
        
        if submit:
            if nombre and situacion:
                msg = f"Hola Pablo, mi código es #COHERENCIA2026. Nombre: {nombre}. Score: {score}. Situación: {situacion}"
                link_wa = f"https://wa.me/59899816392?text={urllib.parse.quote(msg)}"
                st.balloons()
                st.markdown(f'<a href="{link_wa}" target="_blank" style="text-decoration:none;"><div style="background-color:#25D366;color:white;padding:15px;border-radius:10px;text-align:center;font-weight:bold;">📩 ENVIAR RESULTADOS POR WHATSAPP</div></a>', unsafe_allow_html=True)

    if st.button("← Volver a Evaluar"):
        st.session_state.pantalla = 'radar'
        st.rerun()

st.markdown("<p style='text-align: center; font-size: 0.8rem; margin-top: 50px;'>Partnership Shield © 2026</p>", unsafe_allow_html=True)
