import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración estética
st.set_page_config(page_title="SÖV - Ingeniería de la Soberanía", layout="centered")

st.title("🛡️ SÖV: Sistema Operativo de Vínculos")
st.subheader("Radar de Soberanía y Mando")
st.markdown("---")

# 1. Segmentación
tipo_vinculo = st.selectbox(
    "Seleccione el tipo de vínculo a auditar:",
    ["Personal / Pareja", "Socios Comerciales", "Vínculo Mixto"]
)

# 2. Preguntas Organizadas por Dimensión
st.write("### 📝 Cuestionario de Diagnóstico")
st.info("Responde del 1 (Nunca/Nada) al 5 (Siempre/Totalmente)")

# Definimos las dimensiones para el gráfico de radar
dimensiones = {
    "Soberanía y Mando": [0, 1, 2, 3, 4],
    "Reciprocidad": [5, 6, 7, 8, 9],
    "Estabilidad": [10, 11, 12, 13, 14]
}

preguntas = [
    "¿Controlas tu agenda y finanzas sin dar explicaciones?",
    "¿Tu energía al final del día es óptima para vos?",
    "¿Tu identidad es independiente del vínculo?",
    "¿Sabés decir 'no' sin sentir culpa?",
    "¿Tus activos están protegidos de crisis ajenas?",
    "¿El esfuerzo en el vínculo está equilibrado 50/50?",
    "¿Las charlas terminan en acuerdos técnicos claros?",
    "¿Confías en que el otro cumple sin supervisión?",
    "¿El vínculo multiplica tus resultados?",
    "¿Se respetan tus límites y espacios privados?",
    "¿El ambiente habitual es de calma y enfoque?",
    "¿Pasas días sin 'incendios' que requieran tu mando?",
    "¿Hablan un lenguaje común (visión compartida)?",
    "¿La comunicación es honesta y sin ironías?",
    "¿El sistema es sostenible a largo plazo sin agotarte?"
]

respuestas = []
for i, pregunta in enumerate(preguntas):
    res = st.select_slider(f"{i+1}. {pregunta}", options=[1, 2, 3, 4, 5], value=3)
    respuestas.append(res)

# 3. Lógica de Resultados
if st.button("GENERAR DIAGNÓSTICO ESTRATÉGICO"):
    puntaje_total = sum(respuestas)
    score_riesgo = 75 - puntaje_total  # Invertimos: a menos puntos, más riesgo.
    
    st.markdown("---")
    st.header(f"Tu Score SÖV: {score_riesgo}")
    
    # 4. Cálculo de promedios para el Gráfico de Radar
    promedios = []
    for nombre, indices in dimensiones.items():
        valores = [respuestas[i] for i in indices]
        promedios.append(sum(valores) / len(valores))
    
    df_radar = pd.DataFrame(dict(
        r=promedios,
        theta=list(dimensiones.keys())
    ))
    
    fig = px.line_polar(df_radar, r='r', theta='theta', line_close=True)
    fig.update_traces(fill='toself', line_color='#FF4B4B')
    fig.update_polars(radialaxis=dict(visible=True, range=[0, 5]))
    
    st.plotly_chart(fig)
    
    if score_riesgo <= 14:
        st.success("ESTADO: COHERENCIA. Sistema estable, requiere blindaje preventivo.")
    elif score_riesgo <= 34:
        st.warning("ESTADO: DESBALANCE. Fuga de activos detectada. Requiere reingeniería.")
    else:
        st.error("ESTADO: CRÍTICO. Colapso sistémico. Requiere intervención quirúrgica.")
