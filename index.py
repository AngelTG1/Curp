import tkinter as tk
from tkinter import messagebox, filedialog, ttk
from datetime import datetime
import random

# Determina si un año es bisiesto
def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

# Función para generar CURP
def generar_curp(nombre, apellido_paterno, apellido_materno, dia, mes, anio, sexo, estado="CS"):
    # Obtener iniciales
    curp = (apellido_paterno[0] + 
            next((c for c in apellido_paterno[1:] if c in 'AEIOU'), 'X') +
            apellido_materno[0] + 
            nombre[0]).upper()

    # Agregar fecha de nacimiento en formato AAMMDD
    anio = int(anio) % 100
    curp += f"{anio:02}{int(mes):02}{int(dia):02}"

    # Agregar género y estado
    curp += sexo.upper() + estado.upper()

    # Consonantes internas
    consonantes = (
        next((c for c in apellido_paterno[1:] if c not in 'AEIOU'), 'X') +
        next((c for c in apellido_materno[1:] if c not in 'AEIOU'), 'X') +
        next((c for c in nombre[1:] if c not in 'AEIOU'), 'X')
    )
    curp += consonantes.upper()

    # Dígitos finales aleatorios
    curp += str(random.randint(0, 9)) + str(random.randint(0, 9))

    return curp

# Función para generar y mostrar la CURP
def generar_cadena():
    nombre = entry_nombre.get()
    apellido_paterno = entry_apellido_paterno.get()
    apellido_materno = entry_apellido_materno.get()
    dia = dia_combobox.get()
    mes = mes_combobox.get()
    anio = entry_anio.get()
    sexo = sexo_combobox.get()
    estado = estado_combobox.get()
    
    curp = generar_curp(nombre, apellido_paterno, apellido_materno, dia, mes, anio, sexo, estado)
    messagebox.showinfo("CURP Generada", f"La CURP generada es: {curp}")

# GUI con Tkinter
root = tk.Tk()
root.title("Generador de CURP")

# Campos de entrada
tk.Label(root, text="Nombre(s)*").grid(row=0, column=0, padx=10, pady=5)
entry_nombre = tk.Entry(root)
entry_nombre.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Primer apellido*").grid(row=0, column=2, padx=10, pady=5)
entry_apellido_paterno = tk.Entry(root)
entry_apellido_paterno.grid(row=0, column=3, padx=10, pady=5)

tk.Label(root, text="Segundo apellido").grid(row=1, column=0, padx=10, pady=5)
entry_apellido_materno = tk.Entry(root)
entry_apellido_materno.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Día de nacimiento*").grid(row=1, column=2, padx=10, pady=5)
dia_combobox = ttk.Combobox(root, values=[str(i).zfill(2) for i in range(1, 32)], width=5)
dia_combobox.grid(row=1, column=3, padx=10, pady=5)

tk.Label(root, text="Mes de nacimiento*").grid(row=2, column=0, padx=10, pady=5)
mes_combobox = ttk.Combobox(root, values=[str(i).zfill(2) for i in range(1, 13)], width=5)
mes_combobox.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Año de nacimiento*").grid(row=2, column=2, padx=10, pady=5)
entry_anio = tk.Entry(root)
entry_anio.grid(row=2, column=3, padx=10, pady=5)

tk.Label(root, text="Sexo*").grid(row=3, column=0, padx=10, pady=5)
sexo_combobox = ttk.Combobox(root, values=["H", "M"], width=5)
sexo_combobox.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Estado*").grid(row=3, column=2, padx=10, pady=5)
estado_combobox = ttk.Combobox(root, values=[
    "AS", "BC", "BS", "CC", "CL", "CM", "CS", "CH", "DF", "DG", "GT", 
    "GR", "HG", "JC", "MC", "MN", "MS", "NL", "NT", "OC", "PL", "QT", 
    "QR", "SP", "SL", "SR", "TC", "TS", "TL", "VZ", "YN", "ZS"], width=5)
estado_combobox.set("CS")  # Abreviación de Chiapas como valor predeterminado
estado_combobox.grid(row=3, column=3, padx=10, pady=5)

# Botón para generar CURP
button_generar = tk.Button(root, text="Generar CURP", command=generar_cadena)
button_generar.grid(row=4, column=1, columnspan=2, pady=20)

root.mainloop()
