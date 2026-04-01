import pandas as pd 

df_seleccionados = pd.read_csv("data/postulantes_seleccionados.csv")
df_no_seleccionados = pd.read_csv("data/postulantes_no_seleccionados.csv")

df = pd.concat([df_seleccionados, df_no_seleccionados], ignore_index=True)

df_limpio = df[[
    "MODALIDAD_BECA","DNI","IES","CARRERA",
    "CONCEPTO_A","CONCEPTO_B","PUNTAJE_FINAL","CONDICION"
]]

df_limpio = df_limpio[df_limpio["MODALIDAD_BECA"] == "BECA 18 ORDINARIA"]

df_limpio["DNI"] = df_limpio["DNI"].astype(str).str.strip()


def mi_orden_merito(dni):
    dni = str(dni).strip()

    no_sel = df_limpio[df_limpio["CONDICION"] == "NO SELECCIONADO"].copy()

    no_sel = no_sel.sort_values("PUNTAJE_FINAL", ascending=False).reset_index(drop=True)
    no_sel["ORDEN_MERITO"] = no_sel.index + 1

    resultado = no_sel[no_sel["DNI"] == dni]

    if resultado.empty:
        return None  

    orden = int(resultado["ORDEN_MERITO"].values[0])
    puntaje = float(resultado["PUNTAJE_FINAL"].values[0])
    total = len(no_sel)

    top_percent = round((orden / total) * 100, 2)

    if orden <= 2173:
        mensaje = "🟢 Alta probabilidad de ser seleccionado en segunda lista"
    elif orden <= 3000:
        mensaje = "🟡 Probabilidad media (depende de reasignaciones)"
    else:
        mensaje = "🔴 Baja probabilidad"

    return {
        "puntaje": puntaje,
        "orden_merito": orden,
        "total_no_seleccionados": total,
        "top_percent": top_percent,
        "estimacion": mensaje
    }