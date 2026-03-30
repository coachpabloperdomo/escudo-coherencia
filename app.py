import streamlit as st
import urllib.parse

# 1. Configuración y Estilo Mejorado
st.set_page_config(page_title="Partnership Shield", page_icon="🛡️", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { background-color: #D4AF37; color: black; font-weight: bold; border-radius: 10px; height: 3em; width: 100%; }
    .gold-text { color: #D4AF37; font-family: 'Georgia', serif; text-align: center; }
    /* Estilo de Tarjetas con Contraste Asegurado */
    .card-red { background-color: #2b0b0b; padding: 25px; border-radius: 15px; border: 1px solid #ff4b4b; margin-bottom: 25px; color: #ffffff; }
    .card-yellow { background-color: #2b260b; padding: 25px; border-radius: 15px; border: 1px solid #f1c40f; margin-bottom: 25px; color: #ffffff; }
    .card-green { background-color: #0b2b0f; padding: 25px; border-radius: 15px; border: 1px solid #2ecc71; margin-bottom: 25px; color: #ffffff; }
    /* Forzar color de texto en párrafos dentro de tarjetas */
    .card-red p, .card-yellow p, .card-green p { color: #ffffff !important; font-size: 1.1rem; }
    </style>
    """, unsafe_allow_html=True)

# Inicializar el estado de la sesión
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
        f_cancel = st.slider("Incumplimiento de acuerdos (0-10)", 0, 10, 2, help="Ruptura de la palabra empeñada.")
        claridad = st.select_slider("Acceso a Información", options=["Transparencia", "Gris", "Opacidad"])
        triangulacion = st.toggle("Triangulación con terceros", help="Validación externa para desautorizarte.")
    with c2:
        gaslighting = st.toggle("Gaslighting / Invalidez", help="Hacerte dudar de tu realidad.")
        culpa = st.toggle("Transferencia de Culpa", help="Responsabilizarte por sus reacciones.")
        persuasion_neg = st.toggle("Amenazas / Promesas falsas", help="Presión sutil o 'zanahorias' inexistentes.")

    st.markdown("---")
    if st.button("OBTENER DIAGNÓSTICO Y HOJA DE RUTA"):
        # Cálculo del score
        score = f_cancel + (10 if claridad == "Opacidad" else 5 if claridad == "Gris" else 0)
        score += (7 if triangulacion else 0) + (15 if gaslighting else 0) + (8 if culpa else 0) + (7 if persuasion_neg else 0)
        
        st.session_state.score = score
        st.session_state.escenario = escenario
        st.session_state.pantalla = 'solucion'
        st.rerun()

# --- PANTALLA 2: LA SOLUCIÓN (Personalizada) ---
elif st.session_state.pantalla == 'solucion':
    score = st.session_state.score
    escenario = st.session_state.escenario
    st.markdown("<h1 class='gold-text'>🛡️ TU ESTRATEGIA DE DEFENSA</h1>", unsafe_allow_html=True)
    
    if score >= 20:
        st.markdown(f"""
        <div class='card-red'>
            <h2 style='color: #ff4b4b; margin-top:0;'>🚨 ESTATUS: VACIADO CRÍTICO</h2>
            <p><b>Análisis:</b> Estás en una zona de alto riesgo. Se ha detectado una dinámica de extracción activa de tu valor personal o financiero en tu escenario de <b>{escenario}</b>.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("### 🛠️ Solución Inmediata: El Protocolo de Silencio")
        st.info("Copiá este mensaje y envialo ahora por el canal oficial. No des explicaciones adicionales.")
        st.code("He decidido que para proteger la integridad del vínculo/proyecto, toda comunicación futura será documentada. No participaré en discusiones fuera de este protocolo.", language="text")
        
    elif 10 <= score < 20:
        st.markdown(f"""
        <div class='card-yellow'>
            <h2 style='color: #f1c40f; margin-top:0;'>⚠️ ESTATUS: DESBALANCE ESTRATÉGICO</h2>
            <p><b>Análisis:</b> El vínculo en <b>{escenario}</b> está perdiendo coherencia. Hay manipulación presente, pero todavía tenés margen de maniobra táctica.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("### 🛠️ Solución Inmediata: El Patrón Interruptor")
        st.warning("**Táctica:** Ante el próximo reclamo, respondé: 'Entiendo tu punto. Lo voy a procesar y te aviso cuando tenga una decisión'. Y retirate físicamente de la conversación.")

    else:
        st.markdown("""
        <div class='card-green'>
            <h2 style='color: #2ecc71; margin-top:0;'>✅ ESTATUS: COHERENCIA ESTABLE</h2>
            <p><b>Análisis:</b> Tu estructura vincular es sólida. Los niveles de transparencia son óptimos para el crecimiento.</p>
        </div>
        """, unsafe_allow_html=True)

    # --- FORMULARIO DE CIERRE ---
    st.markdown("---")
    st.markdown("<h3 class='gold-text'>¿Querés que analice tu caso personalmente?</h3>", unsafe_allow_html=True)
    
    with st.form("contacto_pablo_v4"):
        nombre = st.text_input("Nombre Completo*")
        situacion = st.text_area("Breve resumen de la situación*")
        submit = st.form_submit_button("SOLICITAR EVALUACIÓN ESTRATÉGICA")
        
        if submit:
            if nombre and situacion:
                resumen = f"Score: {score}/50 | Escenario: {escenario}"
                msg = f"Hola Pablo, mi código es #COHERENCIA2026.\n\nNombre: {nombre}\nDiagnóstico: {resumen}\nSituación: {situacion}"
                link_wa = f"https://wa.me/59899816392?text={urllib.parse.quote(msg)}"
                st.balloons()
                st.markdown(f'<a href="{link_wa}" target="_blank" style="text-decoration:none;"><div style="background-color:#25D366;color:white;padding:15px;border-radius:10px;text-align:center;font-weight:bold;">📩 ENVIAR RESULTADOS POR WHATSAPP</div></a>', unsafe_allow_html=True)
            else:
                st.error("Por favor completá los campos obligatorios.")

    if st.button("← Volver a realizar la Auditoría"):
        st.session_state.pantalla = 'radar'
        st.rerun()

st.markdown("<p style='text-align: center; font-size: 0.8rem; margin-top: 50px; color: #555;'>Partnership Shield © 2026 | Pablo Perdomo</p>", unsafe_allow_html=True)
