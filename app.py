import streamlit as st

# Configuración con estética dorada y profesional
st.set_page_config(page_title="Partnership Shield", page_icon="🛡️", layout="wide")

# Estilo personalizado para el Dorado y el Escudo
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { background-color: #D4AF37; color: black; font-weight: bold; border-radius: 10px; }
    .gold-text { color: #D4AF37; font-family: 'Georgia', serif; }
    </style>
    """, unsafe_allow_html=True)

# Título con Identidad de Marca
st.markdown("<h1 style='text-align: center; color: #D4AF37;'>🛡️ PARTNERSHIP SHIELD</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-style: italic; color: #C0C0C0;'>Arquitectura del Comportamiento Humano & Estrategia Biopsicológica</p>", unsafe_allow_html=True)
st.markdown("---")

# 1. Selección de Escenario
escenario = st.radio(
    "**¿Qué estructura estamos auditando hoy?**", 
    ["Relación de Pareja", "Sociedad Comercial", "Sociedad & Pareja (Vínculo Mixto)"],
    horizontal=True
)

st.write("---")

# 2. Radar de Comportamiento Extendido
st.markdown("<h3 class='gold-text'>🔍 Radar de Comportamiento</h3>", unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    st.write("**Fugas de Transparencia & Coherencia**")
    f_cancel = st.slider("Incumplimiento de acuerdos/citas (0-10)", 0, 10, 2)
    claridad = st.select_slider("Acceso a información (Cuentas, Tiempos, Datos)", options=["Transparencia", "Zonas Grises", "Opacidad Total"])
    triangulacion = st.toggle("¿Hay terceros validando decisiones antes que vos?")
    com_pasiva = st.toggle("¿Notas comunicación pasivo-agresiva o silencios punitivos?")

with col2:
    st.write("**Alertas de Poder & Manipulación**")
    gaslighting = st.toggle("¿Invalidan tu percepción de la realidad? (Gaslighting)")
    culpa = st.toggle("¿Te responsabilizan por sus reacciones o fracasos?")
    aislamiento = st.toggle("¿Sientes que te limitan el contacto con aliados o red de apoyo?")
    persuasion_neg = st.toggle("¿Uso de amenazas sutiles o 'promesas' que nunca llegan?")

# 3. Calculadora de Fuga de Valor
st.markdown("---")
st.markdown("<h3 class='gold-text'>💸 Calculadora de Fuga de Valor</h3>", unsafe_allow_html=True)
c1, c2 = st.columns(2)
with c1:
    valor_hora = st.number_input("Tu valor hora estimado (USD):", min_value=1, value=50)
with c2:
    horas_perdidas = st.number_input("Horas/semana perdidas en conflicto o parálisis:", min_value=0, value=5)

fuga_mensual = valor_hora * horas_perdidas * 4
st.metric("Pérdida de Capital Mensual (Tiempo/Energía):", f"US$ {fuga_mensual}")

# 4. Lógica de Diagnóstico Partnership Shield
score = f_cancel
if claridad == "Zonas Grises": score += 5
if claridad == "Opacidad Total": score += 10
if triangulacion: score += 7
if com_pasiva: score += 5
if gaslighting: score += 15
if culpa: score += 8
if aislamiento: score += 10
if persuasion_neg: score += 7

# 5. Entrega de Valor Táctico
st.markdown("---")
if score >= 20:
    st.error("### 🚨 ESTATUS: VACIADO CRÍTICO")
    st.write("**Diagnóstico:** Estás bajo un proceso de extracción activa.")
    
    st.info("**🛠️ Script Táctico de Interrupción (Copiá y mandá):**")
    if escenario == "Sociedad Comercial":
        txt = "He detectado inconsistencias en el cumplimiento de los acuerdos. Para preservar el valor del proyecto, desde ahora toda gestión será documentada por escrito."
    elif escenario == "Relación de Pareja":
        txt = "Siento que nuestra comunicación ha perdido coherencia. Necesito espacio para procesar los hechos; por el momento, no participaré en discusiones verbales."
    else:
        txt = "Dada la naturaleza mixta de nuestro vínculo, la falta de transparencia actual pone en riesgo ambos planos. He decidido separar la operativa de lo personal."
    
    st.code(txt)

elif 10 <= score < 20:
    st.warning("### ⚠️ ESTATUS: DESBALANCE ESTRATÉGICO")
    st.write("Sugerencia: Aplicá el 'Patrón Interruptor'. Dejá de reaccionar como ellos esperan.")
else:
    st.success("### ✅ ESTATUS: COHERENCIA OPERATIVA")
    st.write("El sistema es estable. Recomendamos auditorías mensuales preventivas.")

# 6. Conversión al High Ticket
st.markdown("---")
st.markdown("<h3 style='text-align: center; color: #D4AF37;'>¿Necesitás un Escudo Definitivo?</h3>", unsafe_allow_html=True)

with st.form("contacto_mentor"):
    nombre = st.text_input("Nombre completo")
    situacion = st.text_area("Describí brevemente tu situación actual")
    submit = st.form_submit_button("AGENDAR EVALUACIÓN ESTRATÉGICA")
    
    if submit:
        st.balloons()
        mensaje_wa = f"Hola Pablo, mi código es #COHERENCIA2026. Nombre: {nombre}. Situación: {situacion}"
        link_wa = f"https://wa.me/59899816392?text={mensaje_wa.replace(' ', '%20')}"
        st.success("✅ Registro listo. Hacé clic abajo para enviar por WhatsApp.")
        st.markdown(f"[📩 ENVIAR WHATSAPP A PABLO]({link_wa})")

st.markdown("<p style='text-align: center; font-size: 0.8rem;'>Partnership Shield © 2026</p>", unsafe_allow_html=True)
