import streamlit as st
import urllib.parse

# 1. Configuración de Página
st.set_page_config(page_title="Partnership Shield", page_icon="🛡️", layout="wide")

# Estilos CSS Profesionales - CORREGIDOS PARA LEGIBILIDAD
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { background-color: #D4AF37; color: black; font-weight: bold; border-radius: 10px; height: 3.5em; width: 100%; border: none; }
    .gold-text { color: #D4AF37; font-family: 'Georgia', serif; text-align: center; }
    .header-box { display: flex; justify-content: center; align-items: center; margin-bottom: 10px; }
    .card-red { background-color: #2b0b0b; padding: 25px; border-radius: 15px; border: 1px solid #ff4b4b; margin-bottom: 25px; border-left: 10px solid #ff4b4b; }
    .card-yellow { background-color: #2b260b; padding: 25px; border-radius: 15px; border: 1px solid #f1c40f; margin-bottom: 25px; border-left: 10px solid #f1c40f; }
    .card-green { background-color: #0b2b0f; padding: 25px; border-radius: 15px; border: 1px solid #2ecc71; margin-bottom: 25px; border-left: 10px solid #2ecc71; }
    
    /* RECUADRO DE TÁCTICAS CORREGIDO (Texto en blanco/plata) */
    .tactic-box { 
        background-color: #161b22; 
        padding: 15px; 
        border-radius: 8px; 
        border-top: 2px solid #D4AF37; 
        margin-top: 10px; 
        color: #f0f0f0 !important;
        font-weight: 500;
    }
    
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

# Diccionario de Contenidos Maestros (Inalterado, es tu médula ósea)
CONTENIDOS = {
    "Relación de Pareja": {
        "Crítico": {
            "titulo": "VACIADO CRÍTICO: Crisis de Confianza",
            "diag": "El sistema nervioso está en 'alerta de supervivencia'. Tu inconsciente procesa la ambigüedad como una amenaza de muerte social, entrando en un bucle de hipervigilancia.",
            "codigo": "Blindaje de Salida",
            "tacticas": ["Protocolo de Silencio: Dejá de pedir explicaciones; la información es poder.", "Auditoría Invisible: Observá micro-movimientos sin confrontar.", "Patrón Interruptor: Actuá con serenidad total para descolocar al otro."],
            "gancho": "Un terapeuta busca el diálogo; la Ingeniería de Comportamiento busca tu soberanía."
        },
        "Desbalance": {
            "titulo": "DESBALANCE: Asimetría de Esfuerzo",
            "diag": "Existe una 'deuda sistémica'. Vos operás como proveedor de orden y el otro como consumidor, generando un vaciado de dopamina en vos y pérdida de respeto en el otro.",
            "codigo": "Contrato Invisible",
            "tacticas": ["Mapeo de Cláusulas: Identificá qué cediste para evitar conflicto.", "Retirada Estratégica: Dejá de cubrir las faltas del otro por 7 días.", "Redefinición de Roles: Verbalizá el nuevo estándar de intercambio."],
            "gancho": "El resentimiento es el síntoma, el contrato es la causa. Necesitás reconfiguración biopsicológica."
        },
        "Coherencia": {
            "titulo": "COHERENCIA: Estabilización y Reseteo",
            "diag": "Sincronización de la 'Lattice'. Se ha recuperado la seguridad básica y el sistema entra en modo de construcción y expansión.",
            "codigo": "Arquitectura de Poder",
            "tacticas": ["Check-up Quincenal: Auditoría de metas compartidas.", "Blindaje de Comunicación: Eliminar el ruido externo (familia/terceros).", "Anclaje de Coherencia: Celebrar hitos de límites respetados."],
            "gancho": "Mantener la coherencia es más difícil que salir de la crisis. La mentoría asegura no volver a viejos surcos."
        }
    },
    "Sociedad Comercial": {
        "Crítico": {
            "titulo": "VACIADO CRÍTICO: Fuga de Activos",
            "diag": "Desconexión total de valores. El socio activó el código de 'Depredador' para maximizar su beneficio individual a costa de la estructura común.",
            "codigo": "Vaciado de Valor",
            "tacticas": ["Cierre de Nodos: Limitá el acceso a información crítica discretamente.", "Documentación de Coherencia: Registrá cada inconsistencia entre dicho y hecho.", "Presuasión: Instalale la idea de que la lealtad es más rentable."],
            "gancho": "En guerra comercial, gana quien gestiona la psicología. No necesitás un abogado, necesitás un estratega."
        },
        "Desbalance": {
            "titulo": "DESBALANCE: Desbalance Operativo",
            "diag": "Parásito sistémico. La estructura se mantiene por tu energía, generando una 'inflación emocional' que hará colapsar la operatividad.",
            "codigo": "Fuga de Soberanía",
            "tacticas": ["Auditoría de Funciones: Definí métricas innegociables.", "Cese de Subvención: Dejá de hacer el trabajo del socio.", "Comunicación Biopsicológica: Confrontá con hechos, no emociones."],
            "gancho": "El desbalance es proyección de tu falta de límites. Reconfiguramos tu identidad de líder."
        },
        "Coherencia": {
            "titulo": "COHERENCIA: Escalabilidad y Confianza",
            "diag": "Flujo óptimo. La sociedad opera como una extensión del sistema nervioso de ambos, multiplicando la resolución de problemas.",
            "codigo": "Sinergia Táctica",
            "tacticas": ["Protocolo de Innovación: Espacios para cuestionar sin ego.", "Blindaje Externo: Protección contra ataques de la competencia.", "Expansión de Soberanía: Conquista de nuevos territorios comerciales."],
            "gancho": "La excelencia requiere mentalidad de Jugador Pro. Mantenete en un nivel que la competencia ni imagine."
        }
    },
    "Vínculo Mixto": {
        "Crítico": {
            "titulo": "VACIADO CRÍTICO: Colapso de Dominios",
            "diag": "Interferencia destructiva. El conflicto en la cama se traslada al balance contable. El sistema está al borde de la aniquilación total.",
            "codigo": "Efecto Cascada",
            "tacticas": ["Separación Quirúrgica: Prohibí hablar de negocios en casa y viceversa.", "Tercero Neutral: Activá mediación externa inmediata.", "Salvaguarda de Activos: Asegurá liquidez mínima de supervivencia."],
            "gancho": "Si no separás los cables ahora, la explosión será total. Solo el análisis biopsicológico salva imperios."
        },
        "Desbalance": {
            "titulo": "DESBALANCE: La Empresa como Hijo Problemático",
            "diag": "Desplazamiento del afecto. Dejaron de ser amantes para ser 'empleados' de su proyecto. Se pierde erotismo y se gana estrés.",
            "codigo": "Asimetría de Prioridades",
            "tacticas": ["Citas de Desconexión: Tiempo sin pantallas ni temas laborales.", "Auditoría de Energía: ¿Quién carga el peso emocional del proyecto?", "Refuerzo de Identidad: Recordar por qué se unieron antes del negocio."],
            "gancho": "Si el negocio mata la pareja, el negocio morirá también. Usá la empresa como motor, no como tumba."
        },
        "Coherencia": {
            "titulo": "COHERENCIA: El Imperio Familiar",
            "diag": "Integración total. Pareja y empresa son un ecosistema cerrado de alta eficiencia. Soberanía absoluta.",
            "codigo": "Escudo de Gobernanza",
            "tacticas": ["Planificación de Legado: Construcción a 10 años.", "Mantenimiento del Escudo: Revisión trimestral de acuerdos.", "Cultivo de la Intimidad: El afecto es la nafta del motor
