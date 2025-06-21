import tkinter as tk
from tkinter import ttk
#codigo de color:
blanco = "#ffffff"
azul_principal = "#1e3d59"
azul_secundario = "#a8d0e6"
azul_oscuro = "#162c42"
fuente_boton = ("Segoe UI", 11, "bold")
ventanaprincipal = tk.Tk()
ventanaprincipal.title("Hospital Ángeles")
ventanaprincipal.geometry("450x350")
ventanaprincipal.configure(bg=azul_secundario)
tk.Label(ventanaprincipal, text="HOSPITAL ÁNGELES", font=("Segoe UI", 22, "bold"),fg=azul_principal, bg=azul_secundario ).pack(pady=20)
tk.Label(ventanaprincipal, text="Donde la salud y el cuidado se encuentran", font=("Segoe UI", 12, "italic"), fg=azul_oscuro, bg=azul_secundario).pack(pady=(0, 30))
tk.Button(ventanaprincipal, text="Ingresar", font=fuente_boton, bg=azul_principal, fg=blanco, activebackground=azul_oscuro, activeforeground=blanco,bd=0, relief="flat", width=18, pady=10).pack(pady=8)
tk.Button(ventanaprincipal, text="Salir", font=fuente_boton, bg=azul_principal, fg=blanco, activebackground=azul_oscuro, activeforeground=blanco,bd=0, relief="flat", width=18, pady=10,command=ventanaprincipal.destroy ).pack(pady=8)
ventanaprincipal.mainloop()
