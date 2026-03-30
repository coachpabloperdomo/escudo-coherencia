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
    .card-red { background-color: #2b0b0b; padding: 25px; border-radius: 15px; border: 1px solid #ff4b4b; margin-bottom: 25px; border-left: 10px solid #ff4b4b; }
    .card-yellow { background-color: #2b260b; padding: 25px; border-radius: 15px; border: 1px solid #f1c40f; margin-bottom: 25px; border-left: 10px solid #f1c40f; }
    .card-green { background-color: #0b2b0f; padding: 25px; border-radius: 15px; border: 1px solid #2ecc71; margin-bottom: 25px; border-left: 10px solid #2ecc71; }
    .tactic-box { background-color: #161b22; padding: 15px; border-radius: 8px; border-top: 2px solid #D4AF37; margin-top: 10px; color: #f0f0f0 !important; font-weight: 500; }
    .info-box-custom { background-color: #1c1c1c; padding: 20px; border-radius: 10px; border: 1px solid #D4AF37; margin: 15px 0; text-align: center; }
    .info-box-custom b { color: #D4AF37; font-size: 1.1rem; }
    .info-box-custom p { color: #ffffff !important; margin-top: 10px; }
    .wa-button { background-color: #25D366; color: white !important; padding: 15px; border-radius: 10px; text-align: center; font-weight: bold; text-decoration: none; display: block; margin-top: 20px; border: none; }
    </style>
    """, unsafe_allow_html=True)

escudo_svg = """
<svg viewBox="-30 -30 572 572" style="width: 55px; height: 55px; fill: #D4AF37; margin-right: 15px; flex-shrink: 0; overflow: visible;">
<path d="M466.5 83.71l-192-80a48.15 48.15 0 0 0-36.94 0l-192 80A48.07 48.07 0 0 0 16 128v192c0 148.6 125.1 267.7 230.1 289.8a48.1 48.1 0 0 0 19.8 0C370.9 587.7 496 468.6 496 320V128a48.07 48.07 0 0 0-29.5-44.29zM256 553.7V64.21l164.5 68.52V320c0 102.7-88.7 186-164.5 208.7z"/>
</svg>
"""

# Base de conocimiento (Mantenemos los 9 escenarios)
CONTENIDOS = {
    "Relación de Pareja": {
        "Crítico": {"titulo": "VACIADO CRÍTICO: Crisis de Confianza", "diag": "Alerta de supervivencia subconsciente.", "codigo": "Blindaje de Salida", "tacticas": ["Protocolo de Silencio", "Auditoría Invisible", "Patrón Interruptor"], "gancho": "La ingeniería busca tu soberanía."},
        "Desbalance": {"titulo": "DESBALANCE: Asimetría de Esfuerzo", "diag": "Deuda sistémica acumulada.", "codigo": "Contrato Invisible", "tacticas": ["Mapeo de Cláusulas", "Retirada Estratégica", "Redefinición"], "gancho": "El resentimiento es el síntoma."},
        "Coherencia": {"titulo": "COHERENCIA: Estabilización", "diag": "Sincronización de la Lattice.", "codigo": "Arquitectura de Poder", "tacticas": ["Check-up Quincenal", "Blindaje Externo", "Anclaje"], "gancho": "Evitá volver a viejos surcos."}
    },
    "Sociedad Comercial": {
        "Crítico": {"titulo": "VACIADO CRÍTICO: Fuga de Activos", "diag": "Código de 'Depredador' activo.", "codigo": "Vaciado de Valor", "tacticas": ["Cierre de Nodos", "Registro de Hechos", "Presuasión"], "gancho": "Gana quien gestiona la psicología."},
        "Desbalance": {"titulo": "DESBALANCE: Operativo", "diag": "Parásito sistémico detectado.", "codigo": "Fuga de Soberanía", "tacticas": ["Métricas Claras", "Cese de Subvención", "Confrontación"], "gancho": "Reconfiguramos tu liderazgo."},
        "Coherencia": {"titulo": "COHERENCIA: Escalabilidad", "diag": "Flujo óptimo de resolución.", "codigo": "Sinergia Táctica", "tacticas": ["Innovación sin Ego", "Blindaje Legal", "Expansión"], "gancho": "Mentalidad de Jugador Pro."}
    },
    "Vínculo Mixto": {
        "Crítico": {"titulo": "VACIADO CRÍTICO: Colapso", "diag": "Interferencia destructiva total.", "codigo": "Efecto Cascada", "tacticas": ["Separación de Dominios", "Mediación", "Salvaguarda"], "gancho": "Solo el análisis biopsicológico salva imperios."},
        "Desbalance": {"titulo": "DESBALANCE: El Negocio como Hijo", "diag": "Desplazamiento del afecto original.", "codigo": "Asimetría de Prioridades", "tacticas": ["Citas sin pantallas", "Auditoría de Energía", "Identidad"], "gancho": "Que el negocio no sea la tumba del amor."},
        "Coherencia": {"titulo": "COHERENCIA: Imperio Familiar", "diag": "Ecosistema de alta eficiencia.", "codigo": "Escudo de Gobernanza", "tacticas": ["Legado 10 años", "Mantenimiento", "Intimidad"], "gancho": "Diferencia entre pareja y dinastía."}
    }
}

if 'pantalla' not in st.session_state:
    st.session_state.pantalla = 'radar'

# --- PANTALLA 1: RADAR ---
if st.session_state.pantalla == 'radar':
    st.markdown(f'<div class="header-box">{escudo_svg}<h1 style="color: #D4AF37; margin: 0;">PARTNERSHIP SHIELD</h1></div>', unsafe_allow_html=True)
    st.write("---")
    escenario = st.radio("**Escenario:**", ["Relación de Pareja", "Sociedad Comercial", "Vínculo Mixto"], horizontal=True)
    c1, c2 = st.columns(2)
    with c1:
        f_cancel = st.slider("Incumplimiento", 0, 10, 2, help="Promesas rotas.")
        friccion = st.slider("Fricción", 0, 10, 2, help="Discusiones constantes.")
    with c2:
        erosion = st.slider("Erosión", 0, 10, 2, help="Pérdida de autoridad.")
        opacidad = st.select_slider("Hermetismo", options=["Transparencia", "Zonas Grises", "Opacidad Total"])
    
    t1, t2 = st.columns(2)
    with t1:
        gas = st.toggle("Gaslighting")
        culp = st.toggle("Transferencia de Culpa")
    with t2:
        aisl = st.toggle("Aislamiento")
        ref = st.toggle("Refuerzo Intermitente")

    if st.button("OBTENER DIAGNÓSTICO"):
        st.session_state.score = f_cancel + friccion + erosion + (15 if opacidad == "Opacidad Total" else 5) + (10 if gas else 0) + (10 if culp else 0) + (10 if aisl else 0) + (10 if ref else 0)
        st.session_state.escenario = escenario
        st.session_state.pantalla = 'diagnostico'
        st.rerun()

# --- PANTALLA 2: DIAGNÓSTICO ---
elif st.session_state.pantalla == 'diagnostico':
    st.markdown(f'<div class="header-box">{escudo_svg}<h1 style="color: #D4AF37; margin: 0;">ANÁLISIS ESTRATÉGICO</h1></div>', unsafe_allow_html=True)
    nivel = "Crítico" if st.session_state.score >= 35 else "Desbalance" if st.session_state.score >= 15 else "Coherencia"
    info = CONTENIDOS[st.session_state.escenario][nivel]
    color = "card-red" if nivel == "Crítico" else "card-yellow" if nivel == "Desbalance" else "card-green"
    
    st.markdown(f"<div class='{color}'><h2>{info['titulo']}</h2><p>Score: {st.session_state.score}/75</p></div>", unsafe_allow_html=True)
    
    ca, cb = st.columns([1.5, 1])
    with ca:
        st.markdown("### 🔍 Diagnóstico")
        st.write(info['diag'])
        st.markdown("### 🛠️ Tácticas")
        for t in info['tacticas']:
            st.markdown(f"<div class='tactic-box'>✅ {t}</div>", unsafe_allow_html=True)
    with cb:
        st.success(f"**Código: {info['codigo']}**")
        st.warning(info['gancho'])
    
    st.write("---")
    if st.button("ACCEDER A LA MENTORÍA Y HOJA DE RUTA"):
        st.session_state.pantalla = 'mentoria'
        st.rerun()
    if st.button("← Re-evaluar"):
        st.session_state.pantalla = 'radar'
        st.rerun()

# --- PANTALLA 3: MENTORÍA ---
elif st.session_state.pantalla == 'mentoria':
    st.markdown(f'<div class="header-box">{escudo_svg}<h1 style="color: #D4AF37; margin: 0;">INGENIERÍA CONDUCTUAL</h1></div>', unsafe_allow_html=True)
    
    col_izq, col_der = st.columns([2, 1])
    
    with col_izq:
        st.markdown("### Tu Hoja de Ruta está lista")
        st.write("Para recibir el análisis completo y coordinar tu sesión de auditoría, completá los datos:")
        with st.form("form_final"):
            nombre = st.text_input("Nombre Completo*")
            situacion = st.text_area("Describí brevemente tu situación actual*")
            enviado = st.form_submit_button("GENERAR ENLACE DE WHATSAPP")
            
            if enviado:
                if nombre and situacion:
                    msg = f"Hola Pablo, vengo de Partnership Shield.\nNombre: {nombre}\nEscenario: {st.session_state.escenario}\nNivel: {st.session_state.score}\nSituación: {situacion}"
                    url_wa = f"https://wa.me/59899816392?text={urllib.parse.quote(msg)}"
                    st.session_state.url_wa = url_wa
                    st.success("¡Enlace generado! Hacé click en el botón verde de abajo.")
    
    with col_der:
        st.markdown('<div class="info-box-custom"><b>📍 SESIÓN DE AUDITORÍA</b><p>Analizaremos tu caso bajo el prisma de la Comunicación Biopsicológica para recuperar tu soberanía.</p></div>', unsafe_allow_html=True)
        if 'url_wa' in st.session_state:
            st.markdown(f'<a href="{st.session_state.url_wa}" target="_blank" class="wa-button">📩 ENVIAR POR WHATSAPP</a>', unsafe_allow_html=True)

    if st.button("← Volver al Diagnóstico"):
        st.session_state.pantalla = 'diagnostico'
        st.rerun()

st.markdown("<p style='text-align: center; font-size: 0.8rem; margin-top: 50px; color: #555;'>Partnership Shield © 2026</p>", unsafe_allow_html=True)
