import streamlit as st

# Configuración de página
st.set_page_config(page_title="Partnership Shield", page_icon="🛡️", layout="wide")

# Estilo Dorado y Negro
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { background-color: #D4AF37; color: black; font-weight: bold; border-radius: 10px; width: 100%; }
    .gold-text { color: #D4AF37; font-family: 'Georgia', serif; }
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
                        help="Mide la ruptura de la palabra empeñada. Un valor alto indica falta de compromiso real.")
    claridad = st.select_slider("Acceso a información (Cuentas, Tiempos, Datos)", 
                               options=["Transparencia", "Zonas Grises", "Opacidad Total"],
                               help="La retención de información es la base del control asimétrico.")
    triangulacion = st.toggle("¿Hay terceros validando decisiones?", 
                             help="Ocurre cuando el socio/pareja busca aliados externos para desautorizar tu criterio.")
    com_pasiva = st.toggle("¿Comunicación pasivo-agresiva?", 
                          help="Uso del silencio o sarcasmo para castigar en lugar de resolver.")

with col2:
    st.write("**Alertas de Poder & Manipulación**")
    gaslighting = st.toggle("¿Gaslighting detectado?", 
                           help="Técnica de manipulación para hacerte dudar de tu propia memoria o percepción de los hechos.")
    culpa = st.toggle("¿Responsabilidad transferida?", 
                     help="Te culpan por sus errores o por cómo ellos se sienten, evitando la responsabilidad.")
    aislamiento = st.toggle("¿Aislamiento estratégico?", 
                           help="Intentan separarte de tus aliados, familia o asesores para debilitar tu posición.")
    persuasion_neg = st.toggle("¿Persuasión negativa?", 
                              help="Uso de amenazas veladas ('Si no hacés esto, entonces...') o falsas promesas futuras.")

# 3. Calculadora de Fuga de Valor
st.markdown("---")
st.markdown("<h3 class='gold-text'>💸 Calculadora de Fuga de Valor</h3>", unsafe_allow_html=True)
c1, c2 = st.columns(2)
with c1:
    valor_hora = st.number_input("Tu valor hora (USD):", min_value=1, value=50, help="¿Cuánto vale una hora de tu paz y productividad?")
with c2:
    horas_perdidas = st.number_input("Horas/semana de conflicto:", min_value=0, value=5, help="Tiempo invertido en rumiar el problema o en discusiones circulares.")

fuga_mensual = valor_hora * horas_perdidas * 4
st.metric("Fuga Mensual de Capital Humano/Económico:", f"US$ {fuga_mensual}")

# 4. Diagnóstico y Entrega de Valor
st.markdown("---")
score = f_cancel + (10 if claridad == "Opacidad Total" else 5 if claridad == "Zonas Grises" else 0)
score += (7 if triangulacion else 0) + (5 if com_pasiva else 0) + (15 if gaslighting else 0)
score += (8 if culpa else 0) + (10 if aislamiento else 0) + (7 if persuasion_neg else 0)

if score >= 20:
    st.error("### 🚨 ESTATUS: VACIADO CRÍTICO")
    st.write("**Acción Táctica Sugerida:** Dejá de alimentar el sistema con información. Iniciá el 'Protocolo de Observación Silenciosa'.")
    script = "Hola. He decidido que para cuidar el vínculo, de ahora en adelante todo acuerdo será documentado. No responderé a comunicaciones fuera de este protocolo."
    st.code(script, language="text")
    mostrar_formulario = True
elif 10 <= score < 20:
    st.warning("### ⚠️ ESTATUS: DESBALANCE ESTRATÉGICO")
    st.write("Sugerencia: Aplicá el 'Patrón Interruptor'. Rompé el ciclo de reacción inmediata.")
    mostrar_formulario = True
else:
    st.success("### ✅ ESTATUS: COHERENCIA ESTABLE")
    st.write("El sistema es saludable. Recomendamos auditorías preventivas.")
    mostrar_formulario = False

# 5. Formulario Final (Solo si hay alerta o al final del proceso)
if mostrar_formulario or score < 10:
    st.markdown("---")
    st.markdown("<h3 style='text-align: center; color: #D4AF37;'>¿Querés detener la fuga hoy mismo?</h3>", unsafe_allow_html=True)
    
    with st.form("contacto_mentor"):
        nombre = st.text_input("Nombre")
        situacion = st.text_area("Describí tu situación")
        submit = st.form_submit_button("SOLICITAR EVALUACIÓN ESTRATÉGICA")
        
        if submit:
            st.balloons()
            # Resumen técnico para que te llegue a vos
            resumen = f"Puntaje: {score}/50 | Fuga: USD {fuga_mensual}"
            msg_wa = f"Hola Pablo, mi código es #COHERENCIA2026. Nombre: {nombre}. Diagnóstico: {resumen}. Situación: {situacion}"
            link_wa = f"https://wa.me/59899816392?text={msg_wa.replace(' ', '%20')}"
            
            st.success("✅ Diagnóstico preparado. Hacé clic abajo para enviármelo por WhatsApp y agendar.")
            st.markdown(f"[📩 ENVIAR RESULTADOS POR WHATSAPP]({link_wa})")

st.markdown("<p style='text-align: center; font-size: 0.8rem;'>Partnership Shield © 2026 | Estratega Pablo Perdomo</p>", unsafe_allow_html=True)
