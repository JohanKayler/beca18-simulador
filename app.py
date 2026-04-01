import streamlit as st
from modelo_simple import mi_orden_merito

st.title("Simulador Beca 18 - Segunda Lista")

st.write("Consulta tu posición estimada en la lista de no seleccionados")

dni = st.text_input("Ingresa tu DNI")

if st.button("Consultar"):
    resultado = mi_orden_merito(dni)
    
    if resultado:
        st.success("Resultado encontrado")
        st.write(f"Puntaje: {resultado['puntaje']}")
        st.write(f"Orden de mérito: {resultado['orden']} de {resultado['total_no_seleccionados']}")
        st.write(f"Top {resultado['percent']}%")
        st.write(resultado["mensaje"])
    else:
        st.error("DNI no encontrado")
st.markdown("---")
st.caption("⚠️ Esta herramienta es solo una estimación y no garantiza resultados oficiales.")