import tkinter as tk
from tkinter import messagebox, filedialog
from datetime import datetime

# Determina si un año es bisiesto
def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def validar_curp_por_estados(curp):

    estado = "q0"
    if len(curp) != 18:
        return False
    estado = "q1"
    
    # Estado q1: Validar letras iniciales (apellido paterno, apellido materno, y nombre)
    # Primera letra del apellido paterno: debe ser una letra mayúscula
    if not ('A' <= curp[0] <= 'Z'):
        return False
    # Segunda letra debe ser una vocal
    if curp[1] not in "AEIOU":
        return False
    # Tercera y cuarta letras deben ser letras mayúsculas (inicial del apellido materno y nombre)
    if not ('A' <= curp[2] <= 'Z') or not ('A' <= curp[3] <= 'Z'):
        return False
    estado = "q2"
    
    # Estado q2: Validar fecha de nacimiento en formato AAMMDD
    try:
        anio = int(curp[4:6])
        mes = int(curp[6:8])
        dia = int(curp[8:10])
        anio_completo = 1900 + anio if anio > 30 else 2000 + anio

        # Estado q3: Validación del mes y día considerando años bisiestos
        if mes < 1 or mes > 12:
            return False
        if mes == 2:
            # Si es febrero, verificar días según si es año bisiesto
            if es_bisiesto(anio_completo) and dia > 29:
                return False
            elif not es_bisiesto(anio_completo) and dia > 28:
                return False
        elif mes in {4, 6, 9, 11} and dia > 30:
            return False
        elif dia > 31:
            return False
        estado = "q3"
    except ValueError:
        return False

    # Estado q4: Validar género
    if curp[10] not in ['H', 'M']:
        return False
    estado = "q5"

    # Estado q5: Validar entidad federativa
    entidad = curp[11:13]
    entidades_validas = {
        'AS', 'BC', 'BS', 'CC', 'CL', 'CM', 'CS', 'CH', 'DF', 'DG', 'GT', 
        'GR', 'HG', 'JC', 'MC', 'MN', 'MS', 'NL', 'NT', 'OC', 'PL', 'QT', 
        'QR', 'SP', 'SL', 'SR', 'TC', 'TS', 'TL', 'VZ', 'YN', 'ZS'
    }
    if entidad not in entidades_validas:
        return False
    estado = "q6"

    # Estado q6: Validar consonantes internas en los nombres
    consonantes_internas = curp[13:16]
    for consonante in consonantes_internas:
        if consonante not in "BCDFGHJKLMNÑPQRSTVWXYZ":
            return False
    estado = "q7"

    # Estado q7: Validar último carácter para evitar duplicados
    if not (curp[16].isalnum() and curp[17].isalnum()):
        return False
    estado = "q_accept"

    # CURP válida si alcanzamos el estado de aceptación
    return estado == "q_accept"

# Función para validar la CURP ingresada
def validar_cadena():
    curp = entry.get().upper()
    if validar_curp_por_estados(curp):
        messagebox.showinfo("Resultado", f"La CURP '{curp}' es válida.")
    else:
        messagebox.showerror("Resultado", f"La CURP '{curp}' es inválida.")

# Cargar archivo y validar CURPs
def cargar_archivo():
    archivo_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if archivo_path:
        with open(archivo_path, 'r') as archivo:
            lineas = archivo.readlines()
            resultados = []
            for linea in lineas:
                curp = linea.strip().upper()
                if validar_curp_por_estados(curp):
                    resultados.append(f"La CURP '{curp}' es válida.\n")
                else:
                    resultados.append(f"La CURP '{curp}' es inválida.\n")
            messagebox.showinfo("Resultados", "".join(resultados))

# GUI con Tkinter
root = tk.Tk()
root.title("Validador de CURP")

label = tk.Label(root, text="Ingrese una CURP o cargue un archivo:", font=("Arial", 14))
label.pack(pady=10)

entry = tk.Entry(root, width=30, font=("Arial", 14))
entry.pack(pady=10)

button_validar = tk.Button(root, text="Validar", command=validar_cadena, font=("Arial", 14))
button_validar.pack(pady=10)

button_archivo = tk.Button(root, text="Cargar archivo", command=cargar_archivo, font=("Arial", 14))
button_archivo.pack(pady=10)

root.mainloop()
