import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Escudo de Coherencia", page_icon="🛡️")

# Estética Profesional
st.title("🛡️ Escudo de Coherencia")
st.subheader("Detector de 'Vaciado de Atención' y Alerta Táctica")
st.markdown("---")

# 1. Identificación del Escenario
tipo_vinculo = st.selectbox(
    "Seleccioná el tipo de relación que querés auditar:",
    ["Relación de Pareja", "Sociedad Comercial / Negocio"]
)

st.info("Respondé con total honestidad. Los datos son volátiles y no se guardan en esta sesión.")

# 2. El Escáner (Preguntas de "Radar")
st.write("### 🔍 Escáner de Comportamiento")

# Categoría A: Operativa (Tiempo y Dinero)
st.write("**A. Gestión de Recursos**")
p1 = st.slider("¿Qué tan frecuente es que se cancelen acuerdos o reuniones sin aviso previo?", 0, 10, 5)
p2 = st.radio("¿Hay claridad total sobre el uso del tiempo o dinero en la última semana?", ["Sí, total", "Hay zonas grises", "Opacidad absoluta"])

# Categoría B: Poder y Percepción (Gaslighting/Manipulación)
st.write("**B. Dinámica de Poder**")
p3 = st.checkbox("¿Sentís que cuestionan tu memoria sobre hechos que estás seguro/a que pasaron?")
p4 = st.checkbox("¿Te sentís responsable por el malestar o la inacción de la otra parte?")

# 3. Lógica de Cálculo (El "Radar")
score = p1
if p2 == "Hay zonas grises": score += 3
if p2 == "Opacidad absoluta": score += 7
if p3: score += 10 # Gaslighting es Alerta Roja inmediata
if p4: score += 5

# 4. ENTREGA DE SOLUCIÓN (La "Bajada a Tierra")
st.markdown("---")
st.write("### 🚨 Resultado del Radar")

if score >= 15:
    st.error("### ¡ALERTA ROJA: Vaciado Crítico Detectado!")
    st.markdown("""
    **Solución Inmediata (Tu 'Radar' te indica):**
    1. **Cese de Información:** Dejá de compartir planes futuros o ideas nuevas de inmediato. La otra parte está en modo 'extracción'.
    2. **Protocolo de Registro:** A partir de este momento, comunicate ÚNICAMENTE por escrito (Email/WhatsApp). No aceptes acuerdos verbales.
    3. **Pregunta de Quiebre:** En el próximo encuentro, preguntá: *'Noté que los acuerdos previos no se están cumpliendo, ¿cuál es tu intención real con este proyecto/relación hoy?'*. No expliques, solo escuchá.
    """)
elif 7 <= score < 15:
    st.warning("### ALERTA AMARILLA: Desviación de Coherencia")
    st.markdown("""
    **Solución Inmediata:**
    1. **Observación Silenciosa:** No reclames. Observá si el patrón se repite 3 veces más.
    2. **Fijar Límite de Tiempo:** Si hay una tarea o compromiso pendiente, poné una fecha límite hoy mismo.
    """)
else:
    st.success("### Coherencia Estable")
    st.write("El vínculo muestra niveles saludables de transparencia. Seguí construyendo sobre esta base.")

# 5. EL PUENTE AL ALTO VALOR (Solo después de ayudar)
st.markdown("---")
with st.expander("🚀 ¿Necesitás una Estrategia Quirúrgica de Salida o Re-negociación?"):
    st.write("""
    Si el radar dio **Rojo** y sentís que estás perdiendo el control de tu capital emocional o financiero, es momento de una intervención profesional.
    
    Podés calificar para una mentoría estratégica uno a uno para diseñar tu escudo de protección definitivo.
    """)
    st.button("Calificar para Mentoría High Ticket")
