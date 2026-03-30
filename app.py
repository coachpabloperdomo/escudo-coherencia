import streamlit as st
import urllib.parse

# 1. Configuración de Página
st.set_page_config(page_title="Partnership Shield", page_icon="🛡️", layout="wide")

# Estilo y Escudo Dorado Diseñado
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
    
    /* Escudo Dorado SVG Integrado */
    .header-shield {
        fill: #D4AF37;
        width: 3rem;
        height: 3rem;
        display: inline-block;
        vertical-align: middle;
        margin-right: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# SVG del Escudo (reemplaza al emoji azul)
escudo_svg = """
<svg class="header-shield" viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg">
<path d="M466.5 83.71l-192-80a48.15 48.15 0 0 0-36.94 0l-192 80A48.07 48.07 0 0 0 16 128v192c0 148.6 125.1 267.7 230.1 289.8a48.1 48.1 0 0 0 19.8 0C370.9 587.7 496 468.6 496 320V128a48.07 48.07 0 0 0-29.5-44.29zM256 553.7V64.21l164.5 68.52V320c0 102.7-88.7 186-164.5 208.7z"/>
</svg>
"""

if 'pantalla' not in st.session_state:
    st.session_state.pantalla = 'radar'

# --- PANTALLA 1: EL RADAR ---
if st.session_state.pantalla == 'radar':
    # Título con escudo dorado SVG
    st.markdown(f"<h1 style='text-align: center; color: #D4AF37;'>{escudo_svg}PARTNERSHIP SHIELD</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #C0C0C0; font-style: italic;'>Arquitectura del Comportamiento Humano & Estrategia Biopsicológica</p>", unsafe_allow_html=True)
    
    st.write("---")
    escenario = st.radio("**Seleccioná el escenario a auditar:**", ["Relación de Pareja", "Sociedad Comercial", "Vínculo Mixto"], horizontal=True)
    
    st.markdown("<h3 class='gold-text'>📡 Radar de Diagnóstico</h3>", unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    with c1:
        f_cancel = st.slider("Incumplimiento de acuerdos (0-10)", 0, 10, 2, help="Nivel de ruptura de la palabra.")
        claridad = st.select_slider("Acceso a Información", options=["Transparencia", "Zonas Grises", "Opacidad Total"])
        triangulacion = st.toggle("Triangulación con terceros", help="Validación externa para desautorizarte.")
    with c2:
        gaslighting = st.toggle("Gaslighting / Invalidez", help="Hacerte dudar de tu realidad.")
        culpa = st.toggle("Transferencia de Culpa", help="Responsabilizarte por sus reacciones.")
        persuasion_neg = st.toggle("Amenazas / Promesas falsas", help="Presión sutil o zanahorias inexistentes.")

    if st.button("OBTENER DIAGNÓSTICO Y SOLUCIÓN"):
        score = f_cancel + (10 if claridad == "Opacidad Total" else 5 if claridad == "Zonas Grises" else 0)
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
            <p><b>Análisis:</b> Se ha detectado una dinámica de extracción activa de valor en tu <b>{escenario}</b>. El vínculo está operando en zona de riesgo biopsicológico.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("### 🛠️ Orientación Inmediata: Protocolo de Coherencia")
        st.write("""
        **Nuestra sugerencia estratégica para evitar escaladas de conflicto:**
        
        1.  **Si no están juntos:** Te sugerimos copiar y enviar el siguiente mensaje por **WhatsApp o el chat habitual** para fijar un límite de respeto.
        2.  **Si están cara a cara:** No lo envíes, pero **mantené esta intención mentalmente**. No te enganches en provocaciones. Si la conversación sube de tono, simplemente decí con calma: *"En este momento no estoy cómodo/a discutiendo esto sin claridad de procesos"* y retírate unos minutos.
        """)
        
        texto_mensaje = "He decidido que para proteger la integridad de nuestro vínculo/proyecto, toda comunicación futura sobre acuerdos operativos o personales será documentada por escrito. No participaré en discusiones verbales fuera de este canal oficial."
        st.markdown(f"<div class='mensaje-copiar'>{texto_mensaje}</div>", unsafe_allow_html=True)
        
    elif 10 <= score < 20:
        st.markdown(f"""
        <div class='card-yellow'>
            <h2 style='color: #f1c40f; margin-top:0;'>⚠️ ESTATUS: DESBALANCE ESTRATÉGICO</h2>
            <p><b>Análisis:</b> El vínculo en <b>{escenario}</b> muestra pérdida de coherencia. Hay manipulación presente, pero tenés margen táctico.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("### 🛠️ Orientación Inmediata: El Patrón Interruptor")
        st.warning("**Táctica:** Ante el próximo reclamo, no reaccionés. Respondé con calma: 'Entiendo tu punto. Lo voy a procesar y te aviso cuando tenga una decisión'. Acto seguido, retirate físicamente de la conversación.")

    else:
        st.markdown("<div class='card-green'><h2>✅ ESTATUS: COHERENCIA ESTABLE</h2><p>El vínculo se mantiene productivo.</p></div>", unsafe_allow_html=True)

    # Formulario
    st.markdown("---")
    st.markdown("<h3 class='gold-text'>¿Querés que Pablo analice tu caso pessoalmente?</h3>", unsafe_allow_html=True)
    with st.form("contacto_v4_3"):
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
