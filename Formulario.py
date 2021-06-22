import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import filedialog as fd
from tkinter import scrolledtext as st
from shutil import move

import Database

class Encuesta:

	def __init__(self, root):
		self.dialogo = tk.Toplevel(root)
		self.database = Database.Pokemons()
		self.presentacion()
		self.cuerpo()
		self.recuperar_imagen()
		self.dialogo.grab_set()

	def presentacion(self):
		self.titulo = ttk.Label(
			self.dialogo,
			text="Poke-Formulario",
			style="Titulo.TLabel",
			font="subtitulo"
		)
		self.titulo.grid(column=0, row=0, padx=5, pady=5)
		parrafo = "Por favor, introduzca todos los datos pedidos del pokemon en el formulario de abajo\n\
en la zona que dice archivo busque la imagen del pokemon.\n\
Nota: La imagen que eligio sera movida a la carpeta imagenes de la pokedex\n\
(tenga en cuenta que la ruta que se le mostrara es la ruta despues de haber\n\
luego de haber movido el archivo)"
		self.parrafo = ttk.Label(
			self.dialogo,
			text=parrafo,
			font="subtitulos",
		)
		self.parrafo.grid(column=0, row=1, padx=5, pady=5)



	def cuerpo(self):
		self.informacion = ttk.Labelframe(self.dialogo, text="Informacion")
		self.informacion.grid(column=0, row=2, padx=5, pady=10, sticky="wn")
		
		self.label2 = ttk.Label(
			self.informacion,
			text="Numero:", 
			style="Datos.TLabel",
			font="datos"
			)
		self.label2.grid(column=0, row=0, padx=5, pady=5, sticky="n")
		self.numero = tk.StringVar()
		self.numero_entry= ttk.Entry(
			self.informacion,
			textvariable=self.numero
			)
		self.numero_entry.grid(column=1, row=0, padx=5, pady=5, sticky="n")

		self.label3 = ttk.Label(
			self.informacion,
			text="Pokemon:",
			style="Datos.TLabel",
			font="datos"
			)	
		self.label3.grid(column=0, row=1, padx=5, pady=5, sticky="n")
		self.pokemon = tk.StringVar()
		self.pokemon_entry = ttk.Entry(
			self.informacion,
			textvariable=self.pokemon
			)
		self.pokemon_entry.grid(column=1, row=1, padx=5, pady=5, sticky="n")

		self.label4 = ttk.Label(
			self.informacion,
			text="Nombre:",
			style="Datos.TLabel",
			font="datos"
			)
		self.label4.grid(column=0, row=2, padx=5, pady=5, sticky="n")
		self.nombre = tk.StringVar()
		self.nombre_entry = ttk.Entry(
			self.informacion,
			textvariable=self.nombre)
		self.nombre_entry.grid(column=1, row=2, padx=5, pady=5, sticky="n")

		self.label5 = ttk.Label(
			self.informacion,
			text="Altura",
			style="Datos.TLabel",
			font="datos"
			)
		self.label5.grid(column=2, row=0, padx=5, pady=5, sticky="n")
		self.altura = tk.StringVar()
		self.altura_entry = ttk.Entry(
			self.informacion, 
			textvariable=self.altura
			)
		self.altura_entry.grid(column=3, row=0, padx=5, pady=4, sticky="n")

		self.label6 = ttk.Label(
			self.informacion,
			text="Peso",
			style="Datos.TLabel",
			font="datos"
			)
		self.label6.grid(column=2, row=1, padx=5, pady=5, sticky="n")
		self.peso = tk.StringVar()
		self.peso_entry = ttk.Entry(
			self.informacion, 
			textvariable=self.peso
			)
		self.peso_entry.grid(column=3, row=1, padx=5, pady=5, sticky="n")

		self.label7 = ttk.Label(
			self.informacion, 
			text="Tipo/Subtipo:",
			style="Datos.TLabel",
			font="datos"
			)
		self.label7.grid(column=2, row=2, padx=5, pady=5, sticky="n")
		self.tipos = tk.StringVar()
		self.tipos_entry = ttk.Entry(
			self.informacion,
			textvariable=self.tipos
			)
		self.tipos_entry.grid(column=3, row=2, padx=5, pady=5, sticky="n")

		self.label8 = ttk.Label(
			self.informacion, 
			text="Comida favorita",
			style="Datos.TLabel",
			font="datos"
			)
		self.label8.grid(column=1, row=3, padx=5, pady=5, sticky="ne")
		self.comida = tk.StringVar()
		self.comida.entry = ttk.Entry(
			self.informacion,
			textvariable=self.comida
			)
		self.comida.entry.grid(column=2, row=3, padx=5, pady=5, sticky="nw")

		self.labelframe = ttk.LabelFrame(self.informacion, text="Decripcion")
		self.labelframe.grid(
			column=0, row=4,
			padx=5, pady=20,
			columnspan=4, sticky="n"
			)
		self.texto = st.ScrolledText(self.labelframe, width=60, height=6)
		self.texto.grid(column=0, row=0, padx=5, pady=5, sticky="we")
	

	def recuperar_imagen(self):
		self.labelframe = ttk.Labelframe(self.dialogo, text="Imagen")
		self.labelframe.grid(column=0, row=4, padx=5, pady=5, sticky="w")
		self.label = ttk.Label(self.labelframe, text="Archivo:")
		self.label.grid(column=0, row=0, padx=5, pady=5, sticky="W")
		self.ruta = tk.StringVar()
		self.entry = ttk.Entry(self.labelframe, width=50, textvariable=self.ruta)
		self.entry.grid(column=1, row=0, padx=5, pady=5, sticky="w")
		self.btn_dialogo = ttk.Button(
			self.labelframe, 
			text="buscar", 
			command=self.buscar_mover
			)
		self.btn_dialogo.grid(column=2, row=0, padx=5, pady=5)
		self.boton = ttk.Button(self.dialogo, text="Guardar", command=self.guardar)
		self.boton.grid(column=0, row=5, padx=5, pady=5)
	
	def buscar_mover(self):
		nombrearch=fd.askopenfilename(initialdir = "/",title = "Seleccione archivo",filetypes = (("archivos png", "*.png"),("todos los archivos","*.*")))
		if nombrearch != "":
			move(nombrearch, r"./imagenes/")
			self.ruta.set("./imagenes/" + os.path.basename(nombrearch))



	def guardar(self):
		datos = (
			self.numero.get(),
			self.pokemon.get(),
			self.nombre.get(),
			self.altura.get(),
			self.peso.get(),
			self.tipos.get(),
			self.comida.get(),
			self.ruta.get(),
			self.texto.get(1.0, tk.END)
			)
		self.database.subir(datos)
		mb.showinfo("Informacion", "Los datos del pokemon fueron guardados!")
		self.numero.set("")
		self.pokemon.set("")
		self.nombre.set("")
		self.altura.set("")
		self.peso.set("")
		self.tipos.set("")
		self.comida.set("")
		self.ruta.set("")