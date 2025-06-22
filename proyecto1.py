import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
#====================================================================================codigo de color:======================================================================================================================0
azul_principal = "#004d66"
azul_claro = "#e6f2f5"
blanco = "#ffffff"
gris = "#f2f2f2"
azul_principal = "#1e3d59"
azul_secundario = "#a8d0e6"
azul_oscuro = "#162c42"
fuente_general = ("Segoe UI", 11)
fuente_titulo = ("Segoe UI", 16, "bold")
fuente_boton = ("Segoe UI", 11, "bold")
#============================================================Clases con herencia ====================================================================
class Persona:
    def __init__(self, nombre, apellidopaterno, apellidomaterno, genero, edad, curp, nss, estado, dias, fecha, meses):
        self.nombre = nombre
        self.apellidopaterno = apellidopaterno
        self.apellidomaterno = apellidomaterno
        self.genero = genero
        self.edad = edad
        self.curp = curp
        self.nss = nss
        self.estado = estado
        self.dias = dias
        self.fecha = fecha
        self.meses = meses

class PersonalHospital:
    def __init__(self, nombre, apellidopa, apellidoma, genero, edad, area):
        self.nombre = nombre
        self.apellidopa = apellidopa
        self.apellidoma = apellidoma
        self.genero = genero
        self.edad = edad
        self.area = area
        self.ocupado = False

class Doctor(PersonalHospital):
    def __init__(self, nombre, apellidopa, apellidoma, genero, edad, area, especialidad):
        super().__init__(nombre, apellidopa, apellidoma, genero, edad, area)
        self.especialidad = especialidad

class Enfermero(PersonalHospital):
    def __init__(self, nombre, apellidopa, apellidoma, genero, edad, area, especialidad):
        super().__init__(nombre, apellidopa, apellidoma, genero, edad, area)
        self.especialidad = especialidad

class Paciente(Persona):
    def __init__(self, nombre, apellidopaterno, apellidomaterno, genero, edad, curp, nss, estado, dias, fecha, meses, area, camilla, doctor, enfermero):
        super().__init__(nombre, apellidopaterno, apellidomaterno, genero, edad, curp, nss, estado, dias, fecha, meses)
        self.area = area
        self.camilla = camilla
        self.doctor = doctor
        self.enfermero = enfermero

# ====================================================Datos iniciales ============================================================================

doctores = [
    Doctor("Dr. Juan", "Perez", "Hernandez", "Masculino", "62", "Urgencias", "Medicina Interna"),
    Doctor("Dr. Pedro", "Hernandez", "Perez", "Masculino", "34", "Hospitalizacion", "Ninguna"),
    Doctor("Dr. Lorenzo", "Sanchez", "Mendez", "Masculino", "45", "Unidad de Cuidados Intensivos", "Cardiologo"),
    Doctor("Dr. Angelica", "Mendez", "Sanchez", "Femenino", "30", "Consulta", "Pediatra"),
]

enfermeros = [
    Enfermero("Enf. Paco", "Escobar", "Ocampo", "Masculino", "27", "Urgencias", "Medicina Interna"),
    Enfermero("Enf. Lupe", "Melchor", "Escobar", "Femenino", "34", "Hospitalización", "Ninguna"),
    Enfermero("Enf. Paquita", "Ocampo", "Melchor", "Femenino", "56", "Unidad de Cuidados Intensivos", "Cardiologo"),
    Enfermero("Enf. Monica", "Mendez", "Sanchez", "Femenino", "30", "Consulta", "Pediatria")
]

camillas = {
    "Urgencias": [{"ocupada": False, "doctor": None, "enfermero": None} for _ in range(5)],
    "Hospitalización": [{"ocupada": False, "doctor": None, "enfermero": None} for _ in range(5)],
    "Unidad de Cuidados Intensivos": [{"ocupada": False, "doctor": None, "enfermero": None} for _ in range(5)],
    "Consulta": [{"ocupada": False, "doctor": None, "enfermero": None} for _ in range(5)],
}

