import streamlit as st

st.title("Clasificador de Clima")

temperatura = st.slider("Temperatura (°C)", min_value=-10, max_value=50, value=25)
humedad = st.slider("Humedad (%)", min_value=0, max_value=100, value=50)
llueve = st.checkbox("¿Está lloviendo?")

if temperatura >= 30:
    if humedad >= 70:
        clasificacion = "Calor húmedo"
    else:
        clasificacion = "Calor seco"
elif temperatura >= 15:
    if llueve:
        clasificacion = "Templado lluvioso"
    else:
        clasificacion = "Templado"
else:
    clasificacion = "Frío"

st.subheader("Resultado")
st.info(f"Clasificación: **{clasificacion}**")

st.write(f"**Temperatura:** {temperatura} °C")
st.write(f"**Humedad:** {humedad}%")
st.write(f"**Lluvia:** {'Sí' if llueve else 'No'}")
