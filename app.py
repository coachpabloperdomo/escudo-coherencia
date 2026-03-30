import streamlit as st
import urllib.parse

# Configuración de página
st.set_page_config(page_title="Partnership Shield", page_icon="🛡️", layout="wide")

# Estilo Dorado y Negro (Branding Partnership Shield)
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { background-color: #D4AF37; color: black; font-weight: bold; border-radius: 10px; width: 100%; }
    .gold-text { color: #D4AF37; font-family: 'Georgia', serif; }
    div[data-testid="stForm"] { border: 1px solid #D4AF37; border-radius: 15px; padding: 20px; }
    </style>
    """, unsafe_allow_html=True)

# Encabezado
st.markdown("<h1 style='text-align: center; color: #D4AF37;'>🛡️ PARTNERSHIP SHIELD</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-style: italic; color: #C0C0C0;'>Arquitectura del Comportamiento Humano & Estrategia Biopsicológica</p>", unsafe_allow_html=True)
st.markdown("---")

# 1. Escenario
escenario = st.radio(
    "**¿Qué estructura estamos auditando hoy?**", 
    ["Relación de Pareja", "Sociedad Comercial", "Sociedad & Pareja (Vínculo Mixto)"],
    horizontal=True
)

st.write("---")

# 2. Radar de Comportamiento (Icono de Radar 📡)
st.markdown("<h3 class='gold-text'>📡 Radar de Comportamiento</h3>", unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    st.write("**Fugas de Transparencia & Coherencia**")
    f_cancel = st.slider("Incumplimiento de acuerdos/citas (0-10)", 0, 10, 2, 
                        help="Mide la ruptura de la palabra empeñada. Indica falta de compromiso real.")
    claridad = st.select_slider("Acceso a información (Cuentas, Tiempos, Datos)", 
                               options=["Transparencia", "Zonas Grises", "Opacidad Total"],
                               help="La retención de información es la base del control asimétrico.")
    triangulacion = st.toggle("¿Hay terceros validando decisiones?", 
                             help="Socio/pareja busca aliados externos para desautorizar tu criterio.")
    com_pasiva = st.toggle("¿Comunicación pasivo-agresiva?", 
                          help="Uso del silencio o sarcasmo para castigar en lugar de resolver.")

with col2:
    st.write("**Alertas de Poder & Manipulación**")
    gaslighting = st.toggle("¿Gaslighting detectado?", 
                           help="Técnica para hacerte dudar de tu propia memoria o percepción.")
    culpa = st.toggle("¿Responsabilidad transferida?", 
                     help="Te culpan por sus errores o reacciones, evitando su responsabilidad.")
    aislamiento = st.toggle("¿Aislamiento estratégico?", 
                           help="Intentan separarte de aliados o familia para debilitar tu posición.")
    persuasion_neg = st.toggle("¿Persuasión negativa?", 
                              help="Uso de amenazas veladas o falsas promesas futuras.")

# 3. Calculadora de Fuga de Valor
st.markdown("---")
st.markdown("<h3 class='gold-text'>💸 Calculadora de Fuga de Valor</h3>", unsafe_allow_html=True)
c1, c2 = st.columns(2)
with c1:
    valor_hora = st.number_input("Tu valor hora (USD):", min_value=1, value=50)
with c2:
    horas_perdidas = st.number_input("Horas/semana de conflicto:", min_value=0, value=5)

fuga_mensual = valor_hora * horas_perdidas * 4
st.metric("Pérdida Mensual de Capital Humano/Económico:", f"US$ {fuga_mensual}")

# 4. Lógica de Diagnóstico
score = f_cancel + (10 if claridad == "Opacidad Total" else 5 if claridad == "Zonas Grises" else 0)
score += (7 if triangulacion else 0) + (5 if com_pasiva else 0) + (15 if gaslighting else 0)
score += (8 if culpa else 0) + (10 if aislamiento else 0) + (7 if persuasion_neg else 0)

st.markdown("---")
if score >= 20:
    st.error("### 🚨 ESTATUS: VACIADO CRÍTICO")
    st.write("**Acción Táctica:** Iniciá el 'Protocolo de Observación Silenciosa'. No des más explicaciones.")
    st.code("Hola. He decidido que todo acuerdo será documentado. No responderé a comunicaciones fuera de este protocolo.", language="text")
elif 10 <= score < 20:
    st.warning("### ⚠️ ESTATUS: DESBALANCE ESTRATÉGICO")
    st.write("Sugerencia: Aplicá el 'Patrón Interruptor'. Rompé el ciclo de reacción inmediata.")
else:
    st.success("### ✅ ESTATUS: COHERENCIA ESTABLE")
    st.write("El sistema es saludable. Recomendamos auditorías preventivas.")

# 5. Formulario de Contacto (Campos Obligatorios)
st.markdown("---")
st.markdown("<h3 style='text-align: center; color: #D4AF37;'>¿Necesitás detener la fuga hoy mismo?</h3>", unsafe_allow_html=True)
st.write("<p style='text-align: center;'>Completá tus datos para recibir tu evaluación estratégica por WhatsApp.</p>", unsafe_allow_html=True)

with st.form("contacto_pablo"):
    nombre = st.text_input("Nombre Completo (Obligatorio)*")
    situacion = st.text_area("Describí tu situación actual (Obligatorio)*")
    
    submit = st.form_submit_button("AGENDAR EVALUACIÓN ESTRATÉGICA")
    
    if submit:
        if not nombre or not situacion:
            st.warning("⚠️ Por favor, completá tu nombre y situación para poder ayudarte.")
        else:
            st.balloons()
            # Datos técnicos para el mensaje
            resumen_tecnico = f"Puntaje de Vaciado: {score}/50 | Fuga económica: USD {fuga_mensual}"
            
            # Formateo del mensaje para WhatsApp
            texto_base = (
                f"Hola Pablo, mi código es #COHERENCIA2026.\n\n"
                f"Nombre: {nombre}\n"
                f"Escenario: {escenario}\n"
                f"Diagnóstico: {resumen_tecnico}\n"
                f"Situación: {situacion}"
            )
            # Codificación segura para URL
            texto_url = urllib.parse.quote(texto_base)
            link_wa = f"https://wa.me/59899816392?text={texto_url}"
            
            st.success("✅ Diagnóstico preparado con éxito.")
            st.markdown(f'<a href="{link_wa}" target="_blank" style="text-decoration:none;"><div style="background-color:#25D366;color:white;padding:15px;border-radius:10px;text-align:center;font-weight:bold;">📩 ENVIAR RESULTADOS POR WHATSAPP A PABLO</div></a>', unsafe_allow_html=True)

st.markdown("<p style='text-align: center; font-size: 0.8rem; color: #C0C0C0;'>Partnership Shield © 2026 | Arquitectura del Comportamiento Humano</p>", unsafe_allow_html=True)