pacientes = []

#===================================================Funciones importantes======================================================================
def asignar_camilla(area):
    for i, camilla in enumerate(camillas[area]):
        if not camilla["ocupada"]:
            doc = next((d for d in doctores if d.area == area and not d.ocupado), None)
            enf = next((e for e in enfermeros if e.area == area and not e.ocupado), None)

            if doc is None or enf is None:
                return None, None, None

            camilla["ocupada"] = True
            camilla["doctor"] = doc
            camilla["enfermero"] = enf
            doc.ocupado = True
            enf.ocupado = True
            return i + 1, doc, enf
    return None, None, None

def registrar_paciente(entry_nombre, entry_apellidopaterno, entry_apellidomaterno, combo_genero, entry_edad, entry_curp, entry_nss, entry_estado, combo_dias, combo_fecha, combo_meses, combo_area):
    nombre = entry_nombre.get().strip()
    apellidopaterno = entry_apellidopaterno.get().strip()
    apellidomaterno = entry_apellidomaterno.get().strip()
    genero = combo_genero.get().strip()
    edad = entry_edad.get().strip()
    curp = entry_curp.get().strip()
    nss = entry_nss.get().strip()
    estado = entry_estado.get().strip()
    dias = combo_dias.get().strip()
    fecha = combo_fecha.get().strip()
    meses = combo_meses.get().strip()
    area = combo_area.get().strip()

    if not nombre or not apellidopaterno or not apellidomaterno or not genero or not edad or not curp or not nss or not estado or not dias or not fecha or not meses or not area:
        messagebox.showerror("Error", "Complete todos los campos")
        return
    try:
        edad = int(edad)
    except ValueError:
        messagebox.showerror("Error", "Edad debe ser un número")
        return

    camilla_num, doc, enf = asignar_camilla(area)
    if camilla_num is None:
        messagebox.showerror("Error", f"No hay camillas o personal disponible en {area}")
        return

    paciente = Paciente(nombre, apellidopaterno, apellidomaterno, genero, edad, curp, nss, estado, dias, fecha, meses, area, camilla_num, doc, enf)
    pacientes.append(paciente)
    messagebox.showinfo("Éxito", f"Paciente: {nombre} registrado en camilla:  {camilla_num} de:{area}")

    entry_nombre.delete(0, tk.END)
    entry_apellidopaterno.delete(0, tk.END)
    entry_apellidomaterno.delete(0, tk.END)
    combo_genero.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    entry_curp.delete(0, tk.END)
    entry_nss.delete(0, tk.END)
    entry_estado.delete(0, tk.END)
    combo_dias.delete(0, tk.END)
    combo_fecha.delete(0, tk.END)
    combo_meses.delete(0, tk.END)

def mostrar_pacientes():
    ventana = tk.Toplevel()
    ventana.title("Pacientes")

    cols = ("Nombre", "Apellido Paterno", "Apellido Materno", "Genero", "Edad", "CURP", "NSS", "Estado", "Dia", "Fecha", "Mes", "Área", "Camilla", "Doctor", "Enfermero")
    tree = ttk.Treeview(ventana, columns=cols, show="headings")

    for col in cols:
        tree.heading(col, text=col)
        tree.column(col, width=100)

    for p in pacientes:
        tree.insert("", tk.END, values=(
            p.nombre,
            p.apellidopaterno,
            p.apellidomaterno,
            p.genero,
            p.edad,
            p.curp,
            p.nss,
            p.estado,
            p.dias,
            p.fecha,
            p.meses,
            p.area,
            p.camilla,
            p.doctor.nombre if p.doctor else "N/A",
            p.enfermero.nombre if p.enfermero else "N/A"
        ))

    tree.pack(expand=True, fill=tk.BOTH)

