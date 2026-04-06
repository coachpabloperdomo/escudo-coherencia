import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Configuración de la Página para Diseño Vanguardista
st.set_page_config(page_title="SÖV - Radar de Soberanía", layout="wide", initial_sidebar_state="collapsed")

# 1. --- CSS PERSONALIZADO (Magia de Diseño) ---
# Aquí definimos colores, fondos oscuros y efectos de neón.
st.markdown("""
<style>
    /* Fondo oscuro y tipografía futurista */
    .stApp {
        background-color: #050A19;
        color: #E0E6ED;
        font-family: 'Courier New', Courier, monospace;
    }

    /* Estilo para los Títulos */
    h1 {
        color: #00FFCC !important;
        text-align: center;
        text-shadow: 0 0 10px #00FFCC, 0 0 20px #00FFCC;
        letter-spacing: 2px;
        text-transform: uppercase;
    }

    /* Contenedores con efecto de vidrio (Glassmorphism) */
    div.stBlock {
        background: rgba(16, 26, 50, 0.8);
        border-radius: 15px;
        padding: 20px;
        border: 1px solid rgba(0, 255, 204, 0.2);
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.5);
    }

    /* Sliders personalizados con color neón */
    .stSlider > div > div > div > div {
        background-color: #00FFCC;
    }
    
    /* Botón futurista */
    .stButton > button {
        background-color: transparent;
        color: #00FFCC;
        border: 2px solid #00FFCC;
        border-radius: 20px;
        text-transform: uppercase;
        letter-spacing: 1px;
        width: 100%;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #00FFCC;
        color: #050A19;
        box-shadow: 0 0 15px #00FFCC;
    }
</style>
""", unsafe_with_html=True)

# 2. --- ENCABEZADO Y SELECTOR ---
# Usamos un contenedor estilizado para el título
with st.container():
    st.markdown("<h1>SÖV: Radar de Soberanía Funcional</h1>", unsafe_with_html=True)
    st.markdown("<p style='text-align:center; color:#8899A6;'>Sistema Operativo de Vínculos</p>", unsafe_with_html=True)
    st.markdown("---")

# 3. --- PANEL DE CONTROL (Slidrs) Y RESULTADO (Radar) ---
# Dividimos la pantalla en dos columnas para un diseño más moderno
col_controles, col_radar = st.columns([1, 1.5])

with col_controles:
    st.markdown("<h3>Controles de Entrada</h3>", unsafe_with_html=True)
    st.markdown("<p style='color:#8899A6; font-size:12px;'>Califica de 1 (Riesgo/Rojo) a 5 (Soberanía/Verde)</p>", unsafe_with_html=True)
    
    # Aquí definimos las 5 Dimensiones del SÖV
    autonomia = st.slider("Autonomía y Agenda", 1, 5, 3, help="¿Control total sobre tus decisiones?")
    energia = st.slider("Nivel de Energía", 1, 5, 3, help="¿Cómo terminas el día?")
    economia = st.slider("Activos y Finanzas", 1, 5, 3, help="¿Protegido de crisis externas?")
    acuerdos = st.slider("Acuerdos Técnicos", 1, 5, 3, help="¿Conversaciones fluidas y claras?")
    limites = st.slider("Límites y Culpa", 1, 5, 3, help="¿Capacidad de decir 'no'?")
    
    # Botón de cálculo estilizado
    st.markdown("<div style='margin-top:20px;'>", unsafe_with_html=True)
    btn_calcular = st.button("ANALIZAR VÍNCULO")
    st.markdown("</div>", unsafe_with_html=True)

# 4. --- LÓGICA Y GRÁFICO (Radar Profundo) ---
with col_radar:
    # Datos para el gráfico
    niveles = [autonomia, energia, economia, acuerdos, limites]
    labels = ['Autonomía', 'Energía', 'Finanzas', 'Acuerdos', 'Límites']

    # Crear el Gráfico de Radar Profundo con Plotly Go (más personalizable)
    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=niveles,
        theta=labels,
        fill='toself',
        name='SÖV Score',
        # Color del relleno y la línea (Neón)
        fillcolor='rgba(0, 255, 204, 0.3)',
        line=dict(color='#00FFCC', width=3),
        marker=dict(color='#00FFCC', size=8)
    ))

    # Configuración Vanguardista del Layout
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 5],
                color='#8899A6',
                gridcolor='rgba(136, 153, 166, 0.2)', # Líneas de cuadrícula sutiles
                font=dict(size=10)
            ),
            angularaxis=dict(
                color='#E0E6ED', # Color de las etiquetas exteriores
                font=dict(size=12)
            ),
            bgcolor='rgba(0,0,0,0)' # Fondo transparente del gráfico
        ),
        showlegend=False,
        paper_bgcolor='rgba(0,0,0,0)', # Fondo transparente del papel
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(t=30, b=30, l=30, r=30)
    )

    # Solo mostramos el radar y el score si se presiona el botón
    if btn_calcular:
        st.plotly_chart(fig, use_container_width=True)
        
        # Cálculo del Score Final
        score = sum(niveles)
        
        # Métrica de Score con diseño neón
        st.markdown(f"""
        <div style='text-align:center; padding:20px; border-radius:15px; border:1px solid #00FFCC; box-shadow:0 0 10px #00FFCC;'>
            <h2 style='color:#E0E6ED; margin:0;'>SCORE SÖV FINAL</h2>
            <h1 style='color:#00FFCC; font-size:60px; margin:0;'>{score} <span style='font-size:30px; color:#8899A6;'>/ 25</span></h1>
        </div>
        """, unsafe_with_html=True)
