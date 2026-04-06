import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="SÖV - Radar de Soberanía", layout="centered")

st.title("🛡️ SÖV: Sistema Operativo de Vínculos")
st.markdown("---")

# 1. Selección de Vínculo
tipo = st.selectbox("Auditar vínculo:", ["Personal / Pareja", "Socios", "Mixto"])

# 2. Las 5 Dimensiones de SÖV (Simplificadas para el gráfico)
st.subheader("Puntúa de 1 (Riesgo) a 5 (Soberanía)")

c1, c2 = st.columns(2)
with c1:
    autonomia = st.slider("Autonomía y Agenda", 1, 5, 3)
    energia = st.slider("Nivel de Energía", 1, 5, 3)
    limites = st.slider("Límites y Culpa", 1, 5, 3)
with c2:
    economia = st.slider("Activos y Finanzas", 1, 5, 3)
    acuerdos = st.slider("Acuerdos Técnicos", 1, 5, 3)

# 3. Lógica del Radar
df = pd.DataFrame(dict(
    r=[autonomia, energia, limites, economia, acuerdos],
    theta=['Autonomía', 'Energía', 'Límites', 'Economía', 'Acuerdos']
))

fig = px.line_polar(df, r='r', theta='theta', line_close=True)
fig.update_traces(fill='toself', line_color='#00FFCC')
fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 5])))

# 4. Mostrar Resultados
if st.button("GENERAR DIAGNÓSTICO SÖV"):
    st.plotly_chart(fig)
    score = sum([autonomia, energia, limites, economia, acuerdos])
    st.metric("Score de Soberanía", f"{score}/25")
    
    if score < 15:
        st.error("⚠️ ALERTA: El sistema detecta alta reactividad. Riesgo de pérdida de activos.")
    else:
        st.success("✅ SISTEMA ESTABLE: Soberanía funcional detectada.")