#==============================================Codigo de la ventana secundaria de Eleccion=================================================================0
def abrirseleccion():#funcion que permite abrir esta ventana
    ventanadeeleccion = tk.Toplevel(ventanaprincipal)
    ventanadeeleccion.title("Seleccionar rol")
    ventanadeeleccion.geometry("420x320")
    ventanadeeleccion.configure(bg=azul_secundario)
    #Encabezado
    encabezado = tk.Frame(ventanadeeleccion, bg=azul_principal, height=60)
    encabezado.pack(fill="x")
    tk.Label(encabezado, text="¿Quién eres?", fg=blanco, bg=azul_principal,font=fuente_titulo, pady=10).pack()

    menu = tk.Frame(ventanadeeleccion, bg=azul_secundario, pady=20)
    menu.pack(expand=True)

    tk.Button(menu, text="Paciente", font=fuente_boton, bg=azul_principal, fg=blanco,activebackground=azul_oscuro, activeforeground=blanco,
                  bd=0, relief="ridge", padx=20, pady=8, command=lambda: registropacientes(ventanadeeleccion)).pack(pady=10, fill="x")
    tk.Button(menu, text="Doctor", font=fuente_boton, bg=azul_principal, fg=blanco,activebackground=azul_oscuro, activeforeground=blanco,
                  bd=0, relief="ridge", padx=20, pady=8).pack(pady=10, fill="x")
    tk.Button(menu, text="Enfermero", font=fuente_boton, bg=azul_principal, fg=blanco,activebackground=azul_oscuro, activeforeground=blanco,
                  bd=0, relief="ridge", padx=20, pady=8).pack(pady=10, fill="x")
    
