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
    
    .card-red { background-color: #2b0b0b; padding: 25px; border-radius: 15px; border: 1px solid #ff4b4b; margin-bottom: 25px; border-left: 10px solid #ff4b4b; color: #ffffff !important; }
    .card-yellow { background-color: #2b260b; padding: 25px; border-radius: 15px; border: 1px solid #f1c40f; margin-bottom: 25px; border-left: 10px solid #f1c40f; color: #ffffff !important; }
    .card-green { background-color: #0b2b0f; padding: 25px; border-radius: 15px; border: 1px solid #2ecc71; margin-bottom: 25px; border-left: 10px solid #2ecc71; color: #ffffff !important; }
    
    .card-red h2, .card-yellow h2, .card-green h2, .card-red p, .card-yellow p, .card-green p { color: #ffffff !important; }

    .tactic-box { background-color: #161b22; padding: 15px; border-radius: 8px; border-top: 2px solid #D4AF37; margin-top: 10px; color: #f0f0f0 !important; font-weight: 500; }
    
    .download-box { background: linear-gradient(145deg, #1e1e1e, #121212); border: 1px dashed #D4AF37; padding: 20px; border-radius: 15px; text-align: center; margin-top: 20px; }
    
    .wa-button { background-color: #25D366; color: white !important; padding: 15px; border-radius: 10px; text-align: center; font-weight: bold; text-decoration: none; display: block; margin-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

escudo_svg = """
<svg viewBox="-30 -30 572 572" style="width: 55px; height: 55px; fill: #D4AF37; margin-right: 15px; flex-shrink: 0; overflow: visible;">
<path d="M466.5 83.71l-192-80a48.15 48.15 0 0 0-36.94 0l-192 80A48.07 48.07 0 0 0 16 128v192c0 148.6 125.1 267.7 230.1 289.8a48.1 48.1 0 0 0 19.8 0C370.9 587.7 496 468.6 496 320V128a48.07 48.07 0 0 0-29.5-44.29zM256 553.7V64.21l164.5 68.52V320c0 102.7-88.7 186-164.5 208.7z"/>
</svg>
"""

# Base de conocimiento revisada (SIN ERRORES DE SINTAXIS)
CONTENIDOS = {
    "Relación de Pareja": {
        "Crítico": {"titulo": "VACIADO CRÍTICO: Crisis de Confianza", "diag": "El sistema está en modo supervivencia por falta de previsibilidad.", "codigo": "Blindaje de Salida", "tacticas": ["Protocolo de Silencio Táctico", "Auditoría de Micro-movimientos", "Interrupción de Patrón"], "gancho": "Recuperá el control de tu paz mental."},
        "Desbalance": {"titulo": "DESBALANCE: Asimetría de Esfuerzo", "diag": "Uno de los nodos está sobrecargado mientras el otro consume energía.", "codigo": "Contrato Invisible", "tacticas": ["Mapeo de Cesiones", "Retirada Estratégica", "Redefinición de Roles"], "gancho": "Dejá de pagar deudas ajenas."},
        "Coherencia": {"titulo": "COHERENCIA: Estabilización Sistémica", "diag": "Vínculo con autonomía y respeto de límites. Blindaje de crecimiento activo.", "codigo": "Arquitectura de Poder", "tacticas": ["Check-up Quincenal", "Blindaje Externo", "Anclaje de Identidad"], "gancho": "La maestría es no volver a los viejos surcos."}
    },
    "Sociedad Comercial": {
        "Crítico": {"titulo": "VACIADO CRÍTICO: Fuga de Activos", "diag": "El socio opera bajo código de depredación individual.", "codigo": "Vaciado de Valor", "tacticas": ["Cierre de Nodos de Info", "Registro de Hechos", "Presuasión"], "gancho": "La psicología es el activo real."},
        "Desbalance": {"titulo": "DESBALANCE: Operativo", "diag": "El proyecto sobrevive por tu empuje. Riesgo de agotamiento de líder.", "codigo": "Fuga de Soberanía", "tacticas": ["Métricas Radicales", "Cese de Subvención", "Confrontación"], "gancho": "Reconfigurá tu autoridad."},
        "Coherencia": {"titulo": "COHERENCIA: Escalabilidad", "diag": "Sinergia total. Los socios multiplican sus capacidades.", "codigo": "Sinergia Táctica", "tacticas": ["Innovación sin Ego", "Blindaje Competitivo", "Expansión"], "gancho": "Jugá en el nivel que otros ni imaginan."}
    },
    "Vínculo Mixto": {
        "Crítico": {"titulo": "VACIADO CRÍTICO: Colapso de Dominios", "diag": "Conflicto emocional contamina lo financiero. Riesgo de implosión.", "codigo": "Efecto Cascada", "tacticas": ["Separación Casa vs Oficina", "Mediación Externa", "Salvaguarda de Activos"], "gancho": "Separar cables antes de la explosión."},
        "Desbalance": {"titulo": "DESBALANCE: Empresa como Hijo", "diag": "Desplazamiento del afecto. Empleados de su proyecto, no compañeros.", "codigo": "Asimetría de Prioridades", "tacticas": ["Citas sin Pantallas", "Auditoría de Carga Mental", "Propósito Inicial"], "gancho": "Que el negocio no sea la tumba del amor."},
        "Coherencia": {"titulo": "COHERENCIA: Imperio Familiar", "diag": "Ecosistema de alta eficiencia. Dinastía en formación.", "codigo": "Escudo de Gobernanza", "tacticas": ["Plan de Legado", "Mantenimiento de Acuerdos", "Cultivo de Intimidad"], "gancho": "Diferencia entre éxito y dinastía."}
    }
}

if 'pantalla' not in st.session_state:
    st.session_state.pantalla = 'radar'

# --- PANTALLA 1: RADAR ---
if st.session_state.pantalla == 'radar':
    st.markdown(f'<div class="header-box">{escudo_svg}<h1 style="color: #D4AF37; margin: 0;">PARTNERSHIP SHIELD</h1></div>', unsafe_allow_html=True)
    st.write("---")
    
    escenario = st.radio("**Escenario a Auditar:**", ["Relación de Pareja", "Sociedad Comercial", "Vínculo Mixto"], horizontal=True)
    
    st.markdown("<h3 class='gold-text'>📡 Radar de Diagnóstico</h3>", unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    with c1:
        f_cancel = st.slider("Incumplimiento de Acuerdos", 0, 10, 2, help="¿Rompen promesas o compromisos?")
        friccion = st.slider("Fricción / Discusiones", 0, 10, 2, help="Tensión constante.")
    with c2:
        erosion = st.slider("Erosión de Autoridad", 0, 10, 2, help="¿Tu opinión ya no pesa?")
        opacidad = st.select_slider("Opacidad", options=["Transparencia", "Zonas Grises", "Opacidad Total"], help="Ocultamiento de información.")
    
    st.markdown("<br>", unsafe_allow_html=True)
    t1, t2 = st.columns(2)
    with t1:
        gas = st.toggle("Gaslighting", help="Invalidan tus emociones.")
        culp = st.toggle("Transferencia de Culpa", help="¿Sos responsable de todo lo malo?")
        aisl = st.toggle("Aislamiento Sugerido", help="Críticas hacia tu entorno cercano.")
    with t2:
        amenazas = st.toggle("Amenazas / Ultimátums", help="Uso de la ruptura como presión.")
        ref = st.toggle("Refuerzo Intermitente", help="Ciclos de afecto y desprecio.")
        triang = st.toggle("Triangulación", help="Uso de terceros para generar inseguridad.")

    if st.button("GENERAR DIAGNÓSTICO ESTRATÉGICO"):
        score = f_cancel + friccion + erosion + (15 if opacidad == "Opacidad Total" else 5)
        score += (10 if gas else 0) + (10 if culp else 0) + (10 if aisl else 0) + (10 if ref else 0) + (10 if amenazas else 0) + (10 if triang else 0)
        st.session_state.score = score
        st.session_state.escenario = escenario
        st.session_state.pantalla = 'diagnostico'
        st.rerun()

# --- PANTALLA 2: DIAGNÓSTICO ---
elif st.session_state.pantalla == 'diagnostico':
    st.markdown(f'<div class="header-box">{escudo_svg}<h1 style="color: #D4AF37; margin: 0;">ANÁLISIS DE SOBERANÍA</h1></div>', unsafe_allow_html=True)
    nivel = "Crítico" if st.session_state.score >= 35 else "Desbalance" if st.session_state.score >= 15 else "Coherencia"
    info = CONTENIDOS[st.session_state.escenario][nivel]
    color_class = "card-red" if nivel == "Crítico" else "card-yellow" if nivel == "Desbalance" else "card-green"
    
    st.markdown(f"<div class='{color_class}'><h2>{info['titulo']}</h2><p style='font-size: 1.2rem;'>Puntaje: {st.session_state.score}/75</p></div>", unsafe_allow_html=True)
    
    ca, cb = st.columns([1.5, 1])
    with ca:
        st.markdown("### 🔍 Diagnóstico")
        st.write(info['diag'])
        st.markdown("### 🛠️ Tácticas")
        for t in info['tacticas']:
            st.markdown(f"<div class='tactic-box'>✅ {t}</div>", unsafe_allow_html=True)
        
        st.markdown('<div class="download-box">', unsafe_allow_html=True)
        st.markdown(f"**📂 WORKBOOK DISPONIBLE:** Nivel {nivel}")
        if st.button("ACCEDER AL MATERIAL"):
            st.session_state.pantalla = 'mentoria'
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    with cb:
        st.success(f"**CÓDIGO: {info['codigo']}**")
        st.warning(info['gancho'])

    st.write("---")
    if st.button("SOLICITAR AUDITORÍA"):
        st.session_state.pantalla = 'mentoria'
        st.rerun()
    if st.button("← Volver"):
        st.session_state.pantalla = 'radar'
        st.rerun()

# --- PANTALLA 3: MENTORÍA ---
elif st.session_state.pantalla == 'mentoria':
    st.markdown(f'<div class="header-box">{escudo_svg}<h1 style="color: #D4AF37; margin: 0;">MENTORÍA ESTRATÉGICA</h1></div>', unsafe_allow_html=True)
    c_izq, c_der = st.columns([2, 1])
    with c_izq:
        with st.form("f_final"):
            nombre = st.text_input("Nombre Completo*")
            situacion = st.text_area("Detallá tu caso*")
            if st.form_submit_button("GENERAR ENLACE"):
                if nombre and situacion:
                    msg = f"Auditoría: {st.session_state.escenario}\nNombre: {nombre}\nScore: {st.session_state.score}\nSituación: {situacion}"
                    st.session_state.url_wa = f"https://wa.me/59899816392?text={urllib.parse.quote(msg)}"
    
    with c_der:
        if 'url_wa' in st.session_state:
            st.markdown(f'<a href="{st.session_state.url_wa}" target="_blank" class="wa-button">📩 ENVIAR POR WHATSAPP</a>', unsafe_allow_html=True)

    if st.button("← Volver"):
        st.session_state.pantalla = 'diagnostico'
        st.rerun()

st.markdown("<p style='text-align: center; font-size: 0.8rem; margin-top: 50px; color: #555;'>Partnership Shield © 2026</p>", unsafe_allow_html=True)
