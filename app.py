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
    </style>
    """, unsafe_allow_html=True)

escudo_svg = """
<svg viewBox="-30 -30 572 572" style="width: 55px; height: 55px; fill: #D4AF37; margin-right: 15px; flex-shrink: 0; overflow: visible;">
<path d="M466.5 83.71l-192-80a48.15 48.15 0 0 0-36.94 0l-192 80A48.07 48.07 0 0 0 16 128v192c0 148.6 125.1 267.7 230.1 289.8a48.1 48.1 0 0 0 19.8 0C370.9 587.7 496 468.6 496 320V128a48.07 48.07 0 0 0-29.5-44.29zM256 553.7V64.21l164.5 68.52V320c0 102.7-88.7 186-164.5 208.7z"/>
</svg>
"""

CONTENIDOS = {
    "Relación de Pareja": {
        "Crítico": {
            "titulo": "VACIADO CRÍTICO: Crisis de Confianza",
            "diag": "El sistema nervioso está en 'alerta de supervivencia'. Tu inconsciente procesa la ambigüedad como una amenaza de muerte social.",
            "codigo": "Blindaje de Salida",
            "tacticas": ["Protocolo de Silencio: Dejá de pedir explicaciones.", "Auditoría Invisible: Observá micro-movimientos.", "Patrón Interruptor: Actuá con serenidad total."],
            "gancho": "La Ingeniería de Comportamiento busca tu soberanía."
        },
        "Desbalance": {
            "titulo": "DESBALANCE: Asimetría de Esfuerzo",
            "diag": "Existe una 'deuda sistémica'. Uno provee orden y el otro consume recursos.",
            "codigo": "Contrato Invisible",
            "tacticas": ["Mapeo de Cláusulas: Identificá qué cediste.", "Retirada Estratégica: Dejá de cubrir faltas.", "Redefinición de Roles: Verbalizá el nuevo estándar."],
            "gancho": "El resentimiento es el síntoma, el contrato es la causa."
        },
        "Coherencia": {
            "titulo": "COHERENCIA: Estabilización y Reseteo",
            "diag": "Sincronización de la Lattice. El sistema entra en modo de expansión.",
            "codigo": "Arquitectura de Poder",
            "tacticas": ["Check-up Quincenal: Auditoría de metas.", "Blindaje de Comunicación: Eliminar ruido externo.", "Anclaje de Coherencia: Celebrar límites respetados."],
            "gancho": "La mentoría asegura no volver a viejos surcos."
        }
    },
    "Sociedad Comercial": {
        "Crítico": {
            "titulo": "VACIADO CRÍTICO: Fuga de Activos",
            "diag": "El socio activó el código de 'Depredador' para maximizar su beneficio individual.",
            "codigo": "Vaciado de Valor",
            "tacticas": ["Cierre de Nodos: Limitá acceso a info crítica.", "Documentación: Registrá inconsistencias.", "Presuasión: Lealtad vs Traición."],
            "gancho": "En guerra comercial, gana quien gestiona la psicología."
        },
        "Desbalance": {
            "titulo": "DESBALANCE: Desbalance Operativo",
            "diag": "Parásito sistémico. La estructura se mantiene solo por tu energía.",
            "codigo": "Fuga de Soberanía",
            "tacticas": ["Métricas: Definí desempeño innegociable.", "Cese de Subvención: No hagas su trabajo.", "Hechos: Confrontá sin emociones."],
            "gancho": "Reconfiguramos tu identidad de líder."
        },
        "Coherencia": {
            "titulo": "COHERENCIA: Escalabilidad",
            "diag": "Flujo óptimo. La sociedad opera con alta resolución de problemas.",
            "codigo": "Sinergia Táctica",
            "tacticas": ["Innovación: Cuestioná sin ego.", "Blindaje: Protección contra competencia.", "Expansión: Conquista de territorios."],
            "gancho": "Mantenete en un nivel que la competencia ni imagine."
        }
    },
    "Vínculo Mixto": {
        "Crítico": {
            "titulo": "VACIADO CRÍTICO: Colapso de Dominios",
            "diag": "Interferencia destructiva. El conflicto emocional contamina la viabilidad financiera.",
            "codigo": "Efecto Cascada",
            "tacticas": ["Separación Quirúrgica: Casa vs Oficina.", "Mediación: Activá tercero neutral.", "Salvaguarda: Asegurá liquidez."],
            "gancho": "Solo el análisis biopsicológico salva imperios."
        },
        "Desbalance": {
            "titulo": "DESBALANCE: Empresa como Hijo Problemático",
            "diag": "Dejaron de ser amantes para ser empleados de su propio proyecto.",
            "codigo": "Asimetría de Prioridades",
            "tacticas": ["Citas: Tiempo sin pantallas.", "Energía: ¿Quién carga el peso?", "Identidad: Recordar el origen."],
            "gancho": "Usá la empresa como motor, no como tumba."
        },
        "Coherencia": {
            "titulo": "COHERENCIA: El Imperio Familiar",
            "diag": "Ecosistema cerrado de alta eficiencia y soberanía absoluta.",
            "codigo": "Escudo de Gobernanza",
            "tacticas": ["Legado: Plan a 10 años.", "Mantenimiento: Revisión de acuerdos.", "Intimidad: Nafta del motor comercial."],
            "gancho": "Protegé lo que tanto te costó construir."
        }
    }
}

if 'pantalla' not in st.session_state:
    st.session_state.pantalla = 'radar'

if st.session_state.pantalla == 'radar':
    st.markdown(f'<div class="header-box">{escudo_svg}<h1 style="color: #D4AF37; margin: 0;">PARTNERSHIP SHIELD</h1></div>', unsafe_allow_html=True)
    st.write("---")
    escenario = st.radio("**Seleccioná escenario:**", ["Relación de Pareja", "Sociedad Comercial", "Vínculo Mixto"], horizontal=True)
    
    c1, c2 = st.columns(2)
    with c1:
        f_cancel = st.slider("Incumplimiento de Acuerdos", 0, 10, 2, help="Frecuencia de promesas rotas.")
        friccion = st.slider("Fricción Operativa", 0, 10, 2, help="Nivel de discusiones constantes.")
    with c2:
        erosion = st.slider("Erosión del Valor", 0, 10, 2, help="Pérdida de autoridad ante el otro.")
        opacidad = st.select_slider("Hermetismo", options=["Transparencia", "Zonas Grises", "Opacidad Total"])

    t1, t2 = st.columns(2)
    with t1:
        gaslighting = st.toggle("Gaslighting", help="Invalidación de tu realidad.")
        culpa = st.toggle("Transferencia de Culpa", help="Sos el responsable de todo lo malo.")
        aislamiento = st.toggle("Aislamiento", help="Alejamiento de tus redes de apoyo.")
    with t2:
        amenazas = st.toggle("Amenazas", help="Ultimátums constantes.")
        refuerzo = st.toggle("Refuerzo Intermitente", help="Ciclos de afecto y castigo.")
        triangulacion = st.toggle("Triangulación", help="Uso de terceros para generar inseguridad.")

    if st.button("OBTENER DIAGNÓSTICO"):
        score = f_cancel + friccion + erosion + (15 if opacidad == "Opacidad Total" else 7 if opacidad == "Zonas Grises" else 0)
        score += (10 if gaslighting else 0) + (8 if culpa else 0) + (10 if amenazas else 0) + (8 if aislamiento else 0) + (10 if refuerzo else 0) + (7 if triangulacion else 0)
        st.session_state.score = score
        st.session_state.escenario = escenario
        st.session_state.pantalla = 'diagnostico'
        st.rerun()

elif st.session_state.pantalla == 'diagnostico':
    st.markdown(f'<div class="header-box">{escudo_svg}<h1 style="color: #D4AF37; margin: 0;">ANÁLISIS</h1></div>', unsafe_allow_html=True)
    nivel = "Crítico" if st.session_state.score >= 35 else "Desbalance" if st.session_state.score >= 16 else "Coherencia"
    info = CONTENIDOS[st.session_state.escenario][nivel]
    color_class = "card-red" if nivel == "Crítico" else "card-yellow" if nivel == "Desbalance" else "card-green"
    
    st.markdown(f"<div class='{color_class}'><h2 style='color:white; margin:0;'>{info['titulo']}</h2><p style='color:white;'>Score: {st.session_state.score}/75</p></div>", unsafe_allow_html=True)
    
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
    
    if st.button("SOLICITAR AUDITORÍA"):
        st.session_state.pantalla = 'mentoria'
        st.rerun()
    if st.button("← Volver"):
        st.session_state.pantalla = 'radar'
        st.rerun()

elif st.session_state.pantalla == 'mentoria':
    st.markdown(f'<div class="header-box">{escudo_svg}<h1 style="color: #D4AF37; margin: 0;">MENTORÍA</h1></div>', unsafe_allow_html=True)
    with st.form("f_final"):
        nombre = st.text_input("Nombre*")
        situacion = st.text_area("Situación*")
        if st.form_submit_button("ENVIAR A WHATSAPP"):
            msg = f"Auditoría: {st.session_state.escenario} - Score: {st.session_state.score}\nNombre: {nombre}"
            st.markdown(f'<a href="https://wa.me/59899816392?text={urllib.parse.quote(msg)}" target="_blank">📲 CLICK AQUÍ PARA ENVIAR</a>', unsafe_allow_html=True)

st.markdown("<p style='text-align: center; font-size: 0.8rem; margin-top: 50px; color: #555;'>Partnership Shield © 2026</p>", unsafe_allow_html=True)