#==================================================Codigo de la ventana de Pacientes==========================================================
def registropacientes(ventanadeeleccion):
    ventanadeeleccion.withdraw()
    ventanapacientes=tk.Toplevel(ventanadeeleccion)
    ventanapacientes.title("Registro de Pacientes")
    ventanapacientes.configure(bg=gris)
    # Encabezado
    encabezado = tk.Frame(ventanapacientes, bg=azul_principal, height=50)
    encabezado.pack(side="top", fill="x")
    tk.Label(encabezado, text="Formulario de Pacientes", fg="white", bg=azul_principal,font=("Helvetica", 16, "bold")).pack(pady=10)
    #Formulario de registro del paciente
    frame_formulario = tk.Frame(ventanapacientes, bg=gris)
    frame_formulario.pack()
    
    tk.Label(frame_formulario, text="Nombres:", bg=gris, font=fuente_general).grid(row=0, column=0)
    entry_nombre= tk.Entry(frame_formulario, font=fuente_general)
    entry_nombre.grid(row=0, column=1)
    
    tk.Label(frame_formulario, text="Apellido paterno:", bg=gris, font=fuente_general).grid(row=1, column=0)
    entry_apellidopaterno= tk.Entry(frame_formulario, font=fuente_general)
    entry_apellidopaterno.grid(row=1, column=1)
    
    tk.Label(frame_formulario, text="Apellido materno:", bg=gris, font=fuente_general).grid(row=2, column=0)
    entry_apellidomaterno = tk.Entry(frame_formulario, font=fuente_general)
    entry_apellidomaterno.grid(row=2, column=1)

    tk.Label(frame_formulario, text="Genero:", bg=gris, font=fuente_general).grid(row=3, column=0)
    combo_genero = ttk.Combobox(frame_formulario, values=["Masculino", "Femenino"])
    combo_genero.grid(row=3, column=1)
    combo_genero.current(0)

    tk.Label(frame_formulario, text="Edad:", bg=gris, font=fuente_general).grid(row=4, column=0)
    entry_edad = tk.Entry(frame_formulario, font=fuente_general)
    entry_edad.grid(row=4, column=1)

    tk.Label(frame_formulario, text="CURP:", bg=gris, font=fuente_general).grid(row=5, column=0)
    entry_curp = tk.Entry(frame_formulario, font=fuente_general)
    entry_curp.grid(row=5, column=1)

    tk.Label(frame_formulario, text="Numero de Seguridad Social:", bg=gris, font=fuente_general).grid(row=6, column=0)
    entry_nss = tk.Entry(frame_formulario, font=fuente_general)
    entry_nss.grid(row=6, column=1)

    tk.Label(frame_formulario, text="Estado del Paciente:", bg=gris, font=fuente_general).grid(row=7, column=0)
    entry_estado = tk.Entry(frame_formulario, font=fuente_general)
    entry_estado.grid(row=7, column=1)

    tk.Label(frame_formulario, text="Día:", bg=gris, font=fuente_general).grid(row=8, column=0)
    combo_dias = ttk.Combobox(frame_formulario, values=["Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"])
    combo_dias.grid(row=8, column=1)
    combo_dias.current(0)

    tk.Label(frame_formulario, text="Fecha:", bg=gris, font=fuente_general).grid(row=9, column=0)
    combo_fecha = ttk.Combobox(frame_formulario, values=[str(i) for i in range(1, 32)])
    combo_fecha.grid(row=9, column=1)
    combo_fecha.current(0)

    tk.Label(frame_formulario, text="Mes:", bg=gris, font=fuente_general).grid(row=10, column=0)
    combo_meses = ttk.Combobox(frame_formulario, values=["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio",
                                                    "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"])
    combo_meses.grid(row=10, column=1)
    combo_meses.current(0)

    tk.Label(frame_formulario, text="Área:", bg=gris, font=fuente_general).grid(row=11, column=0)
    combo_area = ttk.Combobox(frame_formulario, values=list(camillas.keys()), state="readonly")
    combo_area.grid(row=11, column=1)

    def regresar():
        ventanapacientes.destroy()
        ventanadeeleccion.deiconify()

    tk.Button(frame_formulario, text="Registrar Paciente",font=fuente_boton, bg=azul_principal,fg=blanco, command=lambda: registrar_paciente(entry_nombre, entry_apellidopaterno, entry_apellidomaterno, combo_genero, entry_edad, entry_curp, entry_nss, entry_estado, combo_dias, combo_fecha, combo_meses, combo_area)).grid(row=12, column=0, columnspan=2, pady=5)
   
    menupacientes=tk.Menu(ventanapacientes)
    opciones= tk.Menu(menupacientes, tearoff=0)
    opciones.add_command(label="Regresar", command=regresar)
    opciones.add_command(label="Mostrar pacientes", command=mostrar_pacientes)
    menupacientes.add_cascade(label="Opciones", menu=opciones)
    ventanapacientes.config(menu=menupacientes)
  
    
#==============================================================================================Ventana Principal===========================================================================================================
ventanaprincipal = tk.Tk()
ventanaprincipal.title("Hospital Ángeles")
ventanaprincipal.geometry("450x350")
ventanaprincipal.configure(bg=azul_secundario)
tk.Label(ventanaprincipal, text="HOSPITAL ÁNGELES", font=("Segoe UI", 22, "bold"),fg=azul_principal, bg=azul_secundario ).pack(pady=20)
tk.Label(ventanaprincipal, text="Donde la salud y el cuidado se encuentran", font=("Segoe UI", 12, "italic"), fg=azul_oscuro, bg=azul_secundario).pack(pady=(0, 30))
tk.Button(ventanaprincipal, text="Ingresar", font=fuente_boton, bg=azul_principal, fg=blanco, activebackground=azul_oscuro, activeforeground=blanco,bd=0, relief="flat", width=18, pady=10, command=abrirseleccion).pack(pady=8)
tk.Button(ventanaprincipal, text="Salir", font=fuente_boton, bg=azul_principal, fg=blanco, activebackground=azul_oscuro, activeforeground=blanco,bd=0, relief="flat", width=18, pady=10,command=ventanaprincipal.destroy ).pack(pady=8)
ventanaprincipal.mainloop()
