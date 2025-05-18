import streamlit  as st

# Configuración de la página
st.set_page_config(layout="wide")
st.title("Monitoreo de Deforestación en Brasil")

# Sidebar - Filtros
st.sidebar.header("Filtros")
year = st.sidebar.slider("Año", 2000, 2025, 2023)
region = st.sidebar.selectbox("Región", ["Amazonas", "Pará", "Rondônia", "Mato Grosso"])

# Datos simulados (sin geometría)
def cargar_datos():
    return [
        {"year": 2023, "region": "Amazonas", "area_km2": 150.5},
        {"year": 2023, "region": "Amazonas", "area_km2": 200.2},
        {"year": 2023, "region": "Pará", "area_km2": 300.1},
        {"year": 2022, "region": "Pará", "area_km2": 180.0},
        {"year": 2023, "region": "Rondônia", "area_km2": 90.5},
    ]

# Filtrar datos
datos = cargar_datos()
datos_filtrados = [d for d in datos if d["year"] == year and d["region"] == region]

# Mostrar tabla de datos filtrados
st.subheader(f"Datos de deforestación en {region} - {year}")
if datos_filtrados:
    st.table(datos_filtrados)
    area_total = sum(d["area_km2"] for d in datos_filtrados)
    st.metric("Área deforestada", f"{area_total:.2f} km²")
else:
    st.warning("No se encontraron datos para el año y región seleccionados.")
    
