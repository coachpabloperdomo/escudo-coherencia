import streamlit as st

st.set_page_config(page_title="Escudo de Coherencia", page_icon="🛡️")

st.title("🛡️ Escudo de Coherencia")
st.subheader("Tu GPS Táctico para Vínculos y Sociedades")
st.markdown("---")

# 1. Selección de Escenario
escenario = st.radio("¿Qué estamos auditando hoy?", ["Relación de Pareja", "Sociedad Comercial"])

# 2. El Escáner de Radar
st.write("### 🔍 Radar de Comportamiento")

col1, col2 = st.columns(2)

with col1:
    st.write("**Fugas de Transparencia**")
    frecuencia_cancelacion = st.slider("Cancelaciones de acuerdos/citas (0-10)", 0, 10, 2)
    claridad = st.select_slider("Nivel de claridad en info/dinero", options=["Total", "Gris", "Opacidad"])

with col2:
    st.write("**Alertas de Poder**")
    gaslighting = st.toggle("¿Cuestionan tu memoria o cordura? (Gaslighting)")
    culpa = st.toggle("¿Sentís culpa por pedir rendición de cuentas?")

# 3. Calculadora de Daño (BAJADA A TIERRA)
st.markdown("---")
st.write("### 💸 Calculadora de Fuga de Valor")
valor_hora = st.number_input("¿Cuánto vale tu hora de trabajo (USD)?", min_value=1, value=50)
horas_perdidas = st.number_input("Horas semanales perdidas en discusiones o esperas:", min_value=0, value=5)

fuga_mensual = valor_hora * horas_perdidas * 4
st.metric("Fuga de Valor Mensual estimada:", f"US$ {fuga_mensual}")

# 4. Lógica de Alerta
score = frecuencia_cancelacion
if claridad == "Gris": score += 5
if claridad == "Opacidad": score += 10
if gaslighting: score += 15
if culpa: score += 5

st.markdown("---")
if score >= 15:
    st.error("### 🚨 ALERTA ROJA: Vaciado Activo")
    st.write("**Diagnóstico:** Estás en una dinámica de extracción. Tu atención está siendo vaciada.")
    
    # SOLUCIÓN REAL: El "Script de WhatsApp"
    st.info("**🛠️ Acción Inmediata (Copiá y mandá esto):**")
    if escenario == "Sociedad Comercial":
        script = "Hola. Noté que los compromisos previos no se están cumpliendo. Para proteger el proyecto, a partir de ahora toda comunicación operativa será solo por escrito. Quedo atento a la rendición pendiente."
    else:
        script = "Hola. No me siento cómodo/a con cómo se están manejando los acuerdos. Necesito tomarme un tiempo para observar los hechos objetivamente. Por ahora, prefiero no discutir este tema verbalmente."
    
    st.code(script)
    st.caption("Mantené el silencio después de enviar. No des explicaciones.")

elif 8 <= score < 15:
    st.warning("### ⚠️ ALERTA AMARILLA: Desbalance detectado")
    st.write("Sugerencia: Aplicá el 'Código de Persuasión' y observá la reacción del otro sin confrontar.")

else:
    st.success("### ✅ Coherencia Estable")
    st.write("El vínculo es productivo. Seguí manteniendo la transparencia.")

# 5. Salida al High Ticket
st.markdown("---")
if st.button("🚀 Quiero calificar para Mentoría Estratégica con Pablo"):
    st.balloons()
    st.write("Copiá este código de diagnóstico: **#COHERENCIA2026** y envialo por privado para tu evaluación.")
